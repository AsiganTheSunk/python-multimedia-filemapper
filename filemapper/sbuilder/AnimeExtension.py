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


class AnimeExtension():
    def __init__(self):
        self.name = 'AnimeExtension'
        self.supported_fflags = [fflags.ANIME_DIRECTORY_FLAG, fflags.ANIME_FLAG]
        self.supported_season_fflags = []
        self.supported_subtitle_fflags = [fflags.SUBTITLE_DIRECTORY_ANIME_FLAG, fflags.SUBTITLE_ANIME_FLAG]
        return

    '''
        AnimeExtension:
            This section of the code contains the following functions

            build_anime_name:
            build_anime_subtitle_name:
    '''

    def build_name(self, name, year, season, episode, ename, quality, extension, film_tag, debug=False):
        '''
        This function builds a anime name for file or directory
        :param name: It represents the title of the anime you'regex rebuilding to proper match the standard
        :param episode: It represents the episode of the anime you'regex rebuilding to proper match the standard
        :param ename: It represents the name of the episode of the anime you'regex rebuilding to proper match the standard
        :param quality: It represents the resolution of the anime you'regex rebuilding to proper match the standard
        :param extension: It represents the extension of the file containing the anime
        :param debug: It represents the debug status of the function, default it's False
        :return:
        '''
        try:
            ANIME_NAME = ('{name}{episode}{ename}{quality}{extension}').format(
                name=eval_wrapped_key(value=name, wrap_type=NONE_WRAP),
                episode=eval_wrapped_key(value=('E' + episode), wrap_type=EMPTY_WRAP),
                ename=eval_wrapped_key(value=ename, wrap_type=EMPTY_WRAP),
                quality=eval_wrapped_key(value=quality, wrap_type=BRACKET_WRAP),
                extension=eval_wrapped_key(value=extension, wrap_type=EXTENSION_WRAP)
            )

            if debug:
                print ('{engine}: {name}').format(engine=self.name, name=ANIME_NAME)

            return ANIME_NAME
        except Exception as e:
            print e



    def build_subtitle_name(self, name, year, season, episode, subtitle, language, extension, debug=False):
        '''
        This function builds a subs anime name for file or directory
        :param name: It represents the title of the show you'regex rebuilding to proper match the standard
        :param season: It represents the season of the show you'regex rebuilding to proper match the standard
        :param episode: It represents the episode of the show you'regex rebuilding to proper match the standard
        :param subtitle: It represents the subs tag
        :param language: It represents the language of the show
        :param extension: It represents the extension of the file containing the show
        :param debug: It represents the debug status of the function, default it's False
        :return: SUBTITLE_NAME
        '''
        try:
            SUBTITLE_NAME = ('{name}{episode}{subtitle}{language}{extension}').format(
                name=eval_wrapped_key(value=name, wrap_type=NONE_WRAP),
                episode=eval_wrapped_key(value=('E' + episode), wrap_type=EMPTY_WRAP),
                subtitle=eval_wrapped_key(value=subtitle, wrap_type=PARENTHESIS_WRAP),
                language=eval_wrapped_key(value=language, wrap_type=DASH_PARENTHESIS_WRAP),
                extension=eval_wrapped_key(value=extension, wrap_type=EXTENSION_WRAP)
            )

            if debug:
                print ('{engine}: {name}').format(engine=self.name, name=SUBTITLE_NAME)

            return SUBTITLE_NAME

        except Exception as e:
            print e

