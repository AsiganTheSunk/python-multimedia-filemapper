from filemapper.datastructure.FileFlags import FileFlags as fflags
import imdb

class IMDbExtension():
    def __init__(self):
        self.name = 'IMDbExtension'
        self.imdb = imdb.IMDb()
        self.supported_fflags = [fflags.FILM_FLAG, fflags.SHOW_FLAG]
        self.support_formats = []

        return

    def retrieve_film_genre(self, name, index=0, debug=False):
        '''
        This function retrieves the genre of a the film
        :param name:  It represents the name of the show you're searching for
        :param index:  It represents the index of the genres, default value it's 0, you get the main genre
        :param debug: It represents the debug status of the function, default it's False
        :return: GENRE
        '''
        try:
            genres = self.imdb.search_movie(name)[0].movieID
            genre = self.imdb.get_movie(unicode(genres))['genre'][index]
        except Exception as e:
            # raise error that would be corrected in ReEngine turning exception into blank field
            genre = 'N/O'
            return genre
        else:
            if debug:
                print('{extension_engine}: {stream} :: {value}').format(extension_engine=self.name,
                                                                        stream=name,
                                                                        value=genre)
            return genre