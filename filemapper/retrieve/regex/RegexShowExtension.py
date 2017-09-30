from filemapper.datastructure.FileFlags import FileFlags as fflags
# from filemapper.retrieve.regex.RegexEngine import compile_pattern
from config import TRUSTED_UPLOADERS
import re

def compile_pattern(patterns):
    return [re.compile(pattern) for pattern in patterns]

class RegexShowExtension():
    def __init__(self):
        self.name = 'ReShowExtension'
        self.supported_name_fflags = [fflags.SHOW_DIRECTORY_FLAG, fflags.SHOW_FLAG]
        self.supported_season_fflags = [fflags.SEASON_DIRECTORY_FLAG]
        self.supported_subtitle_fflags = [fflags.SUBTITLE_DIRECTORY_SHOW_FLAG, fflags.SUBTITLE_SHOW_FLAG]
        return

    def get_name(self, stream, season_directory=False, debug=False):
        '''
        This function retrieves the name of the show from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param season_directory: --, default value it's False
        :param debug: It represents the debug status of the function, default it's False
        :return: NAME
        '''
        _name_patterns = compile_pattern(patterns=[r'(.*)(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?',
                                                    r'(.*)([s]\d{1,2})'])
        _tail_patterns = compile_pattern(patterns=[r'(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?',
                                                    r'([s]\d{1,2})'])
        try:
            if season_directory:
                tail = re.search('(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?', stream, re.IGNORECASE).group(0)
                name = re.search('(.*)(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?', stream, re.IGNORECASE).group(0)[:-len(tail)]
            else:
                tail = re.search('([s]\d{1,2})', stream, re.IGNORECASE).group(0)
                name = re.search('(.*)([s]\d{1,2})', stream, re.IGNORECASE).group(0)[:-len(tail)]
        except ValueError or TypeError or AttributeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            name = ''
            return name
        else:
            if debug:
                print('{extension_engine}: {stream} :: name:{value}').format(extension_engine=self.name,
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
        _episode_pattern = compile_pattern(patterns=[r'([e])\d{2,3}'])
        try:
            episode = re.search('([e])\d{2,3}', stream, re.IGNORECASE).group(0)
        except ValueError or TypeError or AttributeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            episode = ''
            return episode
        else:
            episode = episode[1:]
            if debug:
                print('{extension_engine}: {stream} :: episode:{value}').format(extension_engine=self.name,
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
        _season_patterns = compile_pattern(patterns=[r'([s]\d{2})', r'\d{1,2}'])
        _season_directory_patterns = compile_pattern(patterns=[r'(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?'])
        try:
            if season_directory:
                season_directory = re.search('(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?', stream, re.IGNORECASE).group(0)
                season = re.search('\d{1,2}', season_directory, re.IGNORECASE).group(0)
            else:
                season = re.search('([s]\d{2})', stream, re.IGNORECASE).group(0)
                season = season[1:]
        except AttributeError:
            season = ''
            return season
        else:

            if debug:
                print('{extension_engine}: {stream} :: season:{value}').format(extension_engine=self.name,
                                                                        stream=stream,
                                                                        value=season)
            return season

    def get_year(self, stream, debug=False):
        return

    def get_tags(self, stream, debug=False):
        return