# import os
# import pandas as pd
# from pandas import DataFrame
# from filemapper import FileMapper as fm
# from filemapper.utils.Metadata import Metadata
# from filemapper.utils.TreeRoot import TreeRoot
# from filemapper.metadata import online_retrieve_module as onrmod
# from filemapper.utils.FileFlags import FileFlags as FFLAGS
from pandas import DataFrame

from filemapper.metadata.Metadata import Metadata
from filemapper.pandas.PandasAnimeExtension import PandasAnimeExtension
from filemapper.pandas.PandasFilmExtension import PandasFilmExtension
from filemapper.pandas.PandasShowExtension import PandasShowExtension
from filemapper.pandas.PandasUtils import PandasUtils


class PandasEngine():
    def __init__(self, tree):
        self.tree = tree
        self.old_dataframe = DataFrame()
        self.new_dataframe = DataFrame()
        self.pandas_utils = PandasUtils()
        self.pandas_extension = [PandasShowExtension(), PandasFilmExtension(),
                                 PandasAnimeExtension()]
        return

    def create_library(self, debug=False):
        root_basename = self.tree.nodes[0].basename
        self.old_dataframe = self.pandas_utils.create_data_frame(tree=self.tree,
                                                                 debug=debug)

        dataframe = self.old_dataframe
        for extension in self.pandas_extension:
            dataframe = extension.create_default_library(dataframe=dataframe,
                                                         root_basename=root_basename)

        self.new_dataframe = dataframe
        if debug:
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8
            print('Final Dataframe')
            print self.new_dataframe
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8
        return self.new_dataframe

    def calculate_rows(self):
        return len(self.new_dataframe.index), (len(self.old_dataframe)), (
            len(self.new_dataframe) - len(self.old_dataframe))

    def update_tree(self, debug=False):
        _total_rows, _old_rows, _new_rows = self.calculate_rows()
        old_dataframe = self.old_dataframe
        dataframe = self.new_dataframe
        tree = self.tree

        if debug:
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8
            print ('MetadataTree MetadataNodes               :: {total}').format(total=_total_rows)
            print ('MetadataTree MetadataNodes to be added   :: {new}').format(new=_new_rows)

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

            tree.add_node(basename=basename, metadata=metadata,
                          parent_basename=parent)

        if debug:
            print ('MetadataTree MetadataNodes to be updated :: {old}').format(
                old=_old_rows)
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8

        for index in range(0, len(old_dataframe.index), 1):
            current_basename = dataframe.iloc[int(index)]['basename']
            current_parent = dataframe.iloc[int(index)]['parent']
            node = tree.search(basename=current_basename)
            old_parent_basename = node[0].parent_basename
            if current_parent != old_parent_basename:
                # print('------'*20)
                # print('Input: index({index}) basename: {base} - [Parent]: old: {old_parent}'.format(index=index, old_parent=old_parent_basename, base=node.basename))
                # print('Onput: index({index}) basename: {basename} - [Parent]: new: {new_parent}'.format(index=index, basename=current_basename, new_parent=current_parent))
                tree.update_parent_node_by_index(index=int(index),
                                                 parent=current_parent)

        tree.tree()
        return tree

#
