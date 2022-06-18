#!/usr/bin/env python3

# Importing Regex Module
import re

# Importing Multimedia FileMapper File Patterns
from multimedia_filemapper.core.sieve_engine.constants.multimedia_file_patterns import SHOW_PATTERNS


class SieveShowExtension:
    def __init__(self):
        self.name = self.__class__.__name__

    @staticmethod
    def is_show_folder(stream):
        '''
        This function checks if the stream it's a show directory returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :return: BOOLEAN
        '''
        try:
            re.search(SHOW_PATTERNS['file_pattern'], stream, re.IGNORECASE).group(0)
        except AttributeError:
            return False
        except Exception:
            raise Exception
        return True

    @staticmethod
    def check_show(stream):
        '''
        This function checks if the stream it's a show file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :return: BOOLEAN
        '''
        try:
            re.search(SHOW_PATTERNS['season_episode_pattern'], stream, re.IGNORECASE).group(0)
        except AttributeError:
            return False
        except Exception:
            raise Exception
        return True

    @staticmethod
    def is_season_folder(stream):
        '''
        This function checks if the stream it's a show season directory returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :return: BOOLEAN
        '''
        try:
            re.search(SHOW_PATTERNS['season_directory_pattern'], stream, re.IGNORECASE).group(0)
        except AttributeError:
            return False
        except Exception:
            raise Exception
        return True
