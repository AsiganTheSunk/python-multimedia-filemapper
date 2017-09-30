from StringBuilder import eval_wrapped_key, EMPTY_WRAP, BRACKET_WRAP, DASH_PARENTHESIS_WRAP, PARENTHESIS_WRAP, EXTENSION_WRAP
from filemapper.datastructure.FileFlags import FileFlags as fflags

class AnimeExtension():
    def __init__(self):
        self.name = 'AnimeExtension'
        self.supported_name_fflags = [fflags.ANIME_DIRECTORY_FLAG, fflags.ANIME_FLAG]
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
            ANIME_NAME = ('{name} E{episode} {ename} {quality}{extension}').format(
                name=eval_wrapped_key(value=name, wrap_type=EMPTY_WRAP),
                episode=eval_wrapped_key(value=episode, wrap_type=EMPTY_WRAP),
                ename=eval_wrapped_key(value=ename, wrap_type=EMPTY_WRAP),
                quality=eval_wrapped_key(value=quality, wrap_type=BRACKET_WRAP),
                extension=eval_wrapped_key(value=extension, wrap_type=EXTENSION_WRAP)
            )

            if debug:
                print ('{engine}: {name}').format(engine=self.name, name=ANIME_NAME)

            return ANIME_NAME
        except:
            raise(Exception)


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
            SUBTITLE_NAME = ('{name} E{episode} {subs} {language}{extension}').format(
                name=eval_wrapped_key(value=name, wrap_type=EMPTY_WRAP),
                episode=eval_wrapped_key(value=episode, wrap_type=EMPTY_WRAP),
                subtitle=eval_wrapped_key(value=subtitle, wrap_type=PARENTHESIS_WRAP),
                language=eval_wrapped_key(value=language, wrap_type=DASH_PARENTHESIS_WRAP),
                extension=eval_wrapped_key(value=extension, wrap_type=EXTENSION_WRAP)
            )

            if debug:
                print ('{engine}: {name}').format(engine=self.name, name=SUBTITLE_NAME)

            return SUBTITLE_NAME

        except:
            raise(Exception)