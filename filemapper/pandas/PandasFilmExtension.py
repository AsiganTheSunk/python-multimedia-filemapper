# import os
# import pandas as pd
# from pandas import DataFrame
# from filemapper import FileMapper as fm
# from filemapper.datastructure.Metadata import Metadata
# from filemapper.datastructure.TreeRoot import TreeRoot
# from filemapper.metadata import online_retrieve_module as onrmod
# from filemapper.datastructure.FileFlags import FileFlags as FFLAGS
#
# class PandasFilmExtension():
#     def __init__(self):
#         return
#
#     def retrieve_movies(dataframe):
#         return dataframe[dataframe.fflag == FFLAGS.FILM_FLAG]
#
#     def retrieve_movies_directories(dataframe):
#         return dataframe[dataframe.fflag == FFLAGS.FILM_DIRECTORY_FLAG]
#
# def create_main_show_directory(dataframe, current_serie=str):
#     dataframe = add_dataframe_row(dataframe=dataframe, name=current_serie, season='N/A', episode='N/A',
#                                   fflag=FFLAGS.MAIN_SHOW_DIRECTORY_FLAG, basename=current_serie, parent='Shows')
#     return dataframe
#
#
# def create_movies_directory(dataframe, library=str):
#     dataframe = add_dataframe_row(dataframe=dataframe, name='Movies', season='', episode='',
#                                   fflag=FFLAGS.LIBRARY_FLAG, basename='Movies', parent=library)
#     return dataframe
#
#
# def create_default_movies_tree_directory(dataframe):
#
#     dataframe_film_directories = retrieve_movies_directories(dataframe)
#     dataframe_film = retrieve_movies(dataframe)
#
#     dataframe_film_temp = dataframe_film.reindex()
#     for index in range(0, len(dataframe_film_temp.index), 1):
#         name = dataframe_film_temp.iloc[int(index)]['name']
#         basename = dataframe_film_temp.iloc[int(index)]['basename']
#         parent = dataframe_film_temp.iloc[int(index)]['parent']
#         dataframe_directory = dataframe_film_directories[dataframe_film_directories.basename == basename[:-4]]
#         real_index = dataframe_film.index[dataframe_film.basename == basename]
#         if dataframe_directory.empty:
#             dataframe = add_dataframe_row(dataframe=dataframe, name=name, season='', episode='', fflag=FFLAGS.FILM_DIRECTORY_FLAG, basename=basename[:-4], parent=parent)
#             dataframe = update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent=basename[:-4])
#
#     dataframe_dfilm_temp = dataframe_film_directories.reindex()
#     for index in range(0, len(dataframe_dfilm_temp.index), 1):
#         name = dataframe_dfilm_temp.iloc[int(index)]['name']
#         season = dataframe_dfilm_temp.iloc[int(index)]['season']
#         basename = dataframe_dfilm_temp.iloc[int(index)]['basename']
#         parent = dataframe_dfilm_temp.iloc[int(index)]['parent']
#         real_index = dataframe.index[dataframe.basename == basename]
#
#         if parent not in 'Movies':
#             real_index = real_index.tolist()[0]
#             dataframe = update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent='Movies')
#
#     return dataframe
