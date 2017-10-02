from filemapper.check.CheckAnimeExtension import CheckAnimeExtension
from filemapper.check.CheckShowExtension import CheckShowExtension
from filemapper.check.CheckCommonExtension import CheckCommonExtension
from filemapper.check.CheckFilmExtension import CheckFilmExtension

class CheckEngine():
    def __init__(self):
        self.name = 'CheckEngine'
        self.show_engine = CheckShowExtension()
        self.film_engine = CheckFilmExtension()
        self.anime_engine = CheckAnimeExtension()
        self.common_engine = CheckCommonExtension()
        return

    def check_main_directory(self, stream, verbose=False, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :param verbose: It represents the verbose status of the function, default it's False
        :return: BOOLEAN
        '''
        try:

            anime_status = self.anime_engine.check_anime_directory(stream=stream, debug=verbose)
            season_status = self.show_engine.check_season_directory(stream=stream, debug=verbose)
            show_status = self.show_engine.check_show_directory(stream=stream, debug=verbose)
            film_status = self.film_engine.check_film(stream=stream, debug=verbose)
            subs_status = self.common_engine.check_subtitles_directory(stream=stream, debug=verbose)
        except Exception as e:
            print 'Exception' + str(e)
            return
        else:
            if anime_status or show_status or season_status or film_status or subs_status:
                status = False
            else:
                status = True
            if debug:
                print('{engine}: {stream} :: status:{status}\n anime_directory:{anime_status}, '
                      'season_directory:{season_status}, show_directory:{show_status}, film_directory:{film_status}, '
                      'subs_directory:{subs_status}').format(engine=self.name, stream=stream, status=status,
                                                             anime_status=str(anime_status),
                                                             season_status=str(season_status),
                                                             show_status=str(show_status),
                                                             film_status=str(film_status),
                                                             subs_status=str(subs_status))

            return status

    def check_show_subtitles(self, stream, verbose=False, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :param verbose: It represents the verbose status of the function, default it's False
        :return: BOOLEAN
        '''
        try:
            show_status = self.show_engine.check_show(stream=stream, debug=verbose)
            subs_status = self.common_engine.check_subtitles(stream=stream, debug=verbose)
        except Exception as e:
            print 'Exception' + str(e)
            return
        else:
            if show_status and subs_status:
                status = True
            else:
                status = False

            if debug:
                print('{engine}: {stream} :: status:{status}\n show:{show_status}, subs:{subs_status}').format(
                    engine=self.name,
                    stream=stream,
                    status=status,
                    show_status=show_status,
                    subs_status=subs_status)

            return status

    def check_show_subtitles_directory(self, stream, verbose=False, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :param verbose: It represents the verbose status of the function, default it's False
        :return: BOOLEAN
        '''
        try:
            show_directory_status = self.show_engine.check_show(stream=stream, debug=verbose)
            subs_status = self.common_engine.check_subtitles_directory(stream=stream, debug=verbose)
        except Exception as e:
            print 'Exception' + str(e)
            return
        else:
            if subs_status and show_directory_status:
                status = True
            else:
                status = False

            if debug:
                print('{engine}: {stream} :: status:{status}\n show_directory:{show_directory_status}, subs:{subs_status}').format(
                    engine=self.name,
                    stream=stream,
                    status=status,
                    show_directory_status=show_directory_status,
                    subs_status=subs_status)

            return status

    def check_anime_subtitles(self, stream, verbose=False, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :param verbose: It represents the verbose status of the function, default it's False
        :return: BOOLEAN
        '''
        try:
            anime_status = self.anime_engine.check_anime_show2(stream=stream, debug=verbose)
            subs_status = self.common_engine.check_subtitles(stream=stream, debug=verbose)
        except Exception as e:
            print e
            return
        else:
            if anime_status and subs_status:
                status = True
            else:
                status = False
            if debug:
                print('{engine}: {stream} :: status:{status}\n anime:{anime_status}, subs:{subs_status}').format(
                    engine=self.name,
                    stream=stream,
                    status=status,
                    anime_status=anime_status,
                    subs_status=subs_status)

            return status

    def check_anime_subtitles_directory(self, stream, verbose=False, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :param verbose: It represents the verbose status of the function, default it's False
        :return: BOOLEAN
        '''
        try:
            anime_directory_status = self.anime_engine.check_anime_directory(stream=stream, debug=verbose)
            subs_status = self.common_engine.check_subtitles_directory(stream=stream, debug=verbose)
        except Exception as e:
            print 'Exception' + str(e)
            return
        else:
            if anime_directory_status and subs_status:
                status = True
            else:
                status = False
            if debug:
                print('{engine}: {stream} :: status:{status}\n anime:{anime_directory_status}, subs:{subs_status}').format(
                    engine=self.name,
                    stream=stream,
                    status=status,
                    anime_directory_status=anime_directory_status,
                    subs_status=subs_status)

            return status

    def check_film_subtitles_directory(self, stream, verbose=False, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :param verbose: It represents the verbose status of the function, default it's False
        :return: BOOLEAN
        '''
        try:
            film_status = self.film_engine.check_film(stream=stream, debug=verbose)
            subs_directory_status = self.common_engine.check_subtitles_directory(stream=stream, debug=verbose)
        except Exception as e:
            print 'Exception' + str(e)
            return
        else:
            if film_status and subs_directory_status:
                status = True
            else:
                status = False
            if debug:
                print('{engine}: {stream} :: status:{status}\n film:{film_status}, subs_directory:{subs_directory_status}').format(
                    engine=self.name,
                    stream=stream,
                    status=status,
                    film_status=film_status,
                    subs_directory_status=subs_directory_status)

            return status

    def check_film_subtitles(self, stream, verbose=False, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :param verbose: It represents the verbose status of the function, default it's False
        :return: BOOLEAN
        '''
        try:
            film_status = self.film_engine.check_film(stream=stream, debug=verbose)
            subs_status = self.common_engine.check_subtitles(stream=stream, debug=verbose)
        except Exception as e:
            print 'Exception' + str(e)
            return
        else:
            if film_status and subs_status:
                status = True
            else:
                status = False
            if debug:
                print('{engine}: {stream} :: status:{status}\n film:{film_status}, subs:{subs_status}').format(
                    engine=self.name,
                    stream=stream,
                    status=status,
                    film_status=film_status,
                    subs_status=subs_status)

            return status

    def check_film(self, stream, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        return self.film_engine.check_film(stream=stream, debug=debug)

    def check_show(self, stream, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        return self.show_engine.check_show(stream=stream, debug=debug)

    def check_anime(self, stream, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        return self.anime_engine.check_anime_show(stream=stream, debug=debug)


    def check_anime_directory(self, stream, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        return self.anime_engine.check_anime_directory(stream=stream, debug=debug)

    def check_season_directory(self, stream, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        return self.show_engine.check_season_directory(stream=stream, debug=debug)

    def check_show_directory(self, stream, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        return self.show_engine.check_show_directory(stream=stream, debug=debug)


    def check_unwanted(self, stream, debug=False):
        '''
        This function maps the file or directory based on the premapping done by check engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        return self.common_engine.check_unwanted(stream=stream, debug=debug)