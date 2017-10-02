from filemapper.datastructure.FileFlags import FileFlags as fflags

def eval_wrapped_key(value, wrap_type):
    '''
    This function peform auxiliary help to the build name functions validating the content of the string
    :param value: It represents the key you'regex testing
    :param wrap_type: It represents the type of wrapping the string it's going to get, numbers 0 to 2, being
                    0 for [value], 1 for (value), 2 for -(value) 3 value
    :return: modified value
    '''
    if value is None:
        return ''
    else:
        if wrap_type is -1:
            if value is '':
                return ''
            return(' ' + value)
        elif wrap_type is 0:
            if value is '':
                return value
            return (' [' + value + ']')
        elif wrap_type is 1:
            if value is '':
                return value
            return (' (' + value + ')')
        elif wrap_type is 2:
            if value is '':
                return value
            return (' - (' + value + ')')
        elif wrap_type is 3:
            if value is '':
                return value
            return ('.' + value)
        else:
            return value

EMPTY_WRAP = -1
BRACKET_WRAP = 0
PARENTHESIS_WRAP = 1
DASH_PARENTHESIS_WRAP = 2
EXTENSION_WRAP = 3
NONE_WRAP = 4


class FilmExtension():
    def __init__(self):
        self.name = 'FilmExtension'
        self.supported_fflags = [fflags.FILM_DIRECTORY_FLAG, fflags.FILM_FLAG]
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
            FILM_NAME = ('{name}{year}{film_tag}{quality}{extension}').format(
                name=eval_wrapped_key(value=name, wrap_type=NONE_WRAP),
                year=eval_wrapped_key(value=year, wrap_type=PARENTHESIS_WRAP),
                film_tag=eval_wrapped_key(value=film_tag, wrap_type=EMPTY_WRAP),
                quality=eval_wrapped_key(value=quality, wrap_type=BRACKET_WRAP),
                extension=eval_wrapped_key(value=extension, wrap_type=EXTENSION_WRAP)
            )

            if debug:
                print ('{engine}: {name}').format(engine=self.name, name=FILM_NAME)

            return FILM_NAME

        except Exception as e:
            print e

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
            print 'Entra en film subtitle name'
            SUBTITLE_NAME = ('{name}{year}{subtitle}{language}{extension}').format(
                name=eval_wrapped_key(value=name, wrap_type=NONE_WRAP),
                year=eval_wrapped_key(value=year, wrap_type=PARENTHESIS_WRAP),
                subtitle=eval_wrapped_key(value=subtitle, wrap_type=PARENTHESIS_WRAP),
                language=eval_wrapped_key(value=language, wrap_type=DASH_PARENTHESIS_WRAP),
                extension=eval_wrapped_key(value=extension, wrap_type=EXTENSION_WRAP)
            )

            if debug:
                print ('{engine}: {name}').format(engine=self.name, name=SUBTITLE_NAME)

            return SUBTITLE_NAME

        except Exception as e:
            print e