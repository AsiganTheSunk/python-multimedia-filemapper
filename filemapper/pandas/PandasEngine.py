# import os
# import pandas as pd
# from pandas import DataFrame
# from filemapper import FileMapper as fm
# from filemapper.datastructure.Metadata import Metadata
# from filemapper.datastructure.TreeRoot import TreeRoot
# from filemapper.metadata import online_retrieve_module as onrmod
# from filemapper.datastructure.FileFlags import FileFlags as FFLAGS
from filemapper.datastructure.TreeRoot import TreeRoot
from pandas import DataFrame
from filemapper.pandas.PandasAnimeExtension import PandasAnimeExtension
from filemapper.pandas.PandasShowExtension import PandasShowExtension
from filemapper.pandas.PandasFilmExtension import PandasFilmExtension
from filemapper.pandas.PandasUtils import PandasUtils

class PandasEngine():
    def __init__(self, tree):
        self.tree = tree
        self.old_dataframe = DataFrame()
        self.new_dataframe = DataFrame()
        self.pandas_utils = PandasUtils()
        self.pandas_extension = [PandasShowExtension(), PandasFilmExtension(), PandasAnimeExtension()]
        return

    def create_library(self, tree):
        self.old_dataframe = self.pandas_utils.create_data_frame(self.tree)
        dataframe = self.old_dataframe

        for extension in self.pandas_extension:
            dataframe = extension.create_default_library(dataframe=dataframe, tree_root=tree)
        self.new_dataframe = dataframe
        return dataframe


#     def update_tree_info(old_dataframe, dataframe, tree):
#         total_rows = len(dataframe.index)
#         new_rows = total_rows - len(old_dataframe.index)
#         print('--: New nodes to be Added to the tree: (' + str(new_rows) + '/' + str(total_rows) + ')')
#         for index in range(len(old_dataframe.index), len(dataframe.index), 1):
#             name = dataframe.iloc[int(index)]['name']
#             season = dataframe.iloc[int(index)]['season']
#             episode = dataframe.iloc[int(index)]['episode']
#             basename = dataframe.iloc[int(index)]['basename']
#             parent = dataframe.iloc[int(index)]['parent']
#             # print('index: ' + str(index), 'basename: ' + str(basename),  'parent: ' + str(parent))
#             # print('name: ' + str(name),'season: ' + str(season),'episode: ' + str(episode))
#             metadata = Metadata()
#             metadata.set_name(name)
#             if season not in 'N/A':
#                 metadata.set_season(season)
#             if episode not in 'N/A':
#                 metadata.set_episode(episode)
#             tree.add_node(basename=basename, metadata=metadata, parent_basename=parent)
#
#         print(
#         '--: Nodes that need to be Updated in the tree: (' + str(len(old_dataframe)) + '/' + str(total_rows) + ')')
#         for index in range(0, len(old_dataframe.index), 1):
#             current_basename = dataframe.iloc[int(index)]['basename']
#             current_parent = dataframe.iloc[int(index)]['parent']
#             node = tree.search(basename=current_basename)
#             node = node[0]
#             old_parent_basename = node.parent_basename
#             if current_parent != old_parent_basename:
#                 # print('------'*20)
#                 # print('Input: index({index}) basename: {base} - [Parent]: old: {old_parent}'.format(index=index, old_parent=old_parent_basename, base=node.basename))
#                 # print('Onput: index({index}) basename: {basename} - [Parent]: new: {new_parent}'.format(index=index, basename=current_basename, new_parent=current_parent))
#                 tree.update_parent_node_by_index(index=int(index), parent=current_parent)
#
#         return tree
#
