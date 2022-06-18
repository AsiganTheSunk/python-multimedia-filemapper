from typing import List

from multimedia_filemapper.core.metadata_engine.struct_data.metadata import Metadata
from multimedia_filemapper.core.rename_engine.core.utils.stringutils import StringUtils
from multimedia_filemapper.core.constants.media_file_flags import FileFlags

EMPTY_WRAP = -1
BRACKET_WRAP = 0
PARENTHESIS_WRAP = 1
DASH_PARENTHESIS_WRAP = 2
EXTENSION_WRAP = 3
DASH_EMPTY_WRAP = 4
NONE_WRAP = 5


class StringFilmExtension:
    def __init__(self):
        self.name = 'FilmExtension'
        self.supported_fflags = [
            FileFlags.FILM_DIRECTORY_FLAG,
            FileFlags.FILM_FLAG,
        ]
        self.supported_season_fflags: List[FileFlags] = []
        self.supported_subtitle_folder_fflags: List[FileFlags] = [
            FileFlags.SUBTITLE_DIRECTORY_FILM_FLAG
        ]
        self.supported_subtitle_file_fflags: List[FileFlags] = [
            FileFlags.SUBTITLE_FILM_FLAG
        ]
        self.string_utils = StringUtils()

    def build_name(self, metadata: Metadata):
        """
        This function builds a film name for file or directory
        :param metadata:
        :return: FILM_NAME
        """
        try:
            _name = self.string_utils.eval_wrapped_key(value=metadata.name, wrap_type=NONE_WRAP)
            _year = self.string_utils.eval_wrapped_key(value=metadata.year, wrap_type=PARENTHESIS_WRAP)
            _film_tag = self.string_utils.eval_wrapped_key(value=metadata.film_tag, wrap_type=EMPTY_WRAP)
            _quality = self.string_utils.eval_wrapped_key(value=metadata.quality, wrap_type=BRACKET_WRAP)
            _vcodec = self.string_utils.eval_wrapped_key(value=metadata.vcodec, wrap_type=BRACKET_WRAP)
            _extension = self.string_utils.eval_wrapped_key(value=metadata.extension, wrap_type=EXTENSION_WRAP)
            FILM_NAME = f'{_name}{_year}{_film_tag}{_quality}{_extension}'
            # print(f'StringFilmExtension.build_name("{metadata}") ->: {FILM_NAME}')
            return FILM_NAME

        except Exception as e:
            print(e)

    def build_subtitle_name(self, metadata: Metadata):
        """
        This function builds a film subtitle_engine name for file or directory
        :param metadata:
        :return: SUBTITLE_NAME
        """

        try:
            _name = self.string_utils.eval_wrapped_key(value=metadata.name, wrap_type=NONE_WRAP)
            _year = self.string_utils.eval_wrapped_key(value=metadata.year, wrap_type=PARENTHESIS_WRAP)
            _film_tag = self.string_utils.eval_wrapped_key(value=metadata.film_tag, wrap_type=EMPTY_WRAP)
            _quality = self.string_utils.eval_wrapped_key(value=metadata.quality, wrap_type=BRACKET_WRAP)
            # _subtitle = self.string_utils.eval_wrapped_key(value=metadata.subtitle, wrap_type=PARENTHESIS_WRAP)
            _language = self.string_utils.eval_wrapped_key(value=metadata.language, wrap_type=PARENTHESIS_WRAP)
            _extension = self.string_utils.eval_wrapped_key(value=metadata.extension, wrap_type=EXTENSION_WRAP)
            SUBTITLE_NAME = f'{_name}{_year}{_quality}{_language}{_extension}'
            # print(f'StringFilmExtension.build_name("{metadata}") ->: {SUBTITLE_NAME}')
            return SUBTITLE_NAME
        except Exception as e:
            print(e)
