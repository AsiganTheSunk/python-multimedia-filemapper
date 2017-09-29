#!/usr/bin/python

import os
from filemapper import filemapper_cc as fmcc
from filemapper import filemapper as fm
from filemapper.pandas import pandas_module as pmod
import imdb

def retrieve_film_gerne(current_movie=str):
    m = imdb.IMDb()
    movie_id = m.search_movie(current_movie)[0].movieID
    movie_genre = m.get_movie(unicode(movie_id))['genre'][0]
    return movie_genre


def file_mapper():
    basedir_new = '/media/asigan/Pila/Peliculos/Peliculas'
    basedir = str(os.getcwd()) + '/test-library'
    print(' ' + '------' * 20)
    print('|' + '\t' * 6 + 'FILE_MAPPER' + '\t'*8 + ' |')
    print(' ' + '------' * 20 + '\n')
    directory = fm.directory_mapper(path=basedir_new, verbose=False)

    trees = fm.build_directory_tree(basedir=basedir_new, directory=directory, verbose=True, debug=True , deep=False)
    trees[0].display()
    print('\n' + '________' * 20)
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
   # fmcc.filemapper_cc()


if __name__ == '__main__':
    main()

# todo validar los cambios
