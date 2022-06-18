# import os
# import cross_reference_engine as pd
# from cross_reference_engine import DataFrame
# from filemapper import FileMapper as fm
# from filemapper.utils.Metadata import Metadata
# from filemapper.utils.TreeRoot import TreeRoot
# from filemapper.metadata_engine import online_retrieve_module as onrmod
# from filemapper.utils.FileFlags import FileFlags as FFLAGS
from pandas import DataFrame

from multimedia_filemapper.core.metadata_engine.core.metadataengine import Metadata
from multimedia_filemapper.core.cross_reference_engine.extensions.pandas_anime_extension import PandasAnimeExtension
from multimedia_filemapper.core.cross_reference_engine.extensions.pandas_film_extension import PandasFilmExtension
from multimedia_filemapper.core.cross_reference_engine.extensions.pandas_show_extension import PandasShowExtension
from multimedia_filemapper.core.cross_reference_engine.core.utils.pandasutils import PandasUtils


class PandasEngine:
    def __init__(self):
        self.old_dataframe = DataFrame()
        self.new_dataframe = DataFrame()
        self.pandas_utils = PandasUtils()
        self.pandas_extension = [
            PandasShowExtension(),
            PandasFilmExtension(),
            PandasAnimeExtension(),
        ]

    def create_library(self, tree):
        self.old_dataframe = self.pandas_utils.create_data_frame(tree=tree)
        for extension in self.pandas_extension:
            print(f'[ {extension.__class__.__name__} ]')
            self.old_dataframe = \
                extension.create_default_library(dataframe=self.old_dataframe, root_basename=tree.nodes[0].basename)
        print(self.old_dataframe)
        print('==================' * 15)
        return self.old_dataframe

    def calculate_rows(self):
        return len(self.new_dataframe.index), (len(self.old_dataframe)), (
            len(self.new_dataframe) - len(self.old_dataframe))

    def update_tree(self, tree):
        _total_rows, _old_rows, _new_rows = self.calculate_rows()
        old_dataframe = self.old_dataframe
        dataframe = self.new_dataframe

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8)
        print(f'MetadataTree MetadataNodes               :: {_total_rows}')
        print(f'MetadataTree MetadataNodes to be added   :: {_new_rows}')

        for index in range(len(old_dataframe.index), len(dataframe.index), 1):
            name = dataframe.iloc[int(index)]['name']
            season = dataframe.iloc[int(index)]['season']
            episode = dataframe.iloc[int(index)]['episode']
            basename = dataframe.iloc[int(index)]['basename']
            parent = dataframe.iloc[int(index)]['parent']
            year = dataframe.iloc[int(index)]['year']
            genre = dataframe.iloc[int(index)]['genre']
            n_season = dataframe.iloc[int(index)]['n_season']
            e_season = dataframe.iloc[int(index)]['e_season']

            metadata = Metadata(
                name=self.pandas_utils.clean_empty_value(value=name),
                season=self.pandas_utils.clean_empty_value(value=season),
                episode=self.pandas_utils.clean_empty_value(value=episode),
                year=self.pandas_utils.clean_empty_value(value=year),
                genre=self.pandas_utils.clean_empty_value(value=genre),
                n_season=self.pandas_utils.clean_empty_value(value=n_season),
                e_season=self.pandas_utils.clean_empty_value(value=e_season))

            tree.add_node(basename=basename, metadata=metadata, parent_basename=parent)

        print(f'MetadataTree MetadataNodes to be updated :: {_old_rows}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8)

        for index in range(0, len(old_dataframe.index), 1):
            current_basename = dataframe.iloc[int(index)]['basename']
            current_parent = dataframe.iloc[int(index)]['parent']
            node = tree.search(basename=current_basename)
            old_parent_basename = node[0].parent_basename
            if current_parent != old_parent_basename:
                # print('------'*20)
                # print('Input: index({index}) basename: {base} - [Parent]: old: {old_parent}'.format(index=index, old_parent=old_parent_basename, base=node.basename))
                # print('Onput: index({index}) basename: {basename} - [Parent]: new: {new_parent}'.format(index=index, basename=current_basename, new_parent=current_parent))
                tree.update_parent_node_by_index(index=int(index), parent=current_parent)

        tree.tree()
        return tree

#
