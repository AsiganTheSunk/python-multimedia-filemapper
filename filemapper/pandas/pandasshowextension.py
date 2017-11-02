from filemapper.metadata.tvdb.tvdbshowextension import TVDbShowExtension
from filemapper.pandas.pandasutils import PandasUtils
from filemapper.sbuilder.stringshowextension import StringShowExtension
from filemapper.utils.fileflags import FileFlags as fflags


class PandasShowExtension():
    def __init__(self):
        self.pandas_utils = PandasUtils()
        self.string_builder = StringShowExtension()
        self.tvdb_extension = TVDbShowExtension()
        return

    def create_default_library(self, dataframe, root_basename):
        '''
        This function creates a default library structure in pandas for films
        :param dataframe: It represents the dataframe input for this function
        :param root_basename: basename of the tree_root structure
        :return: DATAFRAME
        '''
        unique_series = self.get_show_names(dataframe=dataframe)
        dataframe = self.create_shows_directory(dataframe=dataframe, root_basename=root_basename)
        for current_show in unique_series:
            dataframe = self.create_default_show_tree_directory(dataframe=dataframe, current_show=current_show)
        return dataframe

    '''

        GET SECTION OF PANDAS EXTENSION

    '''

    def get_show_names(self, dataframe):
        '''
        This function returns the unique values for film names
        :param dataframe: It represents the dataframe input for this function
        :return: UNIQUE_SHOWS
        '''
        unique_series = dataframe.name[dataframe['fflag'] == fflags.SHOW_FLAG].unique()
        return unique_series

    def get_episode(self, dataframe, current_show, drop_dup=False):
        '''
        This function returns the files with show_flag
        :param dataframe: It represents the dataframe input for this function
        :param current_show: It represents the basename of the current show your mapping
        :param drop_dup: Drop duplicated values by default
        :return:
        '''
        if drop_dup:
            dataframe_episodes = dataframe.groupby(['name']).get_group(
                current_show).drop_duplicates()
        else:
            dataframe_episodes = dataframe.groupby(['name']).get_group(
                current_show)
        return dataframe_episodes[dataframe_episodes.fflag == fflags.SHOW_FLAG]

    def get_episode_directories(self, dataframe, current_show, drop_dup=False):
        '''
        This function returns the files with show_directory_flag
        :param dataframe: It represents the dataframe input for this function
        :param current_show: It represents the basename of the current show your mapping
        :param drop_dup: Drop duplicated values by default
        :return:
        '''
        if drop_dup:
            dataframe_episodes = dataframe.groupby(['name']).get_group(
                current_show).drop_duplicates()
        else:
            dataframe_episodes = dataframe.groupby(['name']).get_group(
                current_show)
        return dataframe_episodes[
            dataframe_episodes.fflag == fflags.SHOW_DIRECTORY_FLAG]

    def get_seasons(self, dataframe, current_show, drop_dup=False):
        '''
        This function returns the files with season_flag
        :param dataframe: It represents the dataframe input for this function
        :param current_show: It represents the basename of the current show your mapping
        :param drop_dup: Drop duplicated values by default
        :return:
        '''
        if drop_dup:
            dataframe_episodes = dataframe.groupby(['name']).get_group(
                current_show).drop_duplicates()
        else:
            dataframe_episodes = dataframe.groupby(['name']).get_group(
                current_show)
        return dataframe_episodes[
            dataframe_episodes.fflag == fflags.SEASON_DIRECTORY_FLAG]

    '''
    
        CREATE SECTION OF PANDAS EXTENSION
        
    '''

    def create_season_directory(self, dataframe, current_show, season, parent):
        '''
        This function creates a season directory
        :param dataframe: It represents the dataframe input for this function
        :param current_show: It represents the current show your mapping
        :param season: It represents the current season you're mapping
        :param parent: It represens the parent of the show you're mapping so you can relink later
        :return: SEASON_DIRECTORY
        '''
        new_season_directory = self.string_builder.build_season_name(
            name=current_show, season=season)
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe,
                                                        name=current_show,
                                                        season=season,
                                                        episode='N/A',
                                                        fflag=fflags.SEASON_DIRECTORY_FLAG,
                                                        basename=new_season_directory,
                                                        parent=parent,
                                                        year='N/A',
                                                        genre='N/A',
                                                        n_season='N/A',
                                                        e_season='N/A')
        return dataframe

    def create_shows_directory(self, dataframe, root_basename):
        '''
        This function creates a default SHOWS folder to later move the films
        :param dataframe: It represents the dataframe input for this function
        :param root_basename: It represents the basename of the TreeRoot structure
        :return: SHOWS_FOLDER
        '''
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe,
                                                        name='Shows',
                                                        season='N/A',
                                                        episode='N/A',
                                                        fflag=fflags.LIBRARY_FLAG,
                                                        basename='Shows',
                                                        parent=root_basename,
                                                        year='N/A', genre='N/A',
                                                        n_season='N/A',
                                                        e_season='N/A')
        return dataframe

    def create_main_show_directory(self, dataframe, current_show):
        '''
        This function creates a default anime directory to later move the films
        :param dataframe: It represents the dataframe input for this function
        :param current_show: It represents the basename of the current anime your mapping
        :return: MOVIE_FOLDER
        '''
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe,
                                                        name=current_show,
                                                        season='N/A',
                                                        episode='N/A',
                                                        fflag=fflags.MAIN_SHOW_DIRECTORY_FLAG,
                                                        basename=current_show,
                                                        parent='Shows',
                                                        year='N/A', genre='N/A',
                                                        n_season='N/A',
                                                        e_season='N/A')
        return dataframe

    def create_default_show_tree_directory(self, dataframe, current_show,
                                           debug=False):
        '''
        This function creates a default structure of Shows Library
        :param dataframe: It represents the dataframe input for this function
        :param current_show: It represents the current serie you're mapping
        :return: SHOWS_LIBRARY
        '''

        # If the main show directory does not exist, it's created
        main_show_directory = dataframe[dataframe['basename'] == current_show]
        if main_show_directory.empty:
            dataframe = self.create_main_show_directory(dataframe=dataframe,
                                                        current_show=current_show)
        else:
            main_index = main_show_directory.index.tolist()[0]
            dataframe = self.pandas_utils.update_parent_dataframe_row(
                dataframe=dataframe, index=int(main_index),
                parent='Shows')

        # Retrieving the episodes files of the current show
        dataframe_episodes = self.get_episode(dataframe=dataframe,
                                              current_show=current_show)
        for episode_index in dataframe_episodes.index.tolist():
            name = dataframe.iloc[int(episode_index)]['name']
            season = dataframe.iloc[int(episode_index)]['season']
            episode = dataframe.iloc[int(episode_index)]['episode']
            basename = dataframe.iloc[int(episode_index)]['basename']
            parent = dataframe.iloc[int(episode_index)]['parent']
            dataframe_seasons = self.get_seasons(dataframe=dataframe,
                                                 current_show=current_show)

            # We check if all the season directories are created if not
            if dataframe_seasons[
                        dataframe_seasons.season == str(int(season))].empty:
                dataframe = self.create_season_directory(dataframe,
                                                         current_show=current_show,
                                                         season=season,
                                                         parent=current_show)
                if debug:
                    print 'created ', season, current_show
            else:
                season_index = dataframe_seasons.index[dataframe_seasons.season == str(int(season))].tolist()[0]
                dataframe = self.pandas_utils.update_parent_dataframe_row(
                    dataframe=dataframe, index=season_index,
                    parent=current_show)
                if debug:
                    print 'updated ', season_index, current_show

            # Now we check if every episode it's in his own directory
            dataframe_episodes_directories = self.get_episode_directories(
                dataframe=dataframe,
                current_show=current_show)
            if dataframe_episodes_directories[
                        dataframe_episodes_directories.basename == basename[:-4]].empty:
                dataframe = self.pandas_utils.add_dataframe_row(
                    dataframe=dataframe, name=name, season=season,
                    episode=episode, fflag=fflags.SHOW_DIRECTORY_FLAG,
                    basename=basename[:-4], parent=parent, year='N/A',
                    genre='N/A', n_season='N/A', e_season='N/A')
                dataframe = self.pandas_utils.update_parent_dataframe_row(
                    dataframe=dataframe, index=int(episode_index),
                    parent=basename[:-4])

        # Now for every episode directory we update the table to point out to the season directory
        dataframe_episodes_directories = self.get_episode_directories(
            dataframe=dataframe, current_show=current_show)
        for episode_directory_index in dataframe_episodes_directories.index.tolist():
            name = dataframe.iloc[int(episode_directory_index)]['name']
            season = dataframe.iloc[int(episode_directory_index)]['season']
            basename = dataframe.iloc[int(episode_directory_index)]['basename']
            parent = dataframe.iloc[int(episode_directory_index)]['parent']
            new_parent = self.string_builder.build_season_name(name=name,
                                                               season=season)

            episode_directory_index = \
                dataframe_episodes_directories.index[dataframe_episodes_directories.basename == basename].tolist()[0]
            if parent is not new_parent:
                dataframe = self.pandas_utils.update_parent_dataframe_row(
                    dataframe=dataframe,
                    index=int(episode_directory_index),
                    parent=new_parent)

        return dataframe

    def get_show_stats(self, dataframe, current_show):
        '''

        :param dataframe:
        :param current_show:
        :return:
        '''
        dataframe_episode = self.get_episode(dataframe=dataframe, current_show=current_show)
        dataframe_episode_directories = self.get_episode_directories(dataframe=dataframe, current_show=current_show)
        dataframe_seasons = self.get_seasons(dataframe=dataframe, current_show=current_show)
        main_show_directory = dataframe[dataframe['basename'] == current_show]
        current_status = 'NO'
        if not main_show_directory.empty:
            current_status = 'YES'
        print('------' * 20)
        print('-- Directory: {status} | SHOW NAME: {show_name} '.format(show_name=current_show, status=current_status))
        print('------' * 20)

        try:
            total_seasons = self.tvdb_extension.get_number_of_seasons(name=current_show)
            for i in range(0, total_seasons, 1):
                try:
                    total_episodes = self.tvdb_extension.get_number_of_season_episodes(name=current_show, season=i)
                    dataframe_episodes_per_season = dataframe_episode[dataframe_episode.season == str(i)]
                    current_episodes = len(dataframe_episodes_per_season)
                except:
                    continue
                else:

                    dataframe_season = dataframe_seasons[dataframe_seasons.season == str(i)]
                    season_dir = 'NO '
                    if not dataframe_season.empty:
                        season_dir = 'YES'
                    print(
                    'Directory: {status} | Season {season} - Found ({current}/{total} Episodes)'.format(
                        season=i,
                        current=current_episodes,
                        total=total_episodes,
                        status=season_dir))
                    dataframe_temp = dataframe_episodes_per_season.reindex()
                    for index in range(0, len(dataframe_temp.index), 1):
                        basename = dataframe_temp.iloc[int(index)]['basename']
                        dataframe_directory = \
                            dataframe_episode_directories[dataframe_episode_directories.basename == basename[:-4]]
                        current_dir = 'NO '
                        if not dataframe_directory.empty:
                            current_dir = 'YES'
                        print('--: Directory: {status} | {basename}'.format(basename=basename, status=current_dir))
                print('------' * 20)

        except:
            return
