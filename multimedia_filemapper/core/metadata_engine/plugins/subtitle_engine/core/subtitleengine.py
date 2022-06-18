#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Note: Typing Python Modules
from typing import List, Any

# Note: Core FileMapper Modules
from multimedia_filemapper.core.constants.media_file_flags import FileFlags
from multimedia_filemapper.core.metadata_engine.core.metadataengine import Metadata
from multimedia_filemapper.core.metadata_engine.plugins.subtitle_engine.extensions.subtitlesrtassextension import \
    SubtitleSrtAssExtension


class SubtitleEngine:
    def __init__(self):
        self.name = 'SubtitleEngine'
        self.supported_file_fflags: List[FileFlags] = [
            FileFlags.SUBTITLE_ANIME_FLAG,
            FileFlags.SUBTITLE_FILM_FLAG,
            FileFlags.SUBTITLE_SHOW_FLAG
        ]
        self.supported_formats: List[str] = ['srt', 'ass']
        self.category_extension: List[Any] = [
            SubtitleSrtAssExtension()
        ]

    def map(self, stream: str, metadata: Metadata) -> Metadata:
        """
        This function maps the file or directory based on the pre-mapping done by filemapper
        :param stream: It represents the input string you're mapping
        :param metadata:
        :return: language
        """
        for extension_engine in self.category_extension:
            # Note: This will try to map the different values present in the file or directory basename
            if metadata.fflag in extension_engine.supported_subtitle_fflags:
                try:
                    metadata.language = extension_engine.get_language(stream=stream)
                    return metadata
                except Exception as error:
                    print(f'{self.__class__.__name__}.map({stream}, {metadata}): -> {error}')
                    return metadata
