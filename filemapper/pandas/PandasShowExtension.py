from filemapper.datastructure.FileFlags import FileFlags as FFLAGS
from filemapper.pandas.PandasUtils import PandasUtils
from filemapper.sbuilder.StringShowExtension import StringShowExtension
from filemapper.metadata.tvdb.TVDbShowExtension import TVDbShowExtension


class PandasShowExtension():
    def __init__(self):
        self.pandas_utils = PandasUtils()
        self.string_builder = StringShowExtension()
        self.tvdb_extension = TVDbShowExtension()
        return

    def create_default_library(self, dataframe, tree_root):
        '''
        This function creates a default library structure in pandas for films
        :param dataframe: It represents the dataframe input for this function
        :param tree_root: basename of the tree_root structure
        :return: DATAFRAME
        '''
        unique_series = self.get_show_names(dataframe=dataframe)
        dataframe = self.create_shows_directory(dataframe=dataframe, root=tree_root)
        for current_serie in unique_series:
            dataframe = self.create_default_show_tree_directory(dataframe=dataframe, current_show=current_serie)
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
        unique_series = dataframe.name[dataframe['fflag'] == FFLAGS.SHOW_FLAG].unique()
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
            dataframe_episodes = dataframe.groupby(['name']).get_group(current_show).drop_duplicates()
        else:
            dataframe_episodes = dataframe.groupby(['name']).get_group(current_show)
        return dataframe_episodes[dataframe_episodes.fflag == FFLAGS.SHOW_FLAG]

    def get_episode_directories(self, dataframe, current_show, drop_dup=False):
        '''
        This function returns the files with show_directory_flag
        :param dataframe: It represents the dataframe input for this function
        :param current_show: It represents the basename of the current show your mapping
        :param drop_dup: Drop duplicated values by default
        :return:
        '''
        if drop_dup:
            dataframe_episodes = dataframe.groupby(['name']).get_group(current_show).drop_duplicates()
        else:
            dataframe_episodes = dataframe.groupby(['name']).get_group(current_show)
        return dataframe_episodes[dataframe_episodes.fflag == FFLAGS.SHOW_DIRECTORY_FLAG]

    def get_seasons(self, dataframe, current_show, drop_dup=False):
        '''
        This function returns the files with season_flag
        :param dataframe: It represents the dataframe input for this function
        :param current_show: It represents the basename of the current show your mapping
        :param drop_dup: Drop duplicated values by default
        :return:
        '''
        if drop_dup:
            dataframe_episodes = dataframe.groupby(['name']).get_group(current_show).drop_duplicates()
        else:
            dataframe_episodes = dataframe.groupby(['name']).get_group(current_show)
        return dataframe_episodes[dataframe_episodes.fflag == FFLAGS.SEASON_DIRECTORY_FLAG]

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
        new_season_directory = self.string_builder.build_season_name(name=current_show, season=season)
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe, name=current_show, season=season,
                                                        episode='N/A', fflag=FFLAGS.SEASON_DIRECTORY_FLAG,
                                                        basename=new_season_directory, parent=parent, year='N/A',
                                                        genre='N/A', n_season='N/A', e_season='N/A')
        return dataframe

    def create_shows_directory(self, dataframe, root):
        '''
        This function creates a default SHOWS folder to later move the films
        :param dataframe: It represents the dataframe input for this function
        :param root: It represents the basename of the TreeRoot structure
        :return: SHOWS_FOLDER
        '''
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe, name='Shows', season='N/A', episode='N/A',
                                                        fflag=FFLAGS.LIBRARY_FLAG, basename='Shows', parent=root,
                                                        year='N/A', genre='N/A', n_season='N/A', e_season='N/A')
        return dataframe

    def create_main_show_directory(self, dataframe, current_show):
        '''
        This function creates a default anime directory to later move the films
        :param dataframe: It represents the dataframe input for this function
        :param current_show: It represents the basename of the current anime your mapping
        :return: MOVIE_FOLDER
        '''
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe, name=current_show, season='N/A',
                                                        episode='N/A', fflag=FFLAGS.MAIN_SHOW_DIRECTORY_FLAG,
                                                        basename=current_show, parent='Shows', year='N/A', genre='N/A',
                                                        n_season='N/A', e_season='N/A')
        return dataframe

    def create_default_show_tree_directory(self, dataframe, current_show):
        '''
        This function creates a default structure of Shows Library
        :param dataframe: It represents the dataframe input for this function
        :param current_show: It represents the current serie you're mapping
        :return: SHOWS_LIBRARY
        '''
        main_show_directory = None
        main_show_directory = dataframe[dataframe['basename'] == current_show]
        if main_show_directory.empty:
            dataframe = self.create_main_show_directory(dataframe=dataframe, current_show=current_show)
        else:
            #TODO CHANGED BECAUSE OF TYPE ERROR INT64
            #real_index = main_show_directory.index.tolist()[0]
            dataframe = self.pandas_utils.update_parent_dataframe_row(dataframe=dataframe, index=int(main_show_directory.index), parent='Shows')

        # metadata season dataframe from current serie
        dataframe_seasons = self.get_seasons(dataframe=dataframe, current_show=current_show)
        # metadata episode file dataframe from current serie
        dataframe_episodes = self.get_episode(dataframe=dataframe, current_show=current_show)
        # metadata episode directory dataframe from current serie
        dataframe_episodes_directories = self.get_episode_directories(dataframe=dataframe, current_show=current_show)

        # reset index to simply iterate over the rows, extracting the values, to create the directory tree
        dataframe_temp = dataframe_episodes.reindex()

        for index in range(0, len(dataframe_temp.index), 1):
            name = dataframe_temp.iloc[int(index)]['name']
            season = dataframe_temp.iloc[int(index)]['season']
            episode = dataframe_temp.iloc[int(index)]['episode']
            basename = dataframe_temp.iloc[int(index)]['basename']
            parent = dataframe_temp.iloc[int(index)]['parent']

            real_index = dataframe_seasons.index[dataframe_seasons.season == season]
            dataframe_season = dataframe_seasons[dataframe_seasons.season == season]
            if dataframe_season.empty:

                dataframe = self.create_season_directory(dataframe, current_show=current_show, season=season, parent=current_show)
            else:
                real_index = real_index.tolist()[0]
                dataframe = self.pandas_utils.update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent=current_show)

            dataframe_directory = dataframe_episodes_directories[dataframe_episodes_directories.basename == basename[:-4]]
            real_index = dataframe_episodes.index[dataframe_episodes.basename == basename].tolist()[0]
            if dataframe_directory.empty:
                print('CREATED: ' + str(basename[:-4]))
                dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe, name=name, season=season,
                                                                episode=episode, fflag=FFLAGS.SHOW_DIRECTORY_FLAG,
                                                                basename=basename[:-4], parent=parent, year='N/A',
                                                                genre='N/A', n_season='N/A', e_season='N/A')
                dataframe = self.pandas_utils.update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent=basename[:-4])

        dataframe_temp = dataframe_episodes_directories.reindex()
        for index in range(0, len(dataframe_temp.index), 1):
            name = dataframe_temp.iloc[int(index)]['name']
            season = dataframe_temp.iloc[int(index)]['season']
            basename = dataframe_temp.iloc[int(index)]['basename']
            parent = dataframe_temp.iloc[int(index)]['parent']
            new_parent = self.string_builder.build_season_name(name=name, season=season)

            real_index = dataframe_episodes_directories.index[dataframe_episodes_directories.basename == basename]
            if parent not in new_parent:
                real_index = real_index.tolist()[0]
                dataframe = self.pandas_utils.update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent=new_parent)
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
                    print('Directory: {status} | Season {season} - Found ({current}/{total} Episodes)'.format(season=i, current=current_episodes, total=total_episodes, status=season_dir))
                    dataframe_temp = dataframe_episodes_per_season.reindex()
                    for index in range(0,len(dataframe_temp.index),1):
                        basename = dataframe_temp.iloc[int(index)]['basename']
                        dataframe_directory = dataframe_episode_directories[dataframe_episode_directories.basename == basename[:-4]]
                        current_dir = 'NO '
                        if not dataframe_directory.empty:
                            current_dir = 'YES'
                        print('--: Directory: {status} | {basename}'.format(basename=basename,status=current_dir))
                print('------' * 20)

        except:
            return
