from filemapper.datastructure.FileFlags import FileFlags as fflags
from filemapper.retrieve.regex.RegexAnimeExtension import RegexAnimeExtension
from filemapper.retrieve.regex.RegexCommonExtension import RegexCommonExtension
from filemapper.retrieve.regex.RegexFilmExtension import RegexFilmExtension
from filemapper.retrieve.regex.RegexShowExtension import RegexShowExtension
from filemapper.retrieve.regex.RegexSubtitleExtension import RegexSubtitleExtension
from filemapper.datastructure.Metadata import Metadata

import re

def compile_pattern(patterns):
    return [re.compile(pattern) for pattern in patterns]

class RegexEngine():
    def __init__(self):
        self.name = 'ReEngine'
        self.supported_fflags = [fflags.FILM_FLAG, fflags.SHOW_FLAG, fflags.ANIME_FLAG,
                                 fflags.FILM_DIRECTORY_FLAG, fflags.SEASON_DIRECTORY_FLAG,
                                 fflags.ANIME_DIRECTORY_FLAG, fflags.SHOW_DIRECTORY_FLAG,
                                 fflags.SUBTITLE_DIRECTORY_FILM_FLAG, fflags.SUBTITLE_FILM_FLAG,
                                 fflags.SUBTITLE_DIRECTORY_SHOW_FLAG, fflags.SUBTITLE_SHOW_FLAG,
                                 fflags.SUBTITLE_DIRECTORY_ANIME_FLAG, fflags.SUBTITLE_ANIME_FLAG
                                 ]

        self.supported_formats = ['mp4','mkv','avi','flv','ogg']
        self.category_extension = [RegexFilmExtension(), RegexAnimeExtension(), RegexShowExtension()]
        self.common_extension = RegexCommonExtension()
        self.subtitle_extension = RegexSubtitleExtension()
        return


    def map(self, stream, fflag, debug=False, verbose=False):
        name = season = episode = tags = year = quality = subs = \
            acodec = vcodec = uploader = source = ''

        for extension_engine in self.category_extension:
                # This will try to map the diferent values present in the file or directory basename

                if fflag in extension_engine.supported_name_fflags:
                    try:
                        name = extension_engine.get_name(stream=stream, season_directory=False, debug=verbose)
                        episode = extension_engine.get_episode(stream=stream, debug=verbose)
                        season = extension_engine.get_season(stream=stream, debug=verbose)
                        year = extension_engine.get_year(stream=stream, debug=verbose)
                        tags = extension_engine.get_tags(stream=stream, debug=verbose)

                    except AttributeError:
                        print 'PARSING FAILED'
                        return
                    else:
                        try:
                            quality = self.common_extension.get_quality(stream=stream, debug=verbose)
                            acodec = self.common_extension.get_acodec(stream=stream, debug=verbose)
                            vcodec = self.common_extension.get_vcodec(stream=stream, debug=verbose)
                            uploader = self.common_extension.get_uploader(stream=stream, debug=verbose)
                            source = self.common_extension.get_source(stream=stream, debug=verbose)
                        except AttributeError:
                            #caputure errors!!!
                            print 'Error common flags'
                            return
                        else:
                            if debug:
                                print('{extension_engine} :: {fflag}::{stream} ::\n name:{name} episode:{episode}, '
                                      'season:{season}, year:{year} tags:{tags}, quality:{quality}\n acodec:{acodec}, '
                                      'vcodec:{vcodec}, uploader:{uploader} source:{source}' ).format(
                                    extension_engine=self.name,
                                    fflag=fflag,
                                    stream=stream,
                                    name=name,
                                    episode=episode,
                                    season=season,
                                    year=year,
                                    tags=tags,
                                    quality=quality,
                                    acodec=acodec,
                                    vcodec=vcodec,
                                    source=source,
                                    uploader=uploader)

                            return Metadata(name=name, episode=episode, season=season, year=year, film_tag=tags,
                                            quality=quality, acodec=acodec, vcodec=vcodec, source=source,
                                            uploader=uploader)

                elif fflag in extension_engine.supported_season_fflags:
                    try:
                        name = extension_engine.get_name(stream=stream, season_directory=True, debug=verbose)
                        season = extension_engine.get_season(stream=stream, season_directory=True, debug=verbose)
                    except AttributeError:
                        print 'PARSING FAILED'
                        return
                    else:
                        try:
                            quality = self.common_extension.get_quality(stream=stream, debug=verbose)
                            # acodec = self.common_engine.get_acodec(stream=stream, debug=debug)
                            # vcodec = self.common_engine.get_vcodec(stream=stream, debug=debug)
                            # uploader = self.common_engine.get_uploader(stream=stream, debug=debug)
                            # source = self.common_engine.get_source(stream=stream)
                        except AttributeError:
                            #caputure errors!!!
                            return
                        else:
                            if debug:
                                print('{extension_engine} :: {fflag}::{stream} ::\n name:{name}'
                                      'season:{season}, quality:{quality} tags:{tags}, subs:{subs}').format(
                                    extension_engine=self.name,
                                    fflag=fflag,
                                    stream=stream,
                                    name=name,
                                    season=season,
                                    quality=quality)

                            return Metadata(name=name, season=season, quality=quality)

                elif fflag in extension_engine.supported_subtitle_fflags:
                    try:
                        name = extension_engine.get_name(stream=stream, season_directory=False, debug=verbose)
                        episode = extension_engine.get_episode(stream=stream, debug=verbose)
                        season = extension_engine.get_season(stream=stream, debug=verbose)
                        year = extension_engine.get_year(stream=stream, debug=verbose)
                        tags = extension_engine.get_tags(stream=stream, debug=verbose)

                    except AttributeError:
                        print 'PARSING FAILED'
                        return
                    else:
                        try:
                            subs = self.subtitle_extension.get_subtitles_directory(stream=stream, debug=verbose)
                        except AttributeError:
                            # caputure errors!!!
                            return
                        else:
                            if debug:
                                print('{extension_engine} :: {fflag}::{stream} ::\n name:{name} episode:{episode}, '
                                      'season:{season}, year:{year} tags:{tags}, subs:{subs}').format(extension_engine=self.name,
                                                                                                         fflag=fflag,
                                                                                                         stream=stream,
                                                                                                         name=name,
                                                                                                         episode=episode,
                                                                                                         season=season,
                                                                                                         year=year,
                                                                                                         tags=tags,
                                                                                                         subs=subs)

                            return Metadata(name=name, episode=episode, season=season, year=year, film_tag=tags, subtitle=subs)
        return