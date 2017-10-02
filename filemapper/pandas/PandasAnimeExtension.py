import os
import pandas as pd
from pandas import DataFrame
from filemapper import FileMapper as fm
from filemapper.datastructure.Metadata import Metadata
from filemapper.datastructure.TreeRoot import TreeRoot
from filemapper.metadata import online_retrieve_module as onrmod
from filemapper.datastructure.FileFlags import FileFlags as FFLAGS
from filemapper.pandas.PandasUtils import PandasUtils

class PandasAnimeExtension():
    def __init__(self):
        self.pandas_utils = PandasUtils()
        return

    def retrieve_animes_directories(self, dataframe, current_anime, drop_dup=False):
        if drop_dup:
            dataframe_episodes_directories = dataframe.groupby(['name']).get_group(current_anime).drop_duplicates()
        else:
            dataframe_episodes_directories = dataframe.groupby(['name']).get_group(current_anime)
        return dataframe_episodes_directories[dataframe_episodes_directories.fflag == FFLAGS.ANIME_DIRECTORY_FLAG]

    def retrieve_animes(self, dataframe, current_anime, drop_dup=False):
        if drop_dup:
            dataframe_episodes = dataframe.groupby(['name']).get_group(current_anime).drop_duplicates()
        else:
            dataframe_episodes = dataframe.groupby(['name']).get_group(current_anime)
        return dataframe_episodes[dataframe_episodes.fflag == FFLAGS.ANIME_FLAG]


    def create_main_anime_directory(self, dataframe, current_serie=str):
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe, name=current_serie, season='N/A', episode='N/A',
                                      fflag=FFLAGS.MAIN_SHOW_DIRECTORY_FLAG, basename=current_serie, parent='Animes')
        return dataframe

    def create_animes_directory(self, dataframe, library=str):
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe, name='Animes', season='', episode='',
                                      fflag=FFLAGS.LIBRARY_FLAG, basename='Animes', parent=library)
        return dataframe

    def create_default_anime_tree_directory(self, dataframe, current_anime=str, library=str, with_dir=True):
        main_show_directory = dataframe[dataframe['basename'] == current_anime]
        if main_show_directory.empty:
            dataframe = self.create_main_anime_directory(dataframe=dataframe, current_serie=current_anime)
        else:
            dataframe = self.pandas_utils.update_parent_dataframe_row(dataframe=dataframe, index=int(main_show_directory.index), parent='Animes')

        dataframe_episodes_directories = self.retrieve_animes_directories(dataframe=dataframe, current_anime=current_anime)
        dataframe_episodes = self.retrieve_animes(dataframe=dataframe, current_anime=current_anime)

        # reset index to simply iterate over the rows, extracting the values, to create the directory tree
        dataframe_temp = dataframe_episodes.reindex()
        for index in range(0, len(dataframe_temp.index), 1):
            name = dataframe_temp.iloc[int(index)]['name']
            episode = dataframe_temp.iloc[int(index)]['episode']
            basename = dataframe_temp.iloc[int(index)]['basename']
            parent = dataframe_temp.iloc[int(index)]['parent']
            season = dataframe_temp.iloc[int(index)]['season']

            dataframe_directory = dataframe_episodes_directories[dataframe_episodes_directories.basename == basename[:-4]]
            real_index = dataframe_episodes.index[dataframe_episodes.basename == basename]
            if dataframe_directory.empty:
                print('CREATED: ' + str(basename[:-4]))
                real_index = real_index.tolist()[0]
                dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe, name=name, season=season, episode=episode, fflag=FFLAGS.SHOW_DIRECTORY_FLAG, basename=basename[:-4], parent=parent)
                dataframe = self.pandas_utils.update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent=basename[:-4])

        dataframe_temp = dataframe_episodes_directories.reindex()
        for index in range(0, len(dataframe_temp.index), 1):
            name = dataframe_temp.iloc[int(index)]['name']
            basename = dataframe_temp.iloc[int(index)]['basename']
            parent = dataframe_temp.iloc[int(index)]['parent']
            real_index = dataframe_episodes_directories.index[dataframe_episodes_directories.basename == basename]
            if parent not in 'Animes':
                real_index = real_index.tolist()[0]
                dataframe = self.pandas_utils.update_parent_dataframe_row(dataframe=dataframe, index=real_index, parent=current_anime)
        return dataframe