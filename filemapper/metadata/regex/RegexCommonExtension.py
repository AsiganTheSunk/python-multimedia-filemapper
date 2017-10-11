import re

from filemapper.utils.FileFlags import FileFlags as fflags


class RegexCommonExtension():
    def __init__(self):
        self.name = 'RegexCommonExtension'
        self.supported_fflags = [fflags.FILM_DIRECTORY_FLAG, fflags.FILM_FLAG,
                                 fflags.ANIME_DIRECTORY_FLAG, fflags.ANIME_FLAG,
                                 fflags.SHOW_DIRECTORY_FLAG, fflags.SHOW_FLAG]
        self.supported_season_fflags = [fflags.SEASON_DIRECTORY_FLAG]
        self.supported_subtitle_fflags = [fflags.SUBTITLE_DIRECTORY_FILM_FLAG,
                                          fflags.SUBTITLE_FILM_FLAG,
                                          fflags.SUBTITLE_DIRECTORY_SHOW_FLAG,
                                          fflags.SUBTITLE_SHOW_FLAG,
                                          fflags.SUBTITLE_DIRECTORY_ANIME_FLAG,
                                          fflags.SUBTITLE_ANIME_FLAG]
        return

    def get_uploader(self, stream, debug=False):
        '''
        This function retrieves the uploader of the of the file or directory from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: UPLOADER
        '''
        _uploader_patterns = [
            'HorribleSubs|AnimeRG|Krosis|Dmcs-Fansubs|Ohys-Raws|PuyaSubs!|FUM|DIMENSION|PODO|ROVERS']

        try:
            uploader = re.search(_uploader_patterns[0], stream,
                                 re.IGNORECASE).group(0)
        except AttributeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            uploader = ''
            return uploader

        else:
            if debug:
                print(
                '{extension_engine}: {stream} :: uploader:{value}').format(
                    extension_engine=self.name,
                    stream=stream,
                    value=uploader)
            return uploader

    def get_quality(self, stream, debug=False):
        '''
        This function retrieves the quality(resolution) of the file or directory from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: QUALITY
        '''

        _quality_patterns = ['(\d{3,4}p)',
                             'BRRip|HDRip|BluRay|DvdRip|WEB(\-)?DL|WEB(\-)?Rip|HDtv',
                             '\d{4}x\d{3,4}']
        try:
            quality = re.search(_quality_patterns[0], stream).group(0)
        except AttributeError:
            try:
                quality = re.search(_quality_patterns[1], stream,
                                    re.IGNORECASE).group(0)
            except AttributeError:
                try:
                    quality = re.search(_quality_patterns[2], stream,
                                        re.IGNORECASE).group(0)
                except AttributeError:
                    # raise error that would be corrected in ReEngine turning exception into blank field
                    quality = ''
                    return quality
                else:
                    quality = quality[5:] + 'p'
                    if debug:
                        print(
                        '{extension_engine}: {stream} :: quality:{value}').format(
                            extension_engine=self.name,
                            stream=stream,
                            value=quality)
                    return quality
            else:
                if debug:
                    print(
                    '{extension_engine}: {stream} :: quality:{value}').format(
                        extension_engine=self.name,
                        stream=stream,
                        value=quality)
                return quality
        else:
            if debug:
                print('{extension_engine}: {stream} :: quality:{value}').format(
                    extension_engine=self.name,
                    stream=stream,
                    value=quality)
            return quality

    def get_acodec(self, stream, debug=False):
        '''
        This function retrieves the audio codec of the file or directory from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: ACODEC
        '''
        _acodec_patterns = ['((AC3)|(DTS)|(DD5\.1)|(ACC(2\.0)?)|(MP3))']
        try:
            acodec = re.search(_acodec_patterns[0], stream,
                               re.IGNORECASE).group(0)
        except AttributeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            acodec = ''
            return acodec
        else:
            if debug:
                print('{extension_engine}: {stream} :: acodec:{value}').format(
                    extension_engine=self.name,
                    stream=stream,
                    value=acodec)
            return acodec

    def get_vcodec(self, stream, debug=False):
        '''
        This function retrieves the video codec of the file or directory from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: VCODEC
        '''
        _vcodec_patterns = ['((x264)|(H264)|(x265)|(H265)|(XviD)|(DivX))']
        try:
            vcodec = re.search(_vcodec_patterns[0], stream,
                               re.IGNORECASE).group(0)
        except AttributeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            vcodec = ''
            return vcodec
        else:
            if debug:
                print('{extension_engine}: {stream} :: vcodec:{value}').format(
                    extension_engine=self.name,
                    stream=stream,
                    value=vcodec)
            return vcodec

    def get_extension(self, stream, debug=False):
        '''
        This function retrieves the extension of the file or directory from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: EXTENSION
        '''
        _extension_pattenrs = ['(\.mkv|\.mp4|\.srt|\.ass)$']
        try:
            extension = re.search(_extension_pattenrs[0], stream).group(0)
        except AttributeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            extension = ''
            return extension
        else:
            extension = extension[1:]
            if debug:
                print(
                '{extension_engine}: {stream} :: extension:{value}').format(
                    extension_engine=self.name,
                    stream=stream,
                    value=extension)
            return extension

    def get_source(self, stream, debug=False):
        '''
        This function retrieves the source of the file or directory from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: SOURCE
        '''
        _source_patterns = ['rartv|rarbg|ettv']
        try:
            source = re.search(_source_patterns[0], stream,
                               re.IGNORECASE).group(0)
        except AttributeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            source = ''
            return source
        else:
            if debug:
                print('{extension_engine}: {stream} :: source:{value}').format(
                    extension_engine=self.name,
                    stream=stream,
                    value=source)
            return source

    def get_unwanted(self, stream, debug=False):
        '''
        This function retrieves the unwanted file argument from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: UNWANTED
        '''
        try:
            unwanted = re.search('(((\.txt)|(\.nfo))$)', stream,
                                 re.IGNORECASE).group(0)
        except AttributeError:
            # raise error that would be corrected in ReEngine turning exception into blank field
            unwanted = ''
            return unwanted
        else:
            unwanted = stream
            if debug:
                print(
                '{extension_engine}: {stream} :: unwanted:{value}').format(
                    extension_engine=self.name,
                    stream=stream,
                    value=unwanted)
            return unwanted

    def get_language(self, stream, debug=False):
        _language_patterns = ['\(es\)|\(spanish\)|\(en\w{0,5}\)']
        try:
            language = re.search(_language_patterns[0], stream,
                                 re.IGNORECASE).group(0)
        except AttributeError:
            language = ''
            return language
        else:
            language = language[1:-1]
            if debug:
                print(
                '{extension_engine}: {stream} :: language:{value}').format(
                    extension_engine=self.name,
                    stream=stream,
                    value=language)
            return language
