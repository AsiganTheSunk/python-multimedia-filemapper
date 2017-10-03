import re

class CheckAnimeExtension():
    def __init__(self):
        self.name = 'CheckAnimeExtension'
        return

    # TODO: Ver que hacer con esta funcion, que hace practicamente lo mismo que la normal
    def check_anime_show2(self, stream, debug=False):
        '''
        This function checks if the stream it's a anime file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        status = False
        _header_pattern  = ['(^\[(\w+(\s|\-|.?))+\])']
        _tail_pattern = ['(\-)(.?)\d{1,3}|(x|E(pisode)?)(\s|\.|\-)?\d{1,3}']
        try:
            re.search(_header_pattern[0], stream, re.IGNORECASE).group(0)
            re.search(_tail_pattern[0], stream, re.IGNORECASE).group(0)
        except AttributeError:
            return status
        else:
            status = True
            if debug:
                print('{extension_engine}: {stream} :: status:{status}').format(extension_engine=self.name, stream=stream,
                                                                                status=str(status))
            return status

    def check_anime_show(self, stream, debug=False):
        '''
        This function checks if the stream it's a anime show returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        status = False
        try:
            re.search('\[(\w+-?)*\](\s\w+)*\s(.?\s)?(\d{0,3}|E\w{0,6}.?\d{0,3})\s\(?\[?(\d{3,4}p|.*)\)?\]?(.mp4|.mkv)', stream, re.IGNORECASE).group(0)
        except AttributeError:
            try:
                re.search('^\[(\w+(\s|\-|.?))+\]', stream, re.IGNORECASE).group(0)
                re.search('\-(.?)\d{1,3}|(x|E(pisode)?)(\s|\.|\-)?\d{1,3}', stream, re.IGNORECASE).group(0)
                re.search('\.mp4|\.mkv', stream, re.IGNORECASE).group(0)
            except AttributeError:
                return status
            else:
                status = True
                if debug:
                    print('{extension_engine}: {stream} :: status:{status}').format(extension_engine=self.name, stream=stream,
                                                                                    status=str(status))
                return status
        else:
            status = True
            if debug:
                print('{extension_engine}: {stream} :: status:{status}').format(extension_engine=self.name, stream=stream,
                                                                                status=str(status))
            return status

    def check_anime_directory(self, stream, debug=False):
        '''
        This function checks if the stream it's anime directory returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        status = False
        _header_pattern = ['^\[(\w+(\s|\-|.?))+\]']
        _tail_pattern = ['\-(.?)\d{1,3}|(x|E(pisode)?)(\s|\.|\-)?\d{1,3}']
        try:
            # regex.search('\[(\w+-?)*\](\s\w+)*\s(.?\s)?(\d{0,3}|E\w{0,6}.?\d{0,3})\s\(?\[?(\d{3,4}p|.*)\)?\]?', path, regex.IGNORECASE).group(0)
            # regex.search('\[(\w+!?)\]|\[(\w+\-?)*\](\s\w+)*\s(.?\s)?(\d{0,3}|E\w{0,6}.?\d{0,3})\s\(?\[?(\d{3,4}p|.*)\)?\]?', path, regex.IGNORECASE).group(0)
            re.search(_header_pattern[0], stream, re.IGNORECASE).group(0)
            re.search(_tail_pattern[0], stream, re.IGNORECASE).group(0)
        except AttributeError as e:
            return status
        else:
            status = True
            if debug:
                print('{extension_engine}: {stream} :: status:{status}').format(extension_engine=self.name, stream=stream,
                                                                                status=str(status))
            return status

