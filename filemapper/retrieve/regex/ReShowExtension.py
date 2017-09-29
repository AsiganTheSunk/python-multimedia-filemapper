from filemapper.datastructure.FileFlags import FileFlags as fflags
from filemapper.retrieve.regex.ReEngine import compile_patterns
from config import TRUSTED_UPLOADERS
import re

class ReShowExtension():
    def __init__(self):
        self.name = 'ReShowExtension'
        self.supported_name_fflags = [fflags.SHOW_DIRECTORY_FLAG, fflags.SHOW_FLAG]
        self.supported_season_fflags = [fflags.SEASON_DIRECTORY_FLAG]
        self.supported_subtitle_fflags = []
        return

    def get_name(self, stream, season_directory=False, debug=False):
        '''
        This function retrieves the name of the show from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param season_directory: --, default value it's False
        :param debug: It represents the debug status of the function, default it's False
        :return: NAME
        '''
        _name_patterns = compile_patterns(patterns=['(.*)(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?',
                                                    '(.*)([s]\d{1,2})'])
        _tail_patterns = compile_patterns(patterns=['(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?',
                                                    '([s]\d{1,2})'])
        try:
            if season_directory:
                tail = re.search(_tail_patterns[0], stream, re.IGNORECASE).group(0)
                name = re.search(_name_patterns[0], stream, re.IGNORECASE).group(0)[:-len(tail)]
            else:
                tail = re.search(_tail_patterns[1], stream, re.IGNORECASE).group(0)
                name = re.search(_name_patterns[1], stream, re.IGNORECASE).group(0)[:-len(tail)]
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
        '''
        This function retrieves the episode of the show from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: EPISODE
        '''
        _episode_pattern = compile_patterns(patterns=['([e])\d{2,3}'])
        try:
            episode = re.search(_episode_pattern[0], stream, re.IGNORECASE).group(0)
        except ValueError or TypeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            episode = ''
            return episode
        else:
            episode = episode[1:]
            if debug:
                print('{extension_engine}: {stream} :: {value}').format(extension_engine=self.name,
                                                                        stream=stream,
                                                                        value=episode)
            return episode

    def get_season(self, stream, season_directory=False, debug=False):
        '''
        This function retrieves the season of the show from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param season_directory: --, default value it's False
        :param debug: It represents the debug status of the function, default it's False
        :return: SEASON
        '''
        _season_patterns = compile_patterns(patterns=['([s]\d{2})', '\d{1,2}'])
        _season_directory_patterns = compile_patterns(patterns=['(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?'])
        try:
            if season_directory:
                season_directory = re.search(_season_directory_patterns[0], stream, re.IGNORECASE).group(0)
                season = re.search(_season_patterns[1], season_directory, re.IGNORECASE).group(0)
            else:
                season = re.search(_season_patterns[0], stream, re.IGNORECASE).group(0)
                season = season[1:]
        except ValueError or TypeError:
            season = ''
            return season
        else:

            if debug:
                print('{extension_engine}: {stream} :: {value}').format(extension_engine=self.name,
                                                                        stream=stream,
                                                                        value=season)
            return season

    def get_year(self, stream, debug=False):
        return

    def get_tags(self, stream, debug=False):
        return