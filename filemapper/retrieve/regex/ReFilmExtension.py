from filemapper.datastructure.FileFlags import FileFlags as fflags
from filemapper.retrieve.regex.ReEngine import compile_patterns
from config import TRUSTED_UPLOADERS
import re

class ReFilmExtension():
    def __init__(self):
        self.name = 'ReFilmExtension'
        self.supported_name_fflags = [fflags.FILM_DIRECTORY_FLAG, fflags.FILM_FLAG]
        self.supported_season_fflags = []
        self.supported_subtitle_fflags = []
        return

    def get_name(self, stream, season_directory=False, debug=False):
        '''
        This function retrieves the name of the film from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: NAME
        '''
        _tail_patterns = compile_patterns(patterns=['(([1-2])([890])(\d{2}))(?!p)'])
        _name_patterns = compile_patterns(patterns=['(.*)(([1-2])([890])(\d{2}))(?!p)'])
        try:
            tail = re.search(_tail_patterns[0], stream).group(0)
            name = re.search(_name_patterns[0], stream).group(0)[:-(len(tail))]
        except ValueError or TypeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            name = ''
            return name
        else:
            if debug:
                print('{extension_engine}: {stream} :: {value}').format(extension_engine=self.name,
                                                                        stream=stream,
                                                                        value=name)
            return name

    def get_episode(self, stream, debug=False):
        return

    def get_season(self, stream, season_directory=False, debug=False):
        return

    def get_year(self, stream, debug=False):
        '''
        This function retrieves the tags of the film from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: YEAR
        '''
        _year_patterns = compile_patterns(patterns=['(([1-2])([890])(\d{2}))(?!p)'])
        try:
            year = re.search(_year_patterns[0], stream).group(0)
        except ValueError or TypeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            year = ''
            return year
        else:
            if debug:
                print('{extension_engine}: {stream} :: {value}').format(extension_engine=self.name,
                                                                        stream=stream,
                                                                        value=year)
            return year

    def get_tags(self, stream, debug=False):
        '''
        This function retrieves the tags of the film from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: TAGS
        '''
        _film_tag_patterns = compile_patterns(patterns='(EXTENDED(.*)?CUT)|REMASTERED')
        try:
            film_tag = re.search(_film_tag_patterns[0], stream, re.IGNORECASE).group(0)
        except ValueError or TypeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            film_tag = ''
            return film_tag
        else:
            if debug:
                print('{extension_engine}: {stream} :: {value}').format(extension_engine=self.name,
                                                                        stream=stream,
                                                                        value=film_tag)
            return film_tag