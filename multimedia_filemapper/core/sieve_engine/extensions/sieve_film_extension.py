#!/usr/bin/env python3

# Importing Regex Module
import re

# Importing Multimedia FileMapper File Patterns
from multimedia_filemapper.core.sieve_engine.constants.multimedia_file_patterns import FILM_PATTERNS


class SieveFilmExtension:
    def __init__(self):
        self.name = self.__class__.__name__

    @staticmethod
    def is_film_folder(stream):
        '''
        This function checks if the stream it's a film file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        try:
            re.search(FILM_PATTERNS['file_pattern'], stream, re.IGNORECASE).group(0)
        except AttributeError:
            return False
        except Exception:
            raise Exception
        return True
