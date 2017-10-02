# import os
# import pandas as pd
# from pandas import DataFrame
# from filemapper import FileMapper as fm
# from filemapper.datastructure.Metadata import Metadata
# from filemapper.datastructure.TreeRoot import TreeRoot
# from filemapper.metadata import online_retrieve_module as onrmod
# from filemapper.datastructure.FileFlags import FileFlags as FFLAGS
#
# class PandasShowExtension():
#     def __init__(self):
#         return
#
#     def create_season_directory(dataframe, current_serie=str, season=str, parent=str):
#         new_season_directory = fm.build_season_directory_name(name=current_serie, season=str(season))
#
#         dataframe = add_dataframe_row(dataframe=dataframe, name=current_serie, season=season, episode='N/A',
#                                       fflag=FFLAGS.SEASON_DIRECTORY_FLAG, basename=new_season_directory, parent=parent)
#         return dataframe
#
#     def create_shows_directory(dataframe, library=str):
#         dataframe = add_dataframe_row(dataframe=dataframe, name='Shows', season='', episode='',
#                                       fflag=FFLAGS.LIBRARY_FLAG, basename='Shows', parent=library)
#         return dataframe
#
#
#
#
#     def create_main_show_directory(dataframe, current_serie=str):
#         dataframe = add_dataframe_row(dataframe=dataframe, name=current_serie, season='N/A', episode='N/A',
#                                       fflag=FFLAGS.MAIN_SHOW_DIRECTORY_FLAG, basename=current_serie, parent='Shows')
#         return dataframe
#
#
# def create_season_directory(dataframe, current_serie=str, season=str, parent=str):
#     new_season_directory = fm.build_season_directory_name(name=current_serie, season=str(season))
#
#     dataframe = add_dataframe_row(dataframe=dataframe, name=current_serie, season=season, episode='N/A',
#                                   fflag=FFLAGS.SEASON_DIRECTORY_FLAG, basename=new_season_directory, parent=parent)
#     return dataframe
#
# #
# def create_shows_directory(dataframe, library=str):
#     dataframe = add_dataframe_row(dataframe=dataframe, name='Shows', season='', episode='',
#                                   fflag=FFLAGS.LIBRARY_FLAG, basename='Shows', parent=library)
#     return dataframe
#
#
#
# def retrieve_episodes(dataframe, current_serie, drop_dup=False):
#     if drop_dup:
#         dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie).drop_duplicates()
#     else:
#         dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie)
#     return dataframe_episodes[dataframe_episodes.fflag == FFLAGS.SHOW_FLAG]
#
#
# def retrieve_episodes_directories(dataframe, current_serie, drop_dup=False):
#     if drop_dup:
#         dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie).drop_duplicates()
#     else:
#         dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie)
#     return dataframe_episodes[dataframe_episodes.fflag == FFLAGS.SHOW_DIRECTORY_FLAG]
#
#
# def retrieve_seasons(dataframe, current_serie, drop_dup=False):
#     if drop_dup:
#         dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie).drop_duplicates()
#     else:
#         dataframe_episodes = dataframe.groupby(['name']).get_group(current_serie)
#     return dataframe_episodes[dataframe_episodes.fflag == FFLAGS.SEASON_DIRECTORY_FLAG]
#
#
# def retrieve_current_episodes_per_season (dataframe, current_serie):
#     dataframe_episodes = retrieve_episodes(dataframe=dataframe, current_serie=current_serie)
#     dataframe_episodes_directories = retrieve_episodes_directories(dataframe=dataframe, current_serie=current_serie)
#     dataframe_seasons = retrieve_seasons(dataframe=dataframe, current_serie=current_serie)
#     main_show_directory = dataframe[dataframe['basename'] == current_serie]
#     current_status = 'NO'
#     if not main_show_directory.empty:
#         current_status = 'YES'
#     print('------' * 20)
#     print('-- Directory: {status} | SHOW NAME: {show_name} '.format(show_name=current_serie, status=current_status))
#     print('------' * 20)
#
#     try:
#         total_seasons = onrmod.retrieve_number_of_seasons(current_serie)
#         for i in range(0, total_seasons, 1):
#             try:
#                 total_episodes = onrmod.retrieve_number_of_episodes_per_season(current_serie, i)
#                 dataframe_episodes_per_season = dataframe_episodes[dataframe_episodes.season == str(i)]
#                 current_episodes = len(dataframe_episodes_per_season)
#             except:
#                 continue
#             else:
#
#                 dataframe_season = dataframe_seasons[dataframe_seasons.season == str(i)]
#                 season_dir = 'NO '
#                 if not dataframe_season.empty:
#                     season_dir = 'YES'
#                 print('Directory: {status} | Season {season} - Found ({current}/{total} Episodes)'.format(season=i, current=current_episodes, total=total_episodes, status=season_dir))
#                 dataframe_temp = dataframe_episodes_per_season.reindex()
#                 for index in range(0,len(dataframe_temp.index),1):
#                     basename = dataframe_temp.iloc[int(index)]['basename']
#                     dataframe_directory = dataframe_episodes_directories[dataframe_episodes_directories.basename == basename[:-4]]
#                     current_dir = 'NO '
#                     if not dataframe_directory.empty:
#                         current_dir = 'YES'
#                     print('--: Directory: {status} | {basename}'.format(basename=basename,status=current_dir))
#             print('------' * 20)
#
#     except:
#         return
#
#
#
# def create_default_show_tree_directory(dataframe, current_serie=str, library=str, with_dir=True):
#     main_show_directory = dataframe[dataframe['basename'] == current_serie]
#     if main_show_directory.empty:
#         dataframe = create_main_show_directory(dataframe=dataframe, current_serie=current_serie)
#     else:
#         dataframe = update_parent_dataframe_row(dataframe=dataframe, index=int(main_show_directory.index), parent='Shows')
#
#     # metadata season dataframe from current serie
#     dataframe_seasons = retrieve_seasons(dataframe=dataframe, current_serie=current_serie)
#     # metadata episode file dataframe from current serie
#     dataframe_episodes = retrieve_episodes(dataframe=dataframe, current_serie=current_serie)
#     # metadata episode directory dataframe from current serie
#     dataframe_episodes_directories = retrieve_episodes_directories(dataframe=dataframe, current_serie=current_serie)
#
#     # reset index to simply iterate over the rows, extracting the values, to create the directory tree
#     dataframe_temp = dataframe_episodes.reindex()
#
#     for index in range(0, len(dataframe_temp.index), 1):
#         name = dataframe_temp.iloc[int(index)]['name']
#         season = dataframe_temp.iloc[int(index)]['season']
#         episode = dataframe_temp.iloc[int(index)]['episode']
#         basename = dataframe_temp.iloc[int(index)]['basename']
#         parent = dataframe_temp.iloc[int(index)]['parent']
#
#         real_index = dataframe_seasons.index[dataframe_seasons.season == season]
#         dataframe_season = dataframe_seasons[dataframe_seasons.season == season]
#         if dataframe_season.empty:
#
#             dataframe = create_season_directory(dataframe, current_serie=current_serie, season=season, parent=current_serie)
#         else:
#             real_index = real_index.tolist()[0]
#             dataframe = update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent=current_serie)
#
#         dataframe_directory = dataframe_episodes_directories[dataframe_episodes_directories.basename == basename[:-4]]
#         real_index = dataframe_episodes.index[dataframe_episodes.basename == basename].tolist()[0]
#         if dataframe_directory.empty:
#             print('CREATED: ' + str(basename[:-4]))
#             dataframe = add_dataframe_row(dataframe=dataframe, name=name, season=season, episode=episode, fflag=FFLAGS.SHOW_DIRECTORY_FLAG, basename=basename[:-4], parent=parent)
#             dataframe = update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent=basename[:-4])
#
#     dataframe_temp = dataframe_episodes_directories.reindex()
#     for index in range(0, len(dataframe_temp.index), 1):
#         name = dataframe_temp.iloc[int(index)]['name']
#         season = dataframe_temp.iloc[int(index)]['season']
#         basename = dataframe_temp.iloc[int(index)]['basename']
#         parent = dataframe_temp.iloc[int(index)]['parent']
#         new_parent = fm.build_season_directory_name(name=name, season=season)
#
#         real_index = dataframe_episodes_directories.index[dataframe_episodes_directories.basename == basename]
#         if parent not in new_parent:
#             real_index = real_index.tolist()[0]
#             dataframe = update_parent_dataframe_row(dataframe=dataframe, index=int(real_index), parent=new_parent)
#     return dataframe
