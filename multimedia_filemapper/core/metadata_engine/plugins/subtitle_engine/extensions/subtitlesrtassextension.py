from typing import List

from langdetect import DetectorFactory
from langdetect import detect

from multimedia_filemapper.core.constants.media_file_flags import FileFlags


class SubtitleSrtAssExtension:
    def __init__(self):
        self.supported_fflags = []
        self.supported_season_fflags = []
        self.supported_subtitle_fflags: List[FileFlags] = [
            FileFlags.SUBTITLE_ANIME_FLAG,
            FileFlags.SUBTITLE_FILM_FLAG,
            FileFlags.SUBTITLE_SHOW_FLAG,
        ]
        self.supported_formats = [
            'srt',
            'ass',
        ]

    @staticmethod
    def get_subtitle_sample(path: str, chunk_size: int = 60) -> str:
        """
        Function _get_subtitle_chunk
        This function opens the subtitle_engine file and extract a chunk using pysrt

        :param path: It represents the path of the subtitle_engine file
        :param chunk_size: It represents the number of lines you'regex_engine gonna metadata_engine in the chunk
        :return: SUBTITLE_CHUNK, None otherwise
        """

        subtitle_line_samples: List[str] = []
        subtitle_sample: str = ''
        try:
            with open(path, 'r', encoding='utf-8') as subtitle_file:
                subtitle_lines = [_line for _line in subtitle_file.readlines()]

                for subtitle_index, subtitle_line in enumerate(subtitle_lines[:chunk_size]):
                    _subtitle_line = subtitle_line.strip()
                    subtitle_line_samples.append(_subtitle_line)

                subtitle_sample = ' '.join(subtitle_line_samples)
                return subtitle_sample
        except Exception as error:
            return subtitle_sample

    def get_language(self, stream) -> str:
        """
        This function retrieves language from a given path using regex_engine | langdetect, firts it will try to get the
        language from the name file, if the fuction it's unable to metadata_engine this way it will try reading a chunk of
        the subtitle_engine content and detect the language using langdetect
        :param stream: It represents the input string you're parsing
        :return: LANGUAGE
        """

        language: str = ''
        DetectorFactory.seed = 0
        try:
            if stream[-3:] in self.supported_formats:
                _subtitle_sample = self.get_subtitle_sample(path=stream)
                if not _subtitle_sample:
                    pass
                else:
                    language = detect(self.get_subtitle_sample(path=stream))
            # print(f'{self.__class__.__name__}.get_language("{stream}"): -> {language}')
            return language
        except Exception as error:
            # print(f'{self.__class__.__name__}.get_language("{stream}"): -> {error}')
            return language
