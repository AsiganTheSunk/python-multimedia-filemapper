#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from re import search, IGNORECASE
from multimedia_filemapper.core.constants.media_file_flags import FileFlags


class RegexSubtitleExtension:
    def __init__(self):
        self.name = 'RegexSubtitleExtension'
        self.supported_fflags = []
        self.supported_season_fflags = []
        self.supported_subtitle_fflags: List[FileFlags] = [
            FileFlags.SUBTITLE_DIRECTORY_FILM_FLAG,
            FileFlags.SUBTITLE_FILM_FLAG,
            FileFlags.SUBTITLE_DIRECTORY_SHOW_FLAG,
            FileFlags.SUBTITLE_SHOW_FLAG,
            FileFlags.SUBTITLE_DIRECTORY_ANIME_FLAG,
            FileFlags.SUBTITLE_ANIME_FLAG,
        ]

    @staticmethod
    def get_subtitles_directory(stream: str) -> str:
        """
        This function retrieves the subtitle_directory of the file or directory from the stream using regular expresions
        :param stream: It represents the input string you're parsing
        :return: SUBTITLE_DIRECTORY
        """
        _subtitle_directory_patterns: List[str] = ['(sub\w{0,6}(?!=\!))']
        subtitle_directory: str = ''
        try:
            subtitle_directory = search(_subtitle_directory_patterns[0], stream, IGNORECASE).group(0)
            # print(f'{self.name}: {stream} :: {subtitle_directory}')
            return subtitle_directory.lower()
        except AttributeError:
            return subtitle_directory

