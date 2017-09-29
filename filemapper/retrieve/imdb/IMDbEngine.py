from filemapper.datastructure.FileFlags import FileFlags as fflags

class IMDbEngine():
    def __init__(self):
        self.name = 'IMDbExtension'
        self.supported_fflags = [fflags.FILM_FLAG, fflags.SHOW_FLAG]
        self.support_formats = []
        return
