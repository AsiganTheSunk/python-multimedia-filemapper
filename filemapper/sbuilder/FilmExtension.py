from StringBuilder import eval_wrapped_key, EMPTY_WRAP, BRACKET_WRAP, DASH_PARENTHESIS_WRAP, PARENTHESIS_WRAP, EXTENSION_WRAP
from filemapper.datastructure.FileFlags import FileFlags as fflags

class FilmExtension():
    def __init__(self):
        self.name = 'FilmExtension'
        self.supported_name_fflags = [fflags.FILM_DIRECTORY_FLAG, fflags.FILM_FLAG]
        self.supported_season_fflags = []
        self.supported_subtitle_fflags = [fflags.SUBTITLE_DIRECTORY_FILM_FLAG, fflags.SUBTITLE_FILM_FLAG]
        return

    '''
        FilmExtension:
            This section of the code contains the following functions

            build_film_name:
            build_film_subtitle_name:
    '''

    def build_name(self, name, year, season, episode, ename, quality, extension, film_tag, debug=False):
        '''
        This function builds a film name for file or directory
        :param name: It represents the title of the film you'regex rebuilding to proper match the standard
        :param year: It represents the year of the film you'regex rebuilding to proper math the standard
        :param film_tag: It represents film tags common in film file or directory to proper match the standard
        :param quality: It represents the resolution of the show you'regex rebuilding to proper match the standard
        :param extension: It represents the extension of the file containing the film
        :param debug: It represents the debug status of the function, default it's False
        :return: FILM_NAME
        '''
        try:
            FILM_NAME = ('{name} {year} {film_tag} {quality}{extension}').format(
                name=eval_wrapped_key(value=name, wrap_type=EMPTY_WRAP),
                year=eval_wrapped_key(value=year, wrap_type=PARENTHESIS_WRAP),
                film_tag=eval_wrapped_key(value=film_tag, wrap_type=EMPTY_WRAP),
                quality=eval_wrapped_key(value=quality, wrap_type=BRACKET_WRAP),
                extension=eval_wrapped_key(value=extension, wrap_type=EXTENSION_WRAP)
            )

            if debug:
                print ('{engine}: {name}').format(engine=self.name, name=FILM_NAME)

            return FILM_NAME

        except:
            raise(Exception)

    def build_subtitle_name(self, name, year, season, episode, subtitle, language, extension, debug=False):
        '''
        This function builds a film subs name for file or directory
        :param name: It represents the title of the film you'regex rebuilding to proper match the standard
        :param year: It represents the year of the film you'regex rebuilding to proper match the standard
        :param subtitle: It represents the subs tag
        :param language: It represents the language of the show
        :param extension: It represents the extension of the file containing the show
        :param debug: It represents the debug status of the function, default it's False
        :return: SUBTITLE_NAME
        '''
        try:
            SUBTITLE_NAME = ('{name} {year} {subs} {language}{extension}').format(
                name=eval_wrapped_key(value=name, wrap_type=EMPTY_WRAP),
                year=eval_wrapped_key(value=year, wrap_type=PARENTHESIS_WRAP),
                subtitle=eval_wrapped_key(value=subtitle, wrap_type=PARENTHESIS_WRAP),
                language=eval_wrapped_key(value=language, wrap_type=DASH_PARENTHESIS_WRAP),
                extension=eval_wrapped_key(value=extension, wrap_type=EXTENSION_WRAP)
            )

            if debug:
                print ('{engine}: {name}').format(engine=self.name, name=SUBTITLE_NAME)

            return SUBTITLE_NAME

        except:
            raise(Exception)