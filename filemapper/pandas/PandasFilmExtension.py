from filemapper.datastructure.FileFlags import FileFlags as FFLAGS
from filemapper.pandas.PandasUtils import PandasUtils

class PandasFilmExtension():
    def __init__(self):
        self.pandas_utils = PandasUtils()
        return

    def create_default_library(self, dataframe, tree_root):
        '''
        This function creates a default library structure in pandas for films
        :param dataframe: It represents the dataframe input for this function
        :param tree_root: basename of the tree_root structure
        :return: DATAFRAME
        '''
        dataframe = self.create_film_directory(dataframe=dataframe, root=tree_root)
        dataframe = self.create_default_movies_tree_directory(dataframe)
        return dataframe

    '''

        GET SECTION OF PANDAS EXTENSION

    '''

    def get_film_names(self, dataframe):
        '''
        This function returns the unique values for film names
        :param dataframe: It represents the dataframe input for this function
        :return: UNIQUE_FILMS
        '''
        unique_movies = dataframe.name[dataframe['fflag'] == FFLAGS.FILM_FLAG].unique()
        return unique_movies

    def get_film(self, dataframe):
        '''
        This function returns the files with film_flag
        :param dataframe: It represents the dataframe input for this function
        :return: FILE_FILMS
        '''
        return dataframe[dataframe.fflag == FFLAGS.FILM_FLAG]

    def get_film_directories(self, dataframe):
        '''
        This function returns the directories with film_directory_flag
        :param dataframe: It represents the dataframe input for this function
        :return: FILE_DIRECTORIES
        '''
        return dataframe[dataframe.fflag == FFLAGS.FILM_DIRECTORY_FLAG]

    '''

        CREATE SECTION OF PANDAS EXTENSION

    '''

    def create_film_directory(self, dataframe, root):
        '''
        This function creates a default Movies folder to later move the films
        :param dataframe: It represents the dataframe input for this function
        :param root: It represents the basename of the TreeRoot structure
        :return: MOVIES_FOLDER
        '''
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe, name='Movies', season='N/A', episode='N/A',
                                                        fflag=FFLAGS.LIBRARY_FLAG, basename='Movies', parent=root,
                                                        year='N/A', genre='N/A', n_season='N/A', e_season='N/A')
        return dataframe

    def create_default_movies_tree_directory(self, dataframe):
        '''
        This function creates a default structure of Movies Library
        :param dataframe: It represents the dataframe input for this function
        :return: MOVIES_LIBRARY
        '''
        dataframe_film = self.get_film(dataframe)
        dataframe_film_directories = self.get_film_directories(dataframe)

        print dataframe_film_directories
        dataframe_film_temp = dataframe_film.reindex()

        for index in range(0, len(dataframe_film_temp.index), 1):
            name = dataframe_film_temp.iloc[int(index)]['name']
            basename = dataframe_film_temp.iloc[int(index)]['basename']
            parent = dataframe_film_temp.iloc[int(index)]['parent']
            dataframe_directory = dataframe_film_directories[dataframe_film_directories.basename == basename[:-4]]

            real_index = dataframe_film.index[dataframe_film.basename == basename]

            print 'real index in films: ',
            if dataframe_directory.empty:
                # TODO CHANGED BECAUSE OF TYPE ERROR INT64
                # real_index = real_index.tolist()[0]
                dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe, name=name,
                                                                season='N/A', episode='N/A',
                                                                fflag=FFLAGS.FILM_DIRECTORY_FLAG,
                                                                basename=basename[:-4], parent=parent,
                                                                year='N/A',genre='N/A', n_season='N/A', e_season='N/A')
                dataframe = self.pandas_utils.update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent=basename[:-4])

        dataframe_dfilm_temp = dataframe_film_directories.reindex()
        for index in range(0, len(dataframe_dfilm_temp.index), 1):
            name = dataframe_dfilm_temp.iloc[int(index)]['name']
            season = dataframe_dfilm_temp.iloc[int(index)]['season']
            basename = dataframe_dfilm_temp.iloc[int(index)]['basename']
            parent = dataframe_dfilm_temp.iloc[int(index)]['parent']
            real_index = dataframe.index[dataframe.basename == basename]

            if parent not in 'Movies':
                real_index = real_index.tolist()[0]
                dataframe = self.pandas_utils.update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent='Movies')

        return dataframe
