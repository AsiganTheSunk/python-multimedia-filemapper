import re

class CheckCommonExtension():
    def __init__(self):
        self.name = 'CheckCommonExtension'
        return

    def check_unwanted(self, stream, debug=False):
        '''
        This function checks if the stream it's a unwanted file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        status = False
        _unwanted_pattern = ['(\.com|\.txt|\.nfo)']
        try:
            re.search(_unwanted_pattern[0], stream).group(0)
        except AttributeError:
            return status
        else:
            status = True
            if debug:
                print('{extension_engine}: {stream} :: status:{status}').format(extension_engine=self.name, stream=stream,
                                                                                status=str(status))
            return status

    def check_multimedia (self, stream, debug=False):
        '''
        This function checks if the stream it's a multimedia file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        status = False
        _multimedia_pattern = ['(\.mkv|\.mp4)']
        try:
            re.search(_multimedia_pattern[0], stream).group(0)
        except AttributeError:
            return status
        else:
            status = True
            if debug:
                print('{extension_engine}: {stream} :: status:{status}').format(extension_engine=self.name, stream=stream,
                                                                                status=str(status))
            return status

    def check_subtitles(self, stream, debug=False):
        '''
        This function checks if the stream it's a subtitles file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        status = False
        _subtitle_pattern = ['(\.sub|\.srt|\.ass)$']
        try:
            re.search(_subtitle_pattern[0], stream).group(0)

        except AttributeError:
            return status
        else:
            status = True
            if debug:
                print('{extension_engine}: {stream} :: status:{status}').format(extension_engine=self.name, stream=stream,
                                                                                status=str(status))
            return status

    def check_subtitles_directory(self, stream, debug=False):
        '''
        This function checks if the stream it's a directory returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        status = False
        _subtitle_pattern = ['(sub\w{0,6}(?!=\!))']
        try:
            r = re.search(_subtitle_pattern[0], stream).group(0)
            print r
        except AttributeError:
            return status
        else:
            status = True
            if debug:
                print('{extension_engine}: {stream} :: status:{status}').format(extension_engine=self.name, stream=stream,
                                                                                status=str(status))
            return status
