from filemapper.datastructure.FileFlags import FileFlags as fflags
from filemapper.retrieve.regex.ReEngine import compile_patterns
from config import TRUSTED_UPLOADERS
import re

class ReAnimeExtension():
    def __init__(self):
        self.name = 'ReAnimeExtension'
        self.supported_name_fflags = [fflags.ANIME_DIRECTORY_FLAG, fflags.ANIME_FLAG]
        self.supported_season_fflags = []
        self.supported_subtitle_fflags = []
        return


    def get_name(self, stream, season_directory=False, debug=False):
        '''
        This function retrieves the name of the anime from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: NAME
        '''
        _uploader_patterns = compile_patterns(patterns=TRUSTED_UPLOADERS)
        _core_patterns = compile_patterns(patterns=['E(pisode)(\-|\.|\s)?(\d{2,3})'])
        _tail_patterns = compile_patterns(patterns=['\[(\w+.*?)\s(\-|x)',
                                                    '\[(\w+.*?)E(pisode)?(x|\-|\.|\s)?(\d{2,3})'])
        try:
            header = len(re.search(_uploader_patterns[0], stream, re.IGNORECASE).group(0)) + 1
            tail = re.search( _tail_patterns[0], stream, re.IGNORECASE).group(0)

        except ValueError or TypeError:
            try:
                header = len(re.search(_uploader_patterns[0], stream, re.IGNORECASE).group(0)) + 1
                tail = re.search( _tail_patterns[1], stream, re.IGNORECASE).group(0)
                core = len(re.search( _core_patterns[0], stream, re.IGNORECASE).group(0))

            except ValueError or TypeError:
                #raise error that would be corrected in ReEngine turning exception into blank field
                name = ''
                return name
            else:
                name = tail[header:-core]
                if debug:
                    print('{extension_engine}: {stream} :: {value}').format(extension_engine=self.name,
                                                                            stream=stream,
                                                                            value=name)
                return name
        else:
            name = tail[header:-2]
            if debug:
                print('{extension_engine}: {stream} :: {value}').format(extension_engine=self.name,
                                                                        stream=stream,
                                                                        value=name)
            return name

    def get_episode(self, stream, debug=False):
        '''
        This function retrieves the episode of the anime from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: EPISODE
        '''
        _episode_patterns = compile_patterns(patterns=['\-.?\d{1,3}','Episode(\-|\s|\.)?(\d{1,3})',
                                                       '(x|E)(\d{1,3})'])
        try:
            episode = re.search(_episode_patterns[0], stream, re.IGNORECASE).group(0)
        except ValueError or TypeError:
            try:
                episode = re.search(_episode_patterns[1], stream, re.IGNORECASE).group(0)
            except ValueError or TypeError:
                try:
                    episode = re.search(_episode_patterns[2], stream, re.IGNORECASE).group(0)
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
            else:
                episode = episode[8:]
                if debug:
                    print('{extension_engine}: {stream} :: {value}').format(extension_engine=self.name,
                                                                            stream=stream,
                                                                            value=episode)
                return episode
        else:
            episode = episode[2:]
            if debug:
                print('{extension_engine}: {stream} :: {value}').format(extension_engine=self.name,
                                                                        stream=stream,
                                                                        value=episode)
            return episode


    def get_season(self, stream, season_directory=False, debug=False):
        return

    def get_year(self, stream, debug=False):
        return

    def get_tags(self, stream, debug=False):
        return