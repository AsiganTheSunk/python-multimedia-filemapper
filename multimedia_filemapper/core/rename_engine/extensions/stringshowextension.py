from multimedia_filemapper.core.rename_engine.core.utils.stringutils import StringUtils
from multimedia_filemapper.core.constants.media_file_flags import FileFlags as fflags

EMPTY_WRAP = -1
BRACKET_WRAP = 0
PARENTHESIS_WRAP = 1
DASH_PARENTHESIS_WRAP = 2
EXTENSION_WRAP = 3
DASH_EMPTY_WRAP = 4
NONE_WRAP = 5


class StringShowExtension:
    def __init__(self):
        self.name = 'ShowExtension'
        self.supported_fflags = [fflags.SHOW_DIRECTORY_FLAG, fflags.SHOW_FLAG]
        self.supported_season_fflags = [fflags.SEASON_DIRECTORY_FLAG]
        self.supported_subtitle_folder_fflags = [fflags.SUBTITLE_DIRECTORY_SHOW_FLAG]
        self.supported_subtitle_file_fflags = [fflags.SUBTITLE_SHOW_FLAG]
        self.string_utils = StringUtils()
        return

    '''
        ShowExtension:
            This section of the code contains the following functions

            build_show_name:
            build_show_subtitle_name:
            build_show_season_name:
    '''

    def build_name(self, metadata):
        '''
        This function builds a show name directory
        :param name: It represents the title of the show you'regex_engine rebuilding to proper match the standard
        :param season: It represents the season of the show you'regex_engine rebuilding to proper match the standard
        :param episode: It represents the episode of the show you'regex_engine rebuilding to proper match the standard
        :param ename: It represents the name of the episode of the show you'regex_engine rebuilding to proper match the standard
        :param quality: It represents the resolution of the show you'regex_engine rebuilding to proper match the standard
        :param extension: It represents the extensions of the file containing the show
        :param debug: It represents the debug status of the function, default it's False
        :return: SHOW_NAME
        '''
        try:

            _name = self.string_utils.eval_wrapped_key(value=metadata.name, wrap_type=NONE_WRAP)
            _season = self.string_utils.eval_wrapped_key(value=('S' + metadata.season), wrap_type=EMPTY_WRAP)
            _episode = self.string_utils.eval_wrapped_key(value=('E' + metadata.episode), wrap_type=NONE_WRAP)
            _ename = self.string_utils.eval_wrapped_key(value=metadata.ename, wrap_type=DASH_EMPTY_WRAP)
            _quality = self.string_utils.eval_wrapped_key(value=metadata.quality, wrap_type=BRACKET_WRAP)
            # _vcodec = self.string_utils.eval_wrapped_key(value=metadata.vcodec, wrap_type=BRACKET_WRAP)
            _extension = self.string_utils.eval_wrapped_key(value=metadata.extension, wrap_type=EXTENSION_WRAP)
            SHOW_NAME = f'{_name}{_season}{_episode}{_ename}{_quality}{_extension}'
            # print(f'{self.name}: {SHOW_NAME}')
            return SHOW_NAME

        except Exception as e:
            print(e)

    def build_subtitle_name(self, metadata):
        '''
        This function builds a subtitle_engine name for file or directory
        :param name: It represents the title of the show you'regex_engine rebuilding to proper match the standard
        :param season: It represents the season of the show you'regex_engine rebuilding to proper match the standard
        :param episode: It represents the episode of the show you'regex_engine rebuilding to proper match the standard
        :param subtitle: It represents the subtitle_engine tag
        :param language: It represents the language of the show
        :param extension: It represents the extensions of the file containing the show
        :param debug: It represents the debug status of the function, default it's False
        :return: SUBTITLE_NAME
        '''
        try:
            _name = self.string_utils.eval_wrapped_key(value=metadata.name, wrap_type=NONE_WRAP)
            _season = self.string_utils.eval_wrapped_key(value=('S' + metadata.season), wrap_type=EMPTY_WRAP)
            _episode = self.string_utils.eval_wrapped_key(value=('E' + metadata.episode), wrap_type=NONE_WRAP)
            _subtitle = self.string_utils.eval_wrapped_key(value=metadata.subtitle, wrap_type=PARENTHESIS_WRAP)
            _language = self.string_utils.eval_wrapped_key(value=metadata.language, wrap_type=DASH_PARENTHESIS_WRAP)
            _extension = self.string_utils.eval_wrapped_key(value=metadata.extension, wrap_type=EXTENSION_WRAP)

            SUBTITLE_NAME = f'{_name}{_season}{_episode}{_subtitle}{_language}{_extension}'
            # print(f'{self.name}: {SUBTITLE_NAME}')
            return SUBTITLE_NAME

        except Exception as e:
            print(e)

    def build_season_name(self, metadata):
        '''
        This function builds a season name for directory
        :param name: It represents the title of the show you'regex_engine rebuilding to proper match the standard
        :param season: It represents the season of the show you'regex_engine rebuilding to proper match the standard
        :param debug: It represents the debug status of the function, default it's False
        :return: SEASON_NAME
        '''
        try:
            _name = self.string_utils.eval_wrapped_key(value=metadata.name, wrap_type=NONE_WRAP)
            _season = self.string_utils.eval_wrapped_key(value=('Season ' + str(int(metadata.season))), wrap_type=BRACKET_WRAP)
            SEASON_NAME = f'{_name}{_season}'
            # print(f'{self.name}: {SEASON_NAME}')
            return SEASON_NAME
        except Exception as e:
            print(e)
