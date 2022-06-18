#!/usr/bin/env python3

# Importing Regex Module
import re

# Importing Common Patterns
from multimedia_filemapper.core.sieve_engine.constants.multimedia_file_patterns import COMMON_PATTERNS


class SieveCommonExtension:
    def __init__(self):
        self.name = self.__class__.__name__

    @staticmethod
    def check_unwanted(stream):
        '''
        This function checks if the stream it's an unwanted file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :return: BOOLEAN
        '''
        try:
            re.search(COMMON_PATTERNS['unwanted_file_extension_patterns'], stream).group(0)
        except AttributeError:
            return False
        except Exception:
            raise Exception
        return True

    @staticmethod
    def check_multimedia_extension(stream):
        '''
        This function checks if the stream it's a multimedia file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :return: BOOLEAN
        '''
        try:
            re.search(COMMON_PATTERNS['multimedia_file_extension_patterns'], stream).group(0)
        except AttributeError:
            return False
        except Exception:
            raise Exception
        return True

    @staticmethod
    def check_subtitles_extension(stream):
        '''
        This function checks if the stream it's a subtitles file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :return: BOOLEAN
        '''
        try:
            re.search(COMMON_PATTERNS['subtitle_extension_patterns'], stream).group(0)
        except AttributeError:
            return False
        except Exception:
            raise Exception
        return True

    @staticmethod
    def is_subtitle_folder(stream):
        '''
        This function checks if the stream it's a directory returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :return: BOOLEAN
        '''
        try:
            re.search(COMMON_PATTERNS['subtitle_directory_patterns'], stream, re.IGNORECASE).group(0)
        except AttributeError:
            return False
        except Exception:
            raise Exception
        return True
