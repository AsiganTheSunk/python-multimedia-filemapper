import re

from multimedia_filemapper.core.constants.media_file_flags import FileFlags as fflags, FileFlags
from multimedia_filemapper.core.metadata_engine.plugins.subtitle_engine.extensions.subtitlesrtassextension import \
    SubtitleSrtAssExtension
from multimedia_filemapper.core.metadata_engine.struct_data.metadata import Metadata
from multimedia_filemapper.core.metadata_engine.plugins.regex_engine.extensions.regexanimeextension \
    import RegexAnimeExtension
from multimedia_filemapper.core.metadata_engine.plugins.regex_engine.extensions.regexcommonextension \
    import RegexCommonExtension
from multimedia_filemapper.core.metadata_engine.plugins.regex_engine.extensions.regexfilmextension \
    import RegexFilmExtension
from multimedia_filemapper.core.metadata_engine.plugins.regex_engine.extensions.regexshowextension \
    import RegexShowExtension
from multimedia_filemapper.core.metadata_engine.plugins.regex_engine.extensions.regexsubtitleextension \
    import RegexSubtitleExtension

from os.path import basename

def compile_pattern(patterns):
    return [re.compile(pattern) for pattern in patterns]


class RegexEngine:
    def __init__(self):
        self.name = 'RegexEngine'
        self.supported_fflags = [
            fflags.FILM_FLAG,
            fflags.SHOW_FLAG,
            fflags.ANIME_FLAG,
            fflags.FILM_DIRECTORY_FLAG,
            fflags.SEASON_DIRECTORY_FLAG,
            fflags.ANIME_DIRECTORY_FLAG,
            fflags.SHOW_DIRECTORY_FLAG,
            fflags.SUBTITLE_DIRECTORY_FILM_FLAG,
            fflags.SUBTITLE_FILM_FLAG,
            fflags.SUBTITLE_DIRECTORY_SHOW_FLAG,
            fflags.SUBTITLE_SHOW_FLAG,
            fflags.SUBTITLE_DIRECTORY_ANIME_FLAG,
            fflags.SUBTITLE_ANIME_FLAG
        ]
        self.category_extension = [
            RegexFilmExtension(),
            RegexAnimeExtension(),
            RegexShowExtension()
        ]
        self.common_extension = RegexCommonExtension()
        self.subtitle_extension = RegexSubtitleExtension()

    def map(self, stream, fflag):
        """
        This function maps the file or directory based on the premapping done by filemapper
        :param stream: It represents the input string you're mapping
        :param fflag: It represents the fflag of the file or directory your mapping
        :return: Metadata
        """

        for extension_engine in self.category_extension:
            if fflag in extension_engine.supported_fflags:
                _stream = basename(stream)
                print(f'>: Reviewing Film|Anime|Show Folder|File :: {stream} with {fflag}')
                try:
                    name = extension_engine.get_name(stream=_stream, season_directory=False)
                    episode = extension_engine.get_episode(stream=_stream)
                    season = extension_engine.get_season(stream=_stream)
                    year = extension_engine.get_year(stream=_stream)
                    tags = extension_engine.get_tags(stream=_stream)
                    quality = self.common_extension.get_quality(stream=_stream)
                    acodec = self.common_extension.get_acodec(stream=_stream)
                    vcodec = self.common_extension.get_vcodec(stream=_stream)
                    uploader = self.common_extension.get_uploader(stream=_stream)
                    source = self.common_extension.get_source(stream=_stream)
                    extension = self.common_extension.get_extension(stream=_stream)
                    return Metadata(name=name, episode=episode,
                                    season=season, year=year, film_tag=tags,
                                    quality=quality, acodec=acodec,
                                    vcodec=vcodec, source=source,
                                    uploader=uploader, fflag=fflag,
                                    extension=extension)
                except Exception as error:
                    print(f'Reviewing Film|Anime|Show Folder|File :: ERROR: {error}')

            elif fflag in extension_engine.supported_season_fflags:
                print(f'>: Reviewing Season Folder {stream} with {fflag}')
                _stream = basename(stream)
                try:
                    name = extension_engine.get_name(stream=_stream, season_directory=True)
                    season = extension_engine.get_season(stream=_stream, season_directory=True)
                    quality = self.common_extension.get_quality(stream=_stream)
                    return Metadata(name=name, season=season, quality=quality, fflag=fflag)
                except Exception as error:
                    print(f'>: Reviewing Anime|Show Season Folder :: ERROR: {error}')

            elif fflag in extension_engine.supported_subtitle_fflags:
                print(f'>: Reviewing Subtitle Folder|File ( {fflag} ) :: {stream}')
                _language: str = ''
                _stream = basename(stream)
                _name: str = ''
                _episode: str = ''
                _season: str = ''
                _year: str = ''
                _tags: str = ''
                _quality: str = ''
                try:
                    # Note: Common and Subtitle Extensions
                    _name = self.subtitle_extension.get_subtitles_directory(stream=_stream)
                    _subs = self.subtitle_extension.get_subtitles_directory(stream=stream)
                    _acodec = self.common_extension.get_acodec(stream=_stream)
                    _vcodec = self.common_extension.get_vcodec(stream=_stream)
                    _uploader = self.common_extension.get_uploader(stream=_stream)
                    _source = self.common_extension.get_source(stream=_stream)
                    _extension = self.common_extension.get_extension(stream=_stream)
                    if fflag is fflags.SUBTITLE_FILM_FLAG:
                        len_aux = len(_stream)
                        _directory_basename = basename(stream[:(-len(_subs) - 1 - len_aux - 1)])
                        # print(_stream, 'HERE ::', _directory_basename, 'DETECTED SUB DIRECTORY ::', _subs)

                        # Note: Film|Anime|Show Extension
                        _name = extension_engine.get_name(stream=_directory_basename, season_directory=False)
                        _episode = extension_engine.get_episode(stream=_directory_basename)
                        _season = extension_engine.get_season(stream=_directory_basename)
                        _year = extension_engine.get_year(stream=_directory_basename)
                        _tags = extension_engine.get_tags(stream=_directory_basename)
                        _quality = self.common_extension.get_quality(stream=_directory_basename)
                        _language = self.common_extension.get_language(stream=_stream)
                        if not _language:
                            subtitle_language_module = SubtitleSrtAssExtension()
                            _language = subtitle_language_module.get_language(stream=stream)

                    _new_metadata = Metadata(
                        name=_name, episode=_episode, quality=_quality,
                        acodec=_acodec, vcodec=_vcodec, uploader=_uploader,
                        source=_source, season=_season, year=_year,
                        film_tag=_tags, subtitle=_subs, fflag=fflag,
                        language=_language, extension=_extension
                    )
                    # print(f'{self.name} :: {fflag}::{stream} :: \n name:{name} episode:{episode}, '
                    #       f'season:{season}, year:{year} tags:{tags}, language:{language}, extensions:{extension}')
                    return _new_metadata
                except Exception as error:
                    print(f'>: Reviewing Subtitle Folder|File ERROR: {error}')

