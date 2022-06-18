#!/usr/bin/env python3

# Importing OS Path Functions
import os

# Importing Multimedia FileMapper Metadata Object
from multimedia_filemapper.core.metadata_engine.struct_data.metadata import Metadata

# Importing Multimedia FileMapper Regex Plugin
from multimedia_filemapper.core.metadata_engine.plugins.regex_engine.core.regexengine import RegexEngine

# Importing Multimedia FileMapper Media DB Plugins
from multimedia_filemapper.core.metadata_engine.plugins.imdb_engine.core.imdbengine import IMDbEngine
from multimedia_filemapper.core.metadata_engine.plugins.tvdb_engine.core.tvdbengine import TVDbEngine

# Importing Multimedia FileMapper Subtitles Plugin
from multimedia_filemapper.core.metadata_engine.plugins.subtitle_engine.core.subtitleengine import SubtitleEngine

# Importing Multimedia FileMapper Constants
from multimedia_filemapper.core.constants.media_file_flags import FileFlags


class MetadataEngine:
    def __init__(self):
        # self.category_engine = [IMDbEngine(), TVDbEngine()]
        self.category_engine = []
        self.subs_engine = SubtitleEngine()
        self.regex_engine = RegexEngine()

    def map(self, stream, fflag):
        """
        This function will map the values of a given file or directory path in
        order to extract the metadata_engine
        :param stream:
        :param fflag:
        :param verbose:
        :param debug:
        :return: METADATA
        """

        try:
            if fflag in (FileFlags.LIBRARY_FLAG, FileFlags.MAIN_SHOW_DIRECTORY_FLAG,
                         FileFlags.IGNORE_FLAG, FileFlags.UNKOWN_FLAG):

                return Metadata(name=stream, fflag=fflag)

            metadata = self.regex_engine.map(stream=stream, fflag=fflag)
            if fflag in self.subs_engine.supported_file_fflags:
                if metadata.language == '':
                    metadata = self.subs_engine.map(stream=stream, metadata=metadata)

            # Bug: This FAILS API_Key Required
            # for category_engine in self.category_engine:
            #     if fflag in category_engine.supported_fflags:
            #         metadata = category_engine.map(metadata=metadata, verbose=verbose, debug=debug)
        except Exception as e:
            print('MetadataEngine Error Here' + str(e))
            return Metadata()
        else:
            return metadata
