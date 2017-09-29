from filemapper.retrieve.imdb import IMDbEngine as imdbe
from filemapper.retrieve.regex import ReEngine as ree
from filemapper.retrieve.subs import SubtitleEngine as subte
from filemapper.retrieve.tvdb import TVDbEngine as tvdbe


# from filemapper.retrieve import FFProbeExtension as ffprobee

class MetadataEngine():
    def __init__(self):
        self.extension_engines = [imdbe.IMDbExtension(), tvdbe.TVDbExtension(), subte.SubtitleExtension(), ree.ReEngine()] #ffprobee.FFProbeExtension()

        return
    #
    # def retrieve_show_info(path=None, verbose=None, fflag=None, deep=None, debug=None):
    #     '''
    #     This function retrieves info from a given path
    #     :param path:
    #     :param verbose:
    #     :param fflag:
    #     :param deep:
    #     :param debug:
    #     :return:
    #     '''
    #     metadata = Metadata()
    #     film_flag = year = ''
    #     name = season = episode = ename = ''
    #     subs = audio = codec = uploader = source = ''
    #     language = ''
    #     try:
    #         aux = str(os.path.basename(path))
    #         if int(fflag) == int(fflags.LIBRARY_FLAG):
    #             name = aux
    #
    #         elif int(fflag) == int(fflags.MAIN_SHOW_DIRECTORY_FLAG):
    #             name = aux
    #
    #         elif int(fflag) == int(fflags.SUBTITLE_DIRECTORY_FILM_FLAG):
    #             name = prettify_title(offrmod.retrieve_film_name(path=aux, verbose=verbose))
    #             year = offrmod.retrieve_film_year(path=aux, verbose=verbose)
    #             subs = offrmod.retrieve_subtitles_directory(path=aux, verbose=verbose)
    #
    #         elif int(fflag) == int(fflags.SUBTITLE_FILM_FLAG):
    #             name = prettify_title(offrmod.retrieve_film_name(path=aux, verbose=verbose))
    #             year = offrmod.retrieve_film_year(path=aux, verbose=verbose)
    #             language = onrmod.retrieve_str_language(path=path, verbose=verbose)
    #
    #         elif int(fflag) == int(fflags.SUBTITLE_DIRECTORY_SHOW_FLAG):
    #             name = prettify_title(offrmod.retrieve_show_name(path=aux, verbose=verbose, fflag=fflag))
    #             season = offrmod.retrieve_season(path=aux, verbose=verbose)
    #             episode = offrmod.retrieve_episode(path=aux, verbose=verbose)
    #             subs = offrmod.retrieve_subtitles_directory(path=aux, verbose=verbose)
    #
    #         elif int(fflag) == int(fflags.SUBTITLE_SHOW_FLAG):
    #             name = prettify_title(offrmod.retrieve_show_name(path=aux, verbose=verbose, fflag=fflag))
    #             season = offrmod.retrieve_season(path=aux, verbose=verbose)
    #             episode = offrmod.retrieve_episode(path=aux, verbose=verbose)
    #             language = onrmod.retrieve_str_language(path=path, verbose=verbose)
    #
    #         elif int(fflag) == int(fflags.SUBTITLE_DIRECTORY_ANIME_FLAG):
    #             name = prettify_title(offrmod.retrieve_anime_name(path=aux, verbose=verbose))
    #             episode = offrmod.retrieve_anime_episode(path=aux, verbose=verbose)
    #             subs = offrmod.retrieve_subtitles_directory(path=aux, verbose=verbose)
    #
    #         elif int(fflag) == int(fflags.SUBTITLE_ANIME_FLAG):
    #             name = prettify_title(offrmod.retrieve_anime_name(path=aux, verbose=verbose))
    #             episode = offrmod.retrieve_anime_episode(path=aux, verbose=verbose)
    #             language = onrmod.retrieve_str_language(path=path, verbose=verbose)
    #
    #         elif int(fflag) == int(fflags.SEASON_DIRECTORY_FLAG):
    #             name = prettify_title(offrmod.retrieve_show_name(path=aux, verbose=verbose, fflag=fflag))
    #             season = offrmod.retrieve_season_directory(path=aux, verbose=verbose)
    #
    #         elif int(fflag) == int(fflags.SHOW_DIRECTORY_FLAG):
    #             name = prettify_title(offrmod.retrieve_show_name(path=aux, verbose=verbose, fflag=fflag))
    #             season = offrmod.retrieve_season(path=aux, verbose=verbose)
    #             episode = offrmod.retrieve_episode(path=aux, verbose=verbose)
    #             ename = onrmod.retrieve_episode_name(show_name=name, season=season, episode=episode, verbose=verbose)
    #
    #         elif int(fflag) == int(fflags.SHOW_FLAG):
    #             name = prettify_title(offrmod.retrieve_show_name(path=aux, verbose=verbose, fflag=fflag))
    #             season = offrmod.retrieve_season(path=aux, verbose=verbose)
    #             episode = offrmod.retrieve_episode(path=aux, verbose=verbose)
    #             ename = onrmod.retrieve_episode_name(show_name=name, season=season, episode=episode, verbose=verbose)
    #
    #         elif int(fflag) == int(fflags.FILM_DIRECTORY_FLAG):
    #             name = prettify_title(offrmod.retrieve_film_name(path=aux, verbose=verbose))
    #             year = offrmod.retrieve_film_year(path=aux, verbose=verbose)
    #             film_flag = str(offrmod.retrieve_film_flags(path=aux, verbose=verbose)).replace('.', ' ')
    #
    #         elif int(fflag) == int(fflags.FILM_FLAG):
    #             name = prettify_title(offrmod.retrieve_film_name(path=aux, verbose=verbose))
    #             year = offrmod.retrieve_film_year(path=aux, verbose=verbose)
    #             film_flag = str(offrmod.retrieve_film_flags(path=aux, verbose=verbose)).replace('.', ' ')
    #
    #         elif int(fflag) == int(fflags.ANIME_FLAG):
    #             name = prettify_title(offrmod.retrieve_anime_name(path=aux, verbose=verbose))
    #             episode = offrmod.retrieve_anime_episode(path=aux, verbose=verbose)
    #
    #         elif int(fflag) == int(fflags.ANIME_DIRECTORY_FLAG):
    #             name = prettify_title(offrmod.retrieve_anime_name(path=aux, verbose=verbose))
    #             episode = offrmod.retrieve_anime_episode(path=aux, verbose=verbose)
    #
    #         elif int(fflag) == int(fflags.UNKOWN_FLAG):
    #             name = aux
    #
    #         quality = offrmod.retrieve_quality(path=aux, verbose=verbose)
    #         extension = offrmod.retrieve_extension(path=aux, verbose=verbose)
    #
    #         if deep:
    #             codec = offrmod.retrieve_offline_codec(path=aux, verbose=verbose)
    #             audio = offrmod.retrieve_offline_audio(path=aux, verbose=verbose)
    #             uploader = offrmod.retrieve_uploader(path=aux, verbose=verbose)
    #             source = offrmod.retrieve_source(path=aux, verbose=verbose)
    #
    #             metadata.set_codec(codec=codec)
    #             metadata.set_audio(audio=audio)
    #             metadata.set_uploader(uploader=uploader)
    #             metadata.set_source(source=source)
    #
    #         metadata.set_name(name=name)
    #         metadata.set_season(season=season)
    #         metadata.set_episode(episode=episode)
    #         metadata.set_ename(ename=ename)
    #         metadata.set_quality(quality=quality)
    #         metadata.set_extension(extension=extension)
    #         metadata.set_language(language=language)
    #         metadata.set_year(year=year)
    #         metadata.set_film_flag(film_flag=film_flag)
    #         metadata.set_subtitle(subs)
    #         metadata.set_fflag(fflag=fflag)
    #
    #         message = 'standard metada'
    #         log_debug(message)
    #         message = str(name), str(ename), str(episode), str(season), str(quality), str(extension), str(language)
    #         log_debug(message)
    #         message = ' extended metada'
    #         log_debug(message)
    #         message = str(audio), str(codec), str(uploader), str(source), str(fflag), str(film_flag), str(subs)
    #         log_debug(message)
    #
    #     except Exception as e:
    #         print (e)
    #         return
    #     else:
    #         return metadata