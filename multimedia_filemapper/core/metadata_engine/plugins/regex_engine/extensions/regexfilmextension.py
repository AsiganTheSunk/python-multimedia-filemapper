# from filemapper.metadata_engine.regex_engine.RegexEngine import compile_pattern
import re

from multimedia_filemapper.core.rename_engine.core.stringbuilder import StringBuilder
from multimedia_filemapper.core.constants.media_file_flags import FileFlags


def compile_pattern(patterns):
    return [re.compile(pattern) for pattern in patterns]


class RegexFilmExtension:
    def __init__(self):
        self.name = 'RegexFilmExtension'
        self.supported_fflags = [
            FileFlags.FILM_DIRECTORY_FLAG,
            FileFlags.FILM_FLAG,
        ]
        self.supported_season_fflags = []
        self.supported_subtitle_fflags = [
            FileFlags.SUBTITLE_DIRECTORY_FILM_FLAG,
            FileFlags.SUBTITLE_FILM_FLAG,
        ]

    def get_name(self, stream, season_directory=False):
        """
        This function retrieves the name of the film from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: NAME
        """
        _tail_patterns = ['((\(?)([1-2])([890])(\d{2})(\))?)(?!p)']
        _name_patterns = ['(.*)(([1-2])([890])(\d{2})(\))?)(?!p)']
        string_builder = StringBuilder()
        try:
            tail = re.search(_tail_patterns[0], stream).group(0)
            name = re.search(_name_patterns[0], stream).group(0)[:-(len(tail))]
        except AttributeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            name = ''
            return name
        else:
            name = string_builder.prettify_stream(name)
            # print(f'{self.name}: {stream} :: name:{name}')
            return name

    def get_episode(self, stream, debug=False):
        return ''

    def get_season(self, stream, season_directory=False):
        return ''

    def get_year(self, stream, debug=False):
        """
        This function retrieves the tags of the film from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: YEAR
        """
        _year_patterns = ['(([1-2])([890])(\d{2}))(?!p)']
        try:
            year = re.search(_year_patterns[0], stream).group(0)
        except AttributeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            year = ''
            return year
        else:
            # print(f'{self.name}: {stream} :: year:{year}')
            return str(year)

    def get_tags(self, stream):
        """
        This function retrieves the tags of the film from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: TAGS
        """
        _film_tag_patterns = ['EXTENDED(.*)?CUT|REMASTERED']
        string_builder = StringBuilder()
        try:
            film_tag = re.search(_film_tag_patterns[0], stream, re.IGNORECASE).group(0)
        except AttributeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            film_tag = ''
            return film_tag
        else:
            film_tag = string_builder.prettify_stream(film_tag, title=False)
            # print(f'{self.name}: {stream} :: tags:{film_tag}')
            return film_tag
