class StringUtils:
    def __init__(self):
        return

    @staticmethod
    def eval_wrapped_key(value, wrap_type):
        """
        This function perform auxiliary help to the build name functions validating the content of the string
        :param value: It represents the key for regex_engine testing
        :param wrap_type: It represents the type of wrapping the string it's going to get, numbers 0 to 2, being
                        0 for [value], 1 for (value), 2 for -(value) 3 value
        :return: modified value
        """

        if value is None:
            return ''
        else:
            if wrap_type == -1:
                if value == '':
                    return ''
                return ' ' + value
            elif wrap_type == 0:
                if value == '':
                    return value
                return ' [' + value + ']'
            elif wrap_type == 1:
                if value == '':
                    return value
                return ' (' + value + ')'
            elif wrap_type == 2:
                if value == '':
                    return value
                return ' - (' + value + ')'
            elif wrap_type == 3:
                if value == '':
                    return value
                return '.' + value
            elif wrap_type == 4:
                if value == '':
                    return value
                return ' - ' + value
            else:
                return value
