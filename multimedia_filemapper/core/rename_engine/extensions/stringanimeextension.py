from multimedia_filemapper.core.rename_engine.core.utils.stringutils import StringUtils
from multimedia_filemapper.core.constants.media_file_flags import FileFlags as fflags

EMPTY_WRAP = -1
BRACKET_WRAP = 0
PARENTHESIS_WRAP = 1
DASH_PARENTHESIS_WRAP = 2
EXTENSION_WRAP = 3
DASH_EMPTY_WRAP = 4
NONE_WRAP = 5


class StringAnimeExtension:
    def __init__(self):
        self.name = 'AnimeExtension'
        self.supported_fflags = [fflags.ANIME_DIRECTORY_FLAG, fflags.ANIME_FLAG]
        self.supported_season_fflags = []
        self.supported_subtitle_folder_fflags = [fflags.SUBTITLE_DIRECTORY_ANIME_FLAG]
        self.supported_subtitle_file_fflags = [fflags.SUBTITLE_ANIME_FLAG]

        self.string_utils = StringUtils()
        return

    '''
        AnimeExtension:
            This section of the code contains the following functions

            build_anime_name:
            build_anime_subtitle_name:
    '''

    def build_name(self, metadata):
        """
        This function builds a anime name for file or directory
        :param name: It represents the title of the anime you'regex_engine rebuilding to proper match the standard
        :param episode: It represents the episode of the anime you'regex_engine rebuilding to proper match the standard
        :param ename: It represents the name of the episode of the anime you'regex_engine rebuilding to proper match the standard
        :param quality: It represents the resolution of the anime you'regex_engine rebuilding to proper match the standard
        :param extension: It represents the extensions of the file containing the anime
        :param debug: It represents the debug status of the function, default it's False
        :return:
        """
        try:
            _name = self.string_utils.eval_wrapped_key(value=metadata.name, wrap_type=NONE_WRAP)
            _episode = self.string_utils.eval_wrapped_key(value=('E' + metadata.episode), wrap_type=EMPTY_WRAP)
            _ename = self.string_utils.eval_wrapped_key(value=metadata.ename, wrap_type=EMPTY_WRAP)
            _quality = self.string_utils.eval_wrapped_key(value=metadata.quality, wrap_type=BRACKET_WRAP)
            # _vcodec = self.string_utils.eval_wrapped_key(value=metadata.vcodec, wrap_type=BRACKET_WRAP)
            _extension = self.string_utils.eval_wrapped_key(value=metadata.extension, wrap_type=EXTENSION_WRAP)
            ANIME_NAME = f'{_name}{_episode}{_ename}{_quality}{_extension}'
            # print(f'{self.name}: {ANIME_NAME}')
            return ANIME_NAME
        except Exception as e:
            print(e)

    def build_subtitle_name(self, metadata):
        """
        This function builds a subtitle_engine anime name for file or directory
        :param name: It represents the title of the show you'regex_engine rebuilding to proper match the standard
        :param season: It represents the season of the show you'regex_engine rebuilding to proper match the standard
        :param episode: It represents the episode of the show you'regex_engine rebuilding to proper match the standard
        :param subtitle: It represents the subtitle_engine tag
        :param language: It represents the language of the show
        :param extension: It represents the extensions of the file containing the show
        :param debug: It represents the debug status of the function, default it's False
        :return: SUBTITLE_NAME
        """
        try:
            _name = self.string_utils.eval_wrapped_key(value=metadata.name, wrap_type=NONE_WRAP)
            _episode = self.string_utils.eval_wrapped_key(value=('E' + metadata.episode), wrap_type=EMPTY_WRAP)
            _subtitle = self.string_utils.eval_wrapped_key(value=metadata.subtitle, wrap_type=PARENTHESIS_WRAP)
            _language = self.string_utils.eval_wrapped_key(value=metadata.language, wrap_type=DASH_PARENTHESIS_WRAP)
            _extension = self.string_utils.eval_wrapped_key(value=metadata.extension, wrap_type=EXTENSION_WRAP)
            SUBTITLE_NAME = f'{_name}{_episode}{_subtitle}{_language}{_extension}'
            print(f'{self.name}: {SUBTITLE_NAME}')
            return SUBTITLE_NAME

        except Exception as e:
            print(e)
