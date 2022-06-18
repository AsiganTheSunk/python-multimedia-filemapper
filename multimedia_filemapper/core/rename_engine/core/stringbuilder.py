
from multimedia_filemapper.core.rename_engine.extensions.stringfilmextension import StringFilmExtension
from multimedia_filemapper.core.rename_engine.extensions.stringshowextension import StringShowExtension
from multimedia_filemapper.core.rename_engine.extensions.stringanimeextension import StringAnimeExtension
from multimedia_filemapper.core.metadata_engine.struct_data.metadata import Metadata
from multimedia_filemapper.core.constants.media_file_flags import FileFlags as fflags

EMPTY_WRAP = -1
BRACKET_WRAP = 0
PARENTHESIS_WRAP = 1
DASH_PARENTHESIS_WRAP = 2
EXTENSION_WRAP = 3


def eval_wrapped_key(value, wrap_type):
    """
    This function peform auxiliary help to the build name functions validating the content of the string
    :param value: It represents the key you'regex_engine testing
    :param wrap_type: It represents the type of wrapping the string it's going to get, numbers 0 to 2, being
                    0 for [value], 1 for (value), 2 for -(value) 3 value
    :return: modified value
    """
    if value is None:
        return ''
    else:
        if wrap_type == 0:
            return '[' + value + ']'
        elif wrap_type == 1:
            return '(' + value + ')'
        elif wrap_type == 2:
            return ' - (' + value + ')'
        elif wrap_type == 3:
            return '.' + value
        else:
            return value


class StringBuilder:
    def __init__(self):
        self.extension_engines = [
            StringAnimeExtension(),
            StringShowExtension(),
            StringFilmExtension()
        ]

    # ADD DUMMY FLAGS FUNCTIONS! to try to remap properly
    def prettify_stream(self, stream, title=True):
        """
        This function makes a stream look pretty, removing dots, dashes and spaces
        :param stream: It represents the input string of the function
        :return: PRETTY_STREAM
        """
        try:
            if title:
                new_stream = stream.replace('-', ' ').replace('.', ' ').replace('_', ' ').rstrip().title()
            else:
                new_stream = stream.replace('-', ' ').replace('.', ' ').replace('_', ' ').rstrip()
        except Exception as e:
            return stream
        else:
            return new_stream

    '''
        GENERAL FUNCTIONS:
            This section of the code contains the following functions

            build_name:
    '''

    def rebuild_name(self, metadata: Metadata) -> str:
        """
        This function rebuilds the name of a show|movie|anime from a given class Metadata Object
        :param metadata: It represents the metadata_engine gathered from the MetadataEngine
        :return: NEW_NAME
        """

        try:
            if metadata.fflag in (fflags.LIBRARY_FLAG, fflags.MAIN_SHOW_DIRECTORY_FLAG, fflags.IGNORE_FLAG):
                return metadata.name
            else:
                for extension_engine in self.extension_engines:
                    if metadata.fflag in extension_engine.supported_fflags:
                        return extension_engine.build_name(metadata)
                    elif metadata.fflag in extension_engine.supported_subtitle_file_fflags:
                        return extension_engine.build_subtitle_name(metadata)
                    elif metadata.fflag in extension_engine.supported_subtitle_folder_fflags:
                        return extension_engine.build_subtitle_name(metadata)
                    elif metadata.fflag in extension_engine.supported_season_fflags:
                        return extension_engine.build_season_name(metadata)

        except Exception as e:
            print(e)
