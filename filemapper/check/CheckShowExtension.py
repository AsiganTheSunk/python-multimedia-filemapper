import re


class CheckShowExtension():
    def __init__(self):
        self.name = 'CheckShowExtension'
        return

    def check_show_directory(self, stream, debug=False):
        '''
        This function checks if the stream it's a show directory returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        status = False
        _show_directory_pattern = [
            '(\w+.+)([s]\d{1,3}[e]\d{1,3}).?(?=(\d{3,4}p)?).*(\[.*\])?']
        try:
            re.search(_show_directory_pattern[0], stream, re.IGNORECASE).group(
                0)
        except AttributeError:
            return status
        else:
            status = True
            if debug:
                print('{extension_engine}: {stream} :: status:{status}').format(
                    extension_engine=self.name,
                    stream=stream,
                    status=str(status))
            return status

    def check_show(self, stream, debug=False):
        '''
        This function checks if the stream it's a show file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        status = False
        _show_pattern = ['([s]\d{1,2}[e]\d{1,2})']
        try:
            re.search(_show_pattern[0], stream, re.IGNORECASE).group(0)
        except AttributeError:
            return status
        else:
            status = True
            if debug:
                print('{extension_engine}: {stream} :: status:{status}').format(
                    extension_engine=self.name,
                    stream=stream,
                    status=str(status))
            return status

    def check_season_directory(self, stream, debug=False):
        '''
        This function checks if the stream it's a show season directory returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        _season_directory_pattern = [
            '(\-|\s|\.)(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?']
        status = False
        try:
            re.search(_season_directory_pattern[0], stream,
                      re.IGNORECASE).group(0)
        except AttributeError:
            return status
        else:
            status = True
            if debug:
                print('{extension_engine}: {stream} :: status:{status}').format(
                    extension_engine=self.name,
                    stream=stream,
                    status=str(status))
            return status
