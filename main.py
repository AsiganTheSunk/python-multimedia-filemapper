#!/usr/bin/python

from filemapper.datastructure.FileFlags import FileFlags as fflags
from filemapper.retrieve.regex.RegexEngine import RegexEngine
from filemapper.retrieve.regex.RegexFilmExtension import RegexFilmExtension
from filemapper.retrieve.regex.RegexShowExtension import RegexShowExtension
from filemapper.retrieve.regex.RegexAnimeExtension import RegexAnimeExtension
from filemapper.retrieve.regex.RegexCommonExtension import RegexCommonExtension
from filemapper.retrieve.regex.RegexSubtitleExtension import RegexSubtitleExtension
def file_mapper():
    regex_engine = RegexEngine()
    regex_engine.map(stream='Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG', fflag=fflags.FILM_DIRECTORY_FLAG,
                     verbose=True)

    regex_engine = RegexEngine()
    regex_engine.map(stream='Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]', fflag=fflags.SHOW_DIRECTORY_FLAG,
                     verbose=True)
    regex_engine.map(stream='[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]', fflag=fflags.ANIME_DIRECTORY_FLAG,
                     verbose=True)

    #
    # movie_engine = RegexFilmExtension()
    # movie_engine.get_name(stream='Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG',debug=True)
    # movie_engine.get_year(stream='Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG',debug=True)
    # movie_engine.get_tags(stream='Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG',debug=True)
    # common_engine.get_quality(stream='Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG',debug=True)
    # common_engine.get_vcodec(stream='Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG',debug=True)
    # common_engine.get_acodec(stream='Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG',debug=True)
    #
    # show_engine = RegexShowExtension()
    # show_engine.get_name(stream='Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]', debug=True)
    # show_engine.get_season(stream='Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]', debug=True)
    # show_engine.get_episode(stream='Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]', debug=True)
    # common_engine.get_quality(stream='Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]', debug=True)
    # common_engine.get_vcodec(stream='Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]', debug=True)
    # common_engine.get_acodec(stream='Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]', debug=True)
    #
    # anime_engine= RegexAnimeExtension()
    # anime_engine.get_name(stream='[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]', debug=True)
    # anime_engine.get_episode(stream='[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]', debug=True)
    # common_engine.get_quality(stream='[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]', debug=True)
    # common_engine.get_uploader(stream='[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]', debug=True)
    #
    #
    # anime_engine.get_name(stream='[Dcms-Fansubs] Detective Conan Episode 840 [1080p]', debug=True)
    # anime_engine.get_episode(stream='[Dcms-Fansubs] Detective Conan Episode 840 [1080p]', debug=True)
    # common_engine.get_quality(stream='[Dcms-Fansubs] Detective Conan Episode 840 [1080p]', debug=True)
    # common_engine.get_uploader(stream='[Dcms-Fansubs] Detective Conan Episode 840 [1080p]', debug=True)

    # basedir_new = '/media/asigan/Pila/Peliculos/Peliculas'
    # basedir = str(os.getcwd()) + '/test-library'
    # print(' ' + '------' * 20)
    # print('|' + '\t' * 6 + 'FILE_MAPPER' + '\t'*8 + ' |')
    # print(' ' + '------' * 20 + '\n')
    # directory = fm.directory_mapper(path=basedir_new, verbose=False)
    #
    # trees = fm.build_directory_tree(basedir=basedir_new, directory=directory, verbose=True, debug=True , deep=False)
    # trees[0].display()
    # print('\n' + '________' * 20)
    #dataframe = pmod.create_data_frame(tree=trees[0])
    #temp = dataframe
    # dataframe = pmod.create_library(dataframe=dataframe, library='test-library')
    # print('\n Dataframe Original:')
    # print(' ' + '------' * 20)
    # print(dataframe)
    # print(' ' + '------' * 20)
    #
    # tree = pmod.update_tree_info(old_dataframe=temp, dataframe=dataframe, tree=trees[0])
    # print('\n Dataframe Final:')
    # print(' ' + '------' * 20)
    # tree.tree()
    # print(' ' + '------' * 20)


def main():
    file_mapper()

if __name__ == '__main__':
    main()

# todo validar los cambios
