import re


class CheckFilmExtension():
    def __init__(self):
        self.name = 'CheckFilmExtension'
        return

    def check_film(self, stream, debug=False):
        '''
        This function checks if the stream it's a film file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        status = False
        _film_pattern = ['(.*)(([1-2])([890])(\d{2}))(?!p)']
        try:
            re.search(_film_pattern[0], stream, re.IGNORECASE).group(0)
        except AttributeError:
            return status
        else:
            status = True
            if debug:
                print('{extension}: {stream} :: status:{status}').format(extension=self.name, stream=stream,
                                                                         status=str(status))
            return status
