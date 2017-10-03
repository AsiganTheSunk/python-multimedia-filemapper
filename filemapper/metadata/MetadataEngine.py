import os

from filemapper.datastructure.FileFlags import FileFlags as fflags
from filemapper.metadata.Metadata import Metadata
from filemapper.metadata.imdb.IMDbEngine import IMDbEngine
from filemapper.metadata.regex.RegexEngine import RegexEngine
from filemapper.metadata.subs.SubtitleEngine import SubtitleEngine
from filemapper.metadata.tvdb.TVDbEngine import TVDbEngine


# from filemapper.metadata import FFProbeExtension as ffprobee

class MetadataEngine():
    def __init__(self):
        self.category_engine = [IMDbEngine(), TVDbEngine()]
        self.subs_engine = SubtitleEngine() #ffprobee.FFProbeExtension()
        self.regex_engine =  RegexEngine()
        return

    def map(self, stream, fflag, verbose=False, debug=False):
        '''
        This function will map the values of a given file or directory path in order to extract the metadata
        :param stream:
        :param fflag:
        :param verbose:
        :param debug:
        :return: METADATA
        '''
        metadata = Metadata()
        basename = os.path.basename(stream)
        try:
            if fflag is (fflags.LIBRARY_FLAG or fflags.MAIN_SHOW_DIRECTORY_FLAG or fflags.IGNORE_FLAG):
                return Metadata(name=basename, fflag=fflag)

            metadata = self.regex_engine.map(stream=basename, fflag=fflag, verbose=verbose, debug=debug)
            if fflag in self.subs_engine.supported_fflags:
                if metadata.get_language() is '':
                    metadata = self.subs_engine.map(stream=stream, metadata=metadata, verbose=verbose, debug=debug)

            for category_engine in self.category_engine:
                if fflag in category_engine.supported_fflags:
                    metadata = category_engine.map(metadata=metadata, verbose=verbose, debug=debug)
        except Exception as e:
            print 'ERROR HERE' + str(e)
            return Metadata()
        else:
            return metadata
