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
        if wrap_type is 0:
            return ('[' + value + ']')
        elif wrap_type is 1:
            return ('(' + value + ')')
        elif wrap_type is 2:
            return (' - (' + value + ')')
        elif wrap_type is 3:
            return ('.' + value)
        else:
            return value

EMPTY_WRAP = -1
BRACKET_WRAP = 0
PARENTHESIS_WRAP = 1
DASH_PARENTHESIS_WRAP = 2
EXTENSION_WRAP = 3

class ShowExtension():
    def __init__(self):
        self.name = 'ShowExtension'
        self.supported_name_fflags = [fflags.SHOW_DIRECTORY_FLAG, fflags.SHOW_FLAG]
        self.supported_season_fflags = [fflags.SEASON_DIRECTORY_FLAG]
        self.supported_subtitle_fflags = [fflags.SUBTITLE_DIRECTORY_SHOW_FLAG, fflags.SUBTITLE_SHOW_FLAG]
        return

    '''
        ShowExtension:
            This section of the code contains the following functions

            build_show_name:
            build_show_subtitle_name:
            build_show_season_name:
    '''

    def build_name(self, name, year, season, episode, ename, quality, extension, film_tag, debug=False):
        '''
        This function builds a show name directory
        :param name: It represents the title of the show you'regex rebuilding to proper match the standard
        :param season: It represents the season of the show you'regex rebuilding to proper match the standard
        :param episode: It represents the episode of the show you'regex rebuilding to proper match the standard
        :param ename: It represents the name of the episode of the show you'regex rebuilding to proper match the standard
        :param quality: It represents the resolution of the show you'regex rebuilding to proper match the standard
        :param extension: It represents the extension of the file containing the show
        :param debug: It represents the debug status of the function, default it's False
        :return: SHOW_NAME
        '''
        try:
            SHOW_NAME = ('{name} S{season}E{episode} {ename} [{quality}]{extension}').format(
                name=eval_wrapped_key(value=name, wrap_type=EMPTY_WRAP),
                season=eval_wrapped_key(value=season, wrap_type=EMPTY_WRAP),
                episode=eval_wrapped_key(value=episode, wrap_type=EMPTY_WRAP),
                ename=eval_wrapped_key(value=ename, wrap_type=EMPTY_WRAP),
                quality=eval_wrapped_key(value=quality, wrap_type=BRACKET_WRAP),
                extension=eval_wrapped_key(value=extension, wrap_type=EXTENSION_WRAP))

            if debug:
                print ('{engine}: {name}').format(engine=self.name, name=SHOW_NAME)

            return SHOW_NAME

        except:
            raise (Exception)

    def build_subtitle_name(self, name, year, season, episode, subtitle, language, extension, debug=False):
        '''
        This function builds a subs name for file or directory
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
            SUBTITLE_NAME = ('{name} S{season}E{episode} {subs} {language}{extension}').format(
                name=eval_wrapped_key(value=name, wrap_type=EMPTY_WRAP),
                season=eval_wrapped_key(value=season, wrap_type=EMPTY_WRAP),
                episode=eval_wrapped_key(value=episode, wrap_type=EMPTY_WRAP),
                subtitle=eval_wrapped_key(value=subtitle, wrap_type=PARENTHESIS_WRAP),
                language=eval_wrapped_key(value=language, wrap_type=DASH_PARENTHESIS_WRAP),
                extension=eval_wrapped_key(value=extension, wrap_type=EXTENSION_WRAP)
            )

            if debug:
                print ('{engine}: {name}').format(engine=self.name, name=SUBTITLE_NAME)

            return SUBTITLE_NAME

        except:
            raise (Exception)

    def build_season_name(self, name, season, debug=False):
        '''
        This function builds a season name for directory
        :param name: It represents the title of the show you'regex rebuilding to proper match the standard
        :param season: It represents the season of the show you'regex rebuilding to proper match the standard
        :param debug: It represents the debug status of the function, default it's False
        :return: SEASON_NAME
        '''
        try:
            SEASON_NAME = ('{name} {season}').format(
                name=eval_wrapped_key(value=name, wrap_type=EMPTY_WRAP),
                season=eval_wrapped_key(value=('Season ' + season), wrap_type=BRACKET_WRAP)
            )

            if debug:
                print ('{engine}: {name}').format(engine=self.name, name=SEASON_NAME)

            return SEASON_NAME
        except:
            raise (Exception)
