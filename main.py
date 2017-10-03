#!/usr/bin/python

from filemapper.datastructure.FileFlags import FileFlags as fflags
from filemapper.metadata.regex.RegexEngine import RegexEngine
from filemapper.metadata.regex.RegexFilmExtension import RegexFilmExtension
from filemapper.metadata.regex.RegexShowExtension import RegexShowExtension
from filemapper.metadata.regex.RegexAnimeExtension import RegexAnimeExtension
from filemapper.metadata.regex.RegexCommonExtension import RegexCommonExtension
from filemapper.metadata.regex.RegexSubtitleExtension import RegexSubtitleExtension
from filemapper.metadata.tvdb.TVDbShowExtension import TVDbShowExtension
from filemapper.metadata.tvdb.TVDbEngine import TVDbEngine
from filemapper.metadata.imdb.IMDbEngine import IMDbEngine
from filemapper.metadata.MetadataEngine import MetadataEngine
from filemapper.check.CheckEngine import CheckEngine
from filemapper.FileMapper import FileMapper
from filemapper.sbuilder.StringBuilder import StringBuilder
from filemapper.pandas.PandasUtils import PandasUtils
from filemapper.pandas.PandasFilmExtension import PandasFilmExtension
from filemapper.pandas.PandasAnimeExtension import PandasAnimeExtension
from filemapper.pandas.PandasEngine import PandasEngine
 #from filemapper.pandas.PandasShowExtension import
import os

def file_mapper():
    basedir = str(os.getcwd()) + '/test-library'
    _file_mapper = FileMapper()

    directory = _file_mapper.premap(path=basedir)
    tree = _file_mapper.build_directory_tree(basedir=basedir, debug=True)
    tree[0].tree()
    print '~~~~~~~~~~~~~~~~~~~~' * 7
    pandas_engine = PandasEngine(tree=tree[0])
    dataframe = pandas_engine.create_library(tree=tree[0].nodes[0].basename)
    print '~~~~~~~~~~~~~~~~~~~~' * 7
    print '~~~~~~~~~~~~~~~~~~~~' * 7


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
