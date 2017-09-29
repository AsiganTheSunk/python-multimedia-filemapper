from filemapper.datastructure.FileFlags import FileFlags as fflags
import re

def compile_patterns(patterns):
    return [re.compile(pattern) for pattern in patterns]

class ReEngine():
    def __init__(self):
        self.name = 'ReExtension'
        self.supported_fflags = [fflags.FILM_FLAG, fflags.SHOW_FLAG, fflags.ANIME_FLAG,
                                 fflags.FILM_DIRECTORY_FLAG, fflags.SEASON_DIRECTORY_FLAG,
                                 fflags.ANIME_DIRECTORY_FLAG, fflags.SHOW_DIRECTORY_FLAG]

        self.supported_formats = ['mp4','mkv','avi','flv','ogg']
        return


