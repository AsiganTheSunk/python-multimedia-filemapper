from filemapper.pandas.pandasutils import PandasUtils
from filemapper.utils.fileflags import FileFlags as FFLAGS


class PandasFilmExtension():
    def __init__(self):
        self.pandas_utils = PandasUtils()
        return

    def create_default_library(self, dataframe, root_basename):
        '''
        This function creates a default library structure in pandas for films
        :param dataframe: It represents the dataframe input for this function
        :param root_basename: basename of the tree_root structure
        :return: DATAFRAME
        '''
        dataframe = self.create_film_directory(dataframe=dataframe, root_basename=root_basename)
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

    def create_film_directory(self, dataframe, root_basename):
        '''
        This function creates a default Movies folder to later move the films
        :param dataframe: It represents the dataframe input for this function
        :param root_basename: It represents the basename of the TreeRoot structure
        :return: MOVIES_FOLDER
        '''
        dataframe = self.pandas_utils.add_dataframe_row(dataframe=dataframe,
                                                        name='Movies',
                                                        season='N/A',
                                                        episode='N/A',
                                                        fflag=FFLAGS.LIBRARY_FLAG,
                                                        basename='Movies',
                                                        parent=root_basename,
                                                        year='N/A', genre='N/A',
                                                        n_season='N/A',
                                                        e_season='N/A')
        return dataframe

    def create_default_movies_tree_directory(self, dataframe):
        '''
        This function creates a default structure of Movies Library
        :param dataframe: It represents the dataframe input for this function
        :return: MOVIES_LIBRARY
        '''

        dataframe_film = self.get_film(dataframe)
        for film_index in dataframe_film.index.tolist():
            name = dataframe.iloc[int(film_index)]['name']
            year = dataframe.iloc[int(film_index)]['year']
            basename = dataframe.iloc[int(film_index)]['basename']
            parent = dataframe.iloc[int(film_index)]['parent']

            dataframe_film_directories = self.get_film_directories(dataframe)
            if dataframe_film_directories[
                        dataframe_film_directories.basename == basename[:-4]].empty:
                dataframe = self.pandas_utils.add_dataframe_row(
                    dataframe=dataframe, name=name,
                    season='N/A', episode='N/A',
                    fflag=FFLAGS.FILM_DIRECTORY_FLAG,
                    basename=basename[:-4], parent=parent,
                    year=year, genre='N/A', n_season='N/A', e_season='N/A')

                dataframe = self.pandas_utils.update_parent_dataframe_row(
                    dataframe=dataframe, index=int(film_index),
                    parent=basename[:-4])

        dataframe_film_directories = self.get_film_directories(dataframe=dataframe)

        for directory_film_index in dataframe_film_directories.index.tolist():
            parent = dataframe.iloc[int(directory_film_index)]['parent']
            if parent is not 'Movies':
                dataframe = self.pandas_utils.update_parent_dataframe_row(
                    dataframe=dataframe,
                    index=int(directory_film_index),
                    parent='Movies')

        return dataframe
