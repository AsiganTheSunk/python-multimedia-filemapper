#!/usr/bin/env python3

# Importing Multimedia FileMapper File Patterns
from multimedia_filemapper.core.sieve_engine.constants.multimedia_file_patterns import FILM_PATTERNS
from multimedia_filemapper.core.sieve_engine.constants.multimedia_file_patterns import SHOW_PATTERNS
from multimedia_filemapper.core.sieve_engine.constants.multimedia_file_patterns import ANIME_PATTERNS
from multimedia_filemapper.core.sieve_engine.constants.multimedia_file_patterns import COMMON_PATTERNS

# Importing Multimedia FileMapper SieveEngine Extensions
from multimedia_filemapper.core.sieve_engine.extensions.sieve_film_extension import SieveFilmExtension
from multimedia_filemapper.core.sieve_engine.extensions.sieve_show_extension import SieveShowExtension
from multimedia_filemapper.core.sieve_engine.extensions.sieve_anime_extension import SieveAnimeExtension
from multimedia_filemapper.core.sieve_engine.extensions.sieve_common_extension import SieveCommonExtension

# Importing Custom Logger & Logging Modules
from multimedia_filemapper.logger.custom_logger import CustomLogger
from logging import INFO, DEBUG, WARNING
import logging


class SieveEngine:
    def __init__(self, logging_lvl=INFO):
        self.name = self.__class__.__name__

        self._film_patterns = FILM_PATTERNS
        self._show_patterns = SHOW_PATTERNS
        self._anime_patterns = ANIME_PATTERNS
        self._common_patterns = COMMON_PATTERNS

        self.logger = CustomLogger(name=__name__, level=logging_lvl)

        # CustomLogger Format Definition
        formatter = logging.Formatter(fmt='%(asctime)s - [%(levelname)s]: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        # Custom Logger File Configuration: File Init Configuration
        file_handler = logging.FileHandler('./multimedia_filemapper/log/engine/sieve_engine.log', 'w')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level=logging_lvl)

        # Custom Logger Console Configuration: Console Init Configuration
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level=logging_lvl)

        # Custom Logger Console/File Handler Configuration
        self.logger.addHandler(file_handler)
        # self.logger.addHandler(console_handler)

        self.show_extension = SieveShowExtension()
        self.film_extension = SieveFilmExtension()
        self.anime_extension = SieveAnimeExtension()
        self.common_extension = SieveCommonExtension()

    def is_multimedia_folder(self, stream):
        """
        This function maps the file or directory based on the pre-mapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        """
        _status: bool = False
        try:
            _is_anime_folder = self.anime_extension.is_anime_folder(stream=stream)
            _is_season_folder = self.show_extension.is_season_folder(stream=stream)
            _is_show_folder = self.show_extension.is_show_folder(stream=stream)
            _is_film_folder = self.film_extension.is_film_folder(stream=stream)
            _is_subtitle_folder = self.common_extension.is_subtitle_folder(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if all([_is_anime_folder, _is_show_folder, _is_season_folder, _is_film_folder, _is_subtitle_folder]):
                _status = False
            # if anime_status or show_status or season_status or film_status or subs_status:
            #     status = False
            else:
                _status = True

            # self.logger.info('{0}: {1} CheckMainDirectory [ {2} ]'.format(self.name, stream, _status))
            # self.logger.debug('- anime_directory_pattern: {0}, season_directory_pattern: {1}, show_directory_pattern: {2}'.format(str(_is_anime_folder), str(_is_season_folder), str(_is_show_folder)))
            # self.logger.debug('- film_directory_pattern: {0}, subtitles_directory_pattern: {1}'.format(str(_is_film_folder), str(_is_subtitle_folder)))
            # print(f'is_multimedia_folder: {stream} :: {_status}')
            return _status

    def check_show_subtitles(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''
        try:
            show_status = self.show_extension.check_show(stream=stream)
            subs_status = self.common_extension.check_subtitles_extension(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if show_status and subs_status:
                status = True
            else:
                status = False

            self.logger.info('{0}: {1} CheckShowSubtitle [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - show_pattern: {0}, subtitles_extension_pattern: {1}'.format(show_status, subs_status))
            return status

    def is_show_subtitle_folder(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''
        try:
            show_directory_status = self.show_extension.check_show(stream=stream)
            subs_status = self.common_extension.is_subtitle_folder(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if subs_status and show_directory_status:
                status = True
            else:
                status = False

            self.logger.info('{0}: {1} CheckShowSubtitlesDirectory [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - show_directory_pattern: {0}, subtitles_directory_pattern:{1}'.format(show_directory_status, subs_status))
            return status

    def check_anime_subtitles(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''
        try:
            anime_status = self.anime_extension.check_anime_subtitles(stream=stream)
            subs_status = self.common_extension.check_subtitles_extension(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if anime_status and subs_status:
                status = True
            else:
                status = False
            self.logger.info('{0}: {1} CheckAnimeSubtitles [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - anime_subtitles_pattern: {0}, subtitles_extension_pattern: {1}'.format(anime_status, subs_status))
            return status

    def is_anime_subtitle_folder(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''
        try:
            anime_directory_status = self.anime_extension.is_anime_folder(stream=stream)
            subs_status = self.common_extension.is_subtitle_folder(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if anime_directory_status and subs_status:
                status = True
            else:
                status = False
                self.logger.info('{0}: {1} CheckAnimeSubtitlesDirectory {2}'.format(self.name, stream, status))
                self.logger.debug(' - anime_directory_pattern: {0}, subtitle_directory_pattern: {1}'.format(anime_directory_status, subs_status))
            return status

    def is_film_subtitle_folder(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''
        try:
            film_status = self.film_extension.is_film_folder(stream=stream)
            subs_directory_status = self.common_extension.is_subtitle_folder(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if film_status and subs_directory_status:
                status = True
            else:
                status = False

            self.logger.info('{0}: {1} CheckFilmSubtitlesDirectory [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - film_pattern: {0}, subtitles_directory_pattern: {1}'.format(film_status, subs_directory_status))
            return status

    def check_film_subtitles(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''
        try:
            film_status = self.film_extension.is_film_folder(stream=stream)
            subs_status = self.common_extension.check_subtitles_extension(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if film_status and subs_status:
                status = True
            else:
                status = False
            self.logger.info('{0}: {1} CheckFilmSubtitles [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - film_pattern: {0}, subtitles_extension_pattern: {1}'.format(film_status, subs_status))
            return status

    def is_anime_folder(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''

        try:
            anime_directory_status = self.anime_extension.is_anime_folder(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if anime_directory_status:
                status = True
            else:
                status = False
            self.logger.info('{0}: {1} CheckAnimeDirectory [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - anime_directory_pattern: {0}'.format(anime_directory_status))
            return status

    def check_film(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''
        try:
            film_status = self.film_extension.is_film_folder(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if film_status:
                status = True
            else:
                status = False
            self.logger.info('{0}: {1} CheckFilm [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - film_pattern: {0}'.format(film_status))
            return status

    def check_show(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''
        try:
            show_status = self.show_extension.check_show(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if show_status:
                status = True
            else:
                status = False
            self.logger.info('{0}: {1} CheckShow [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - show_pattern: {0}'.format(show_status))
            return status

    def check_anime(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''
        try:
            anime_status = self.anime_extension.check_anime_show(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if anime_status:
                status = True
            else:
                status = False
            self.logger.info('{0}: {1} CheckAnime [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - anime_pattern: {0}'.format(anime_status))
            return status

    def is_season_folder(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''
        try:
            season_status = self.show_extension.is_season_folder(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if season_status:
                status = True
            else:
                status = False
            self.logger.info('{0}: {1} CheckSeasonDirectory [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - season_directory_pattern: {0}'.format(season_status))
            return status

    def is_show_folder(self, stream):
        # Añadir Clausula de os.path.isdir() o os.path.isfile() para el caso apropiado?
        # Mantener la disposicion actual, desde el modulo Core.
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :return: BOOLEAN
        '''
        try:
            show_directory_status = self.show_extension.is_show_folder(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if show_directory_status:
                status = True
            else:
                status = False
            self.logger.info('{0}: {1} CheckShowDirectory [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - show_directory_pattern: {0}'.format(show_directory_status))
            return status

    def check_unwanted(self, stream):
        '''
        This function maps the file or directory based on the premapping done by sieve_engine engine
        :param stream: It represents the input string you're mapping
        :param debug: It represents the debug status of the function, default it's False
        :return: BOOLEAN
        '''
        try:
            unwanted_status = self.common_extension.check_unwanted(stream=stream)
        except Exception as err:
            self.logger.fatal(err)
            return
        else:
            if unwanted_status:
                status = True
            else:
                status = False
            self.logger.info('{0}: {1} CheckUnWanted: [ {2} ]'.format(self.name, stream, status))
            self.logger.debug(' - unwanted_file_pattern: {0}'.format(unwanted_status))
            return status
