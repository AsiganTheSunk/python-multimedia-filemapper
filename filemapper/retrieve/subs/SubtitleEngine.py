from filemapper.datastructure.FileFlags import FileFlags as fflags
from langdetect import DetectorFactory
from langdetect import detect
import filemapper.retrieve.regex
import chardet
import pysrt

class SubtitleEngine():
    def __init__(self):
        self.name = 'SubtitleEngine'
        self.supported_fflags = [fflags.SUBTITLE_ANIME_FLAG, fflags.SUBTITLE_FILM_FLAG, fflags.SUBTITLE_SHOW_FLAG]
        self.supported_formats = ['srt','ass']
        return