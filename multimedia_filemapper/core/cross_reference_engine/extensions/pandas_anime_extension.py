from multimedia_filemapper.core.cross_reference_engine.core.utils.pandasutils import PandasUtils
from multimedia_filemapper.core.constants.media_file_flags import FileFlags


class PandasAnimeExtension:
    def __init__(self):
        self.pandas_utils = PandasUtils()

    def create_default_library(self, dataframe, root_basename):
        """
        This function creates a default library structure in cross_reference_engine for films
        :param dataframe: It represents the dataframe input for this function
        :param tree_root: basename of the tree_root structure
        :return: DATAFRAME
        """
        unique_anime = self.get_anime_names(dataframe=dataframe)
        dataframe = self.create_animes_directory(dataframe=dataframe, root_basename=root_basename)
        for current_anime in unique_anime:
            dataframe = self.create_default_anime_tree_directory(dataframe=dataframe, current_anime=current_anime)
        return dataframe

    def get_anime_names(self, dataframe):
        """
        This function returns the unique values for film names
        :param dataframe: It represents the dataframe input for this function
        :return: UNIQUE_ANIMES
        """
        unique_anime = dataframe.name[dataframe['fflag'] == FileFlags.ANIME_FLAG].unique()
        return unique_anime

    def get_anime(self, dataframe, current_anime, drop_dup=False):
        """
        This function returns the files with anime_flag
        :param dataframe: It represents the dataframe input for this function
        :param current_anime: It represents the basename of the current anime your mapping
        :param drop_dup: Drop duplicated values by default
        :return:
        """
        if drop_dup:
            dataframe_episodes = dataframe.groupby(['name']).get_group(current_anime).drop_duplicates()
        else:
            dataframe_episodes = dataframe.groupby(['name']).get_group(current_anime)
        return dataframe_episodes[dataframe_episodes.fflag == FileFlags.ANIME_FLAG]

    def get_anime_directories(self, dataframe, current_anime, drop_dup=False):
        """
        This function returns the directories with film_directory_flag
        :param dataframe: It represents the dataframe input for this function
        :param drop_dup: Drop duplicated values by default
        :return: ANIME_DIRECTORIES
        """
        if drop_dup:
            dataframe_episodes_directories = dataframe.groupby(['name']).get_group(current_anime).drop_duplicates()
        else:
            dataframe_episodes_directories = dataframe.groupby(['name']).get_group(current_anime)
        return dataframe_episodes_directories[dataframe_episodes_directories.fflag == FileFlags.ANIME_DIRECTORY_FLAG]

    '''

        CREATE SECTION OF PANDAS EXTENSION

    '''

    def create_animes_directory(self, dataframe, root_basename):
        """
        This function creates a default ANIME folder to later move the films
        :param dataframe: It represents the dataframe input for this function
        :param root_basename: It represents the basename of the TreeRoot structure
        :return: ANIME_FOLDER
        """
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe,
                                                        name='Animes',
                                                        season='N/A',
                                                        episode='N/A',
                                                        fflag=FileFlags.LIBRARY_FLAG,
                                                        basename='Animes',
                                                        parent=root_basename,
                                                        year='N/A', genre='N/A',
                                                        n_season='N/A',
                                                        e_season='N/A')
        return dataframe

    def create_main_anime_directory(self, dataframe, current_anime):
        """
        This function creates a default anime directory to later move the films
        :param dataframe: It represents the dataframe input for this function
        :param current_anime: It represents the basename of the current anime your mapping
        :return: MOVIE_FOLDER
        """
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe,
                                                        name=current_anime,
                                                        season='N/A',
                                                        episode='N/A',
                                                        fflag=FFLAGS.MAIN_SHOW_DIRECTORY_FLAG,
                                                        basename=current_anime,
                                                        parent='Animes',
                                                        year='N/A',
                                                        genre='N/A',
                                                        n_season='N/A',
                                                        e_season='N/A')
        return dataframe

    def create_default_anime_tree_directory(self, dataframe, current_anime,
                                            debug=False):
        """
        This function creates a default structure of Anime Library
        :param dataframe: It represents the dataframe input for this function
        :param current_anime: It represents the current serie you're mapping
        :return: ANIME LIBRARY
        """
        main_show_directory = dataframe[dataframe['basename'] == current_anime]
        if main_show_directory.empty:
            dataframe = self.create_main_anime_directory(dataframe=dataframe, current_anime=current_anime)
        else:
            main_index = main_show_directory.index.tolist()[0]
            dataframe = self.pandas_utils.update_parent_dataframe_row(dataframe=dataframe, index=int(main_index),
                parent='Animes')

        dataframe_episodes = self.get_anime(dataframe=dataframe, current_anime=current_anime)
        for episode_index in dataframe_episodes.index.tolist():
            name = dataframe.iloc[int(episode_index)]['name']
            episode = dataframe.iloc[int(episode_index)]['episode']
            basename = dataframe.iloc[int(episode_index)]['basename']
            parent = dataframe.iloc[int(episode_index)]['parent']
            season = dataframe.iloc[int(episode_index)]['season']

            dataframe_episodes_directories = self.get_anime_directories(
                dataframe=dataframe,
                current_anime=current_anime)
            if dataframe_episodes_directories[dataframe_episodes_directories.basename == basename[:-4]].empty:
                dataframe = self.pandas_utils.add_dataframe_row(
                    dataframe=dataframe, name=name, season=season,
                    episode=episode, fflag=FFLAGS.SHOW_DIRECTORY_FLAG,
                    basename=basename[:-4], parent=parent, year='N/A',
                    genre='N/A', n_season='N/A', e_season='N/A')

                dataframe = self.pandas_utils.update_parent_dataframe_row(
                    dataframe=dataframe, index=int(episode_index),
                    parent=basename[:-4])
                if debug:
                    print('CREATED: ' + str(basename[:-4]))

        dataframe_episodes_directories = self.get_anime_directories(
            dataframe=dataframe, current_anime=current_anime)
        for episode_directory_index in dataframe_episodes_directories.index.tolist():
            parent = dataframe.iloc[int(episode_directory_index)]['parent']
            if parent not in 'Animes':
                dataframe = self.pandas_utils.update_parent_dataframe_row(
                    dataframe=dataframe,
                    index=int(episode_directory_index),
                    parent=current_anime)
        return dataframe
