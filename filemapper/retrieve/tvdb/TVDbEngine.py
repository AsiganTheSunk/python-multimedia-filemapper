from filemapper.datastructure.FileFlags import FileFlags as fflags

class TVDbEngine():
    def __init__(self):
        self.name = 'TVDbEngine'
        self.supported_fflags = [fflags.SHOW_FLAG, fflags.SHOW_DIRECTORY_FLAG, fflags]
        return
