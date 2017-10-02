# import os
# import pandas as pd
# from pandas import DataFrame
# from filemapper import FileMapper as fm
# from filemapper.datastructure.Metadata import Metadata
# from filemapper.datastructure.TreeRoot import TreeRoot
# from filemapper.metadata import online_retrieve_module as onrmod
# from filemapper.datastructure.FileFlags import FileFlags as FFLAGS
#
# class PandasEngine():
#     def __init__(self):
#         return
#
#     def update_parent_dataframe_row(dataframe, index, parent):
#         dataframe.loc[dataframe.index == index, 'parent'] = parent
#         return dataframe
#
#     def retrieve_library_show_statistics(self, dataframe):
#         unique_series = retrieve_name_series(dataframe=dataframe)
#         print('------' * 20)
#         print('-- DETECTED [ {current} ] SHOWS'.format(current=len(unique_series)))
#         for current_serie in unique_series:
#             retrieve_current_episodes_per_season(dataframe=dataframe, current_serie=current_serie)
#             print
#         return dataframe
#
#     def create_library(self, dataframe, library=str):
#         unique_series = retrieve_name_series(dataframe=dataframe)
#         dataframe = create_shows_directory(dataframe=dataframe, library=library)
#         for current_serie in unique_series:
#             dataframe = create_default_show_tree_directory(dataframe=dataframe, current_serie=current_serie,
#                                                            library=library)
#
#         dataframe = create_movies_directory(dataframe=dataframe, library=library)
#         dataframe = create_default_movies_tree_directory(dataframe)
#
#         dataframe = create_animes_directory(dataframe=dataframe, library=library)
#         unique_animes = retrieve_name_animes(dataframe=dataframe)
#         for current_anime in unique_animes:
#             dataframe = create_default_anime_tree_directory(dataframe=dataframe, current_anime=current_anime,
#                                                             library=library)
#         # TODO Hay que hacerlo para cada uno de los estilos, movie y serie estan echos, hace falta un tercero para los animes
#         # dataframe = build_genre_dataframe_row(dataframe=dataframe)
#         return dataframe
#
#     def add_dataframe_row(dataframe, name, season, episode, fflag, basename, parent):
#         dict = {'name': [name],
#                 'season': [season],
#                 'episode': [episode],
#                 'fflag': [fflag],
#                 'basename': [basename],
#                 'parent': [parent]
#                 }
#         new_row = DataFrame(dict)
#         dataframe = dataframe.append(new_row, ignore_index=True)
#         return dataframe
#
#     def update_tree_info(old_dataframe, dataframe, tree):
#         total_rows = len(dataframe.index)
#         new_rows = total_rows - len(old_dataframe.index)
#         print('--: New nodes to be Added to the tree: (' + str(new_rows) + '/' + str(total_rows) + ')')
#         for index in range(len(old_dataframe.index), len(dataframe.index), 1):
#             name = dataframe.iloc[int(index)]['name']
#             season = dataframe.iloc[int(index)]['season']
#             episode = dataframe.iloc[int(index)]['episode']
#             basename = dataframe.iloc[int(index)]['basename']
#             parent = dataframe.iloc[int(index)]['parent']
#             # print('index: ' + str(index), 'basename: ' + str(basename),  'parent: ' + str(parent))
#             # print('name: ' + str(name),'season: ' + str(season),'episode: ' + str(episode))
#             metadata = Metadata()
#             metadata.set_name(name)
#             if season not in 'N/A':
#                 metadata.set_season(season)
#             if episode not in 'N/A':
#                 metadata.set_episode(episode)
#             tree.add_node(basename=basename, metadata=metadata, parent_basename=parent)
#
#         print(
#         '--: Nodes that need to be Updated in the tree: (' + str(len(old_dataframe)) + '/' + str(total_rows) + ')')
#         for index in range(0, len(old_dataframe.index), 1):
#             current_basename = dataframe.iloc[int(index)]['basename']
#             current_parent = dataframe.iloc[int(index)]['parent']
#             node = tree.search(basename=current_basename)
#             node = node[0]
#             old_parent_basename = node.parent_basename
#             if current_parent != old_parent_basename:
#                 # print('------'*20)
#                 # print('Input: index({index}) basename: {base} - [Parent]: old: {old_parent}'.format(index=index, old_parent=old_parent_basename, base=node.basename))
#                 # print('Onput: index({index}) basename: {basename} - [Parent]: new: {new_parent}'.format(index=index, basename=current_basename, new_parent=current_parent))
#                 tree.update_parent_node_by_index(index=int(index), parent=current_parent)
#
#         return tree
#
#     def build_genre_dataframe_row (self, dataframe):
#         dataframe['genre'] = 'N/A'
#         # TODO: buscar aquellos que tengan como padre el basename de la carpeta y anadir genre ahi si es necesario
#         for index in range(0, len(dataframe) , 1):
#             fflag = dataframe.iloc[int(index)]['fflag']
#             name = dataframe.iloc[int(index)]['name']
#             if str(fflag) == FFLAGS.FILM_DIRECTORY_FLAG:
#                 current_genre = onrmod.retrieve_film_genre(name)
#                 dataframe.loc[dataframe.index == index, 'genre'] = current_genre
#                 #print name
#
#             elif str(fflag) == FFLAGS.MAIN_SHOW_DIRECTORY_FLAG:
#                 current_genre = onrmod.retrieve_show_genre(name)
#                 dataframe.loc[dataframe.index == index, 'genre'] = current_genre
#                 #print 'SHOW'
#
#         return dataframe
