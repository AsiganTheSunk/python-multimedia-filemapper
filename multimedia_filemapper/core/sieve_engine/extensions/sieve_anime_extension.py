#!/usr/bin/env python3
# coding=utf-8

# TODO No recuerdo para que servian estas, revisar en un futuro!.
# regex_engine.search('\[(\w+-?)*\](\s\w+)*\s(.?\s)?(\d{0,3}|E\w{0,6}.?\d{0,3})\s\(?\[?(\d{3,4}p|.*)\)?\]?', path, regex_engine.IGNORECASE).group(0)
# regex_engine.search('\[(\w+!?)\]|\[(\w+\-?)*\](\s\w+)*\s(.?\s)?(\d{0,3}|E\w{0,6}.?\d{0,3})\s\(?\[?(\d{3,4}p|.*)\)?\]?', path, regex_engine.IGNORECASE).group(0)

# Importing Regex Module
import re

# Importing Multimedia FileMapper File Patterns
from multimedia_filemapper.core.sieve_engine.constants.multimedia_file_patterns import ANIME_PATTERNS
from multimedia_filemapper.core.sieve_engine.constants.multimedia_file_patterns import COMMON_PATTERNS


class SieveAnimeExtension:
    def __init__(self):
        self.name = self.__class__.__name__

    @staticmethod
    def check_anime_subtitles(stream):
        '''
        This function checks if the stream it's a anime file returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :return: BOOLEAN
        '''
        try:
            re.search(ANIME_PATTERNS['anime_show_pattern']['head_pattern'], stream, re.IGNORECASE).group(0)
            re.search(ANIME_PATTERNS['anime_show_pattern']['tail_pattern'], stream, re.IGNORECASE).group(0)
        except AttributeError:
            return False
        except Exception:
            raise Exception
        return True

    @staticmethod
    def check_anime_show(stream):
        '''
        This function checks if the stream it's a anime show returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :return: BOOLEAN
        '''
        try:
            re.search(ANIME_PATTERNS['anime_show_pattern']['full_pattern'], stream, re.IGNORECASE).group(0)
        except AttributeError:
            try:
                re.search(ANIME_PATTERNS['anime_show_pattern']['head_pattern'], stream, re.IGNORECASE).group(0)
                re.search(ANIME_PATTERNS['anime_show_pattern']['tail_pattern'], stream, re.IGNORECASE).group(0)
                re.search(COMMON_PATTERNS['multimedia_file_extension_patterns'], stream, re.IGNORECASE).group(0)
            except AttributeError:
                return False
            except Exception:
                raise Exception
            else:
                return True
        return True

    @staticmethod
    def is_anime_folder(stream):
        """
        This function checks if the stream it's anime directory returning True, otherwise False
        :param stream: It represents the input string you're parsing
        :return: BOOLEAN
        """
        try:
            re.search(ANIME_PATTERNS['anime_show_pattern']['head_pattern'], stream, re.IGNORECASE).group(0)
            re.search(ANIME_PATTERNS['anime_show_pattern']['tail_pattern'], stream, re.IGNORECASE).group(0)
        except AttributeError:
            return False
        except Exception:
            raise Exception
        return True
