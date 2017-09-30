from filemapper.datastructure.Metadata import Metadata
from filemapper.datastructure.FileFlags import FileFlags as fflags
import ShowExtension as show
import AnimeExtension as anime
import FilmExtension as film

EMPTY_WRAP = -1
BRACKET_WRAP = 0
PARENTHESIS_WRAP = 1
DASH_PARENTHESIS_WRAP = 2
EXTENSION_WRAP = 3

def eval_wrapped_key(value, wrap_type):
    '''
    This function peform auxiliary help to the build name functions validating the content of the string
    :param value: It represents the key you'regex testing
    :param wrap_type: It represents the type of wrapping the string it's going to get, numbers 0 to 2, being
                    0 for [value], 1 for (value), 2 for -(value) 3 value
    :return: modified value
    '''
    if value is None:
        return ''
    else:
        if wrap_type is 0:
            return ('[' + value + ']')
        elif wrap_type is 1:
            return ('(' + value + ')')
        elif wrap_type is 2:
            return (' - (' + value + ')')
        elif wrap_type is 3:
            return ('.' + value)
        else:
            return value

class StringBuilder():
    def __init__(self):
        self.extension_engines = [anime.AnimeExtension(), show.ShowExtension(), film.FilmExtension()]
        return

    # ADD DUMMY FLAGS FUNCTIONS! to try to remap properly

    def prettify(self, path=None):
        '''
        This function makes a name pretty
        :param path:
        :return:
        '''
        try:
            new_path = path.replace('-', ' ').replace('.', ' ').replace('_', ' ').rstrip().title()
        except Exception as e:
            return path
        else:
            return new_path

    '''
        GENERAL FUNCTIONS:
            This section of the code contains the following functions

            build_name:
    '''

    def rebuild_name(self, metadata, debug=False):
        '''
        This function rebuilds the name of a show|movie|anime from a given class Metadata Object
        :param metadata: It represents the metadata gathered from the MetadataEngine
        :param debug: It represents the debug status of the function, default it's False
        :return: NEW_NAME
        '''

        name, year, season, episode, \
        ename, quality, subtitle, language, \
        film_tag, fflag, extension = self.unpack_metadata(metadata=metadata)

        try:
            if int(fflag) == int(unicode(fflags.LIBRARY_FLAG)) \
                    or int(unicode(fflags.MAIN_SHOW_DIRECTORY_FLAG)) \
                    or int(unicode(fflags.IGNORE_FLAG)):

                return name
            else:
                for extension_engine in self.extension_engines:
                    if int(fflag) in extension_engine.supported_name_fflags:
                        return extension_engine.build_name(name=name, year=year, season=season, episode=episode, ename=ename, quality=quality, extension=extension, film_tag=film_tag, debug=debug)
                    elif int(fflag) in extension_engine.supported_subtitle_fflags:
                        return extension_engine.build_subtitle_name(name=name, year=year, season=season, episode=episode, subtitle=subtitle, language=language, extension=extension, debug=debug)
                    elif int(fflag) in extension_engine.supported_season_fflags:
                        return extension_engine.build_season_name(name=name, season=season, debug=debug)

        except:
            raise(Exception)

    def unpack_metadata(self, metadata, debug):
        '''
        This function unpacks the Metada Object
        :param metadata: It represents the metadata a class Metadata Object
        :return: name, year, season, episode, ename, quality, subs, language, film_tag, fflag, extension
        '''
        try:
            name = metadata.get_name()
            year = metadata.get_year()
            season = metadata.get_season()
            episode = metadata.get_episode()
            ename = metadata.get_ename()
            quality = metadata.get_quality()
            subtitle = metadata.get_subtitle()
            language = metadata.get_language()
            film_flag = metadata.get_film_tag()
            fflag = metadata.get_fflag()
            extension = metadata.get_extension()

            if debug:
                print (name, year, season, episode, ename, quality, subtitle, language, film_flag, fflag, extension)

            return (name, year, season, episode, ename, quality, subtitle, language, film_flag, fflag, extension)

        except:
            raise(Exception)