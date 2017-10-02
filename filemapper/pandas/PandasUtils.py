import os
import pandas as pd
from pandas import DataFrame
from filemapper import FileMapper as fm
from filemapper.datastructure.Metadata import Metadata
from filemapper.datastructure.TreeRoot import TreeRoot
from filemapper.metadata import online_retrieve_module as onrmod
from filemapper.datastructure.FileFlags import FileFlags as FFLAGS

class PandasUtils():
    def __init__(self):
        return

    def update_parent_dataframe_row(self, dataframe, index, parent):
        dataframe.loc[dataframe.index == index, 'parent'] = parent
        return dataframe

    def add_dataframe_row(self, dataframe, name, season, episode, fflag, basename, parent):
        dict = {'name': [name],
                'season': [season],
                'episode': [episode],
                'fflag': [fflag],
                'basename': [basename],
                'parent': [parent]
                }
        new_row = DataFrame(dict)
        dataframe = dataframe.append(new_row, ignore_index=True)
        return dataframe

    def create_data_frame (self, tree=TreeRoot):
        basenamelist = []
        identifierlist = []
        parent_basenamelist = []
        namelist = []
        seasonlist = []
        episodelist = []
        fflaglist = []
        yearlist = []

        for node in tree.get_nodes():
            metadata = node.get_metadata()
            identifierlist.append(node.identifier)
            basenamelist.append(node.basename)
            parent_basenamelist.append(node.parent_basename)

            namelist.append(metadata.get_name())
            episodelist.append(metadata.get_episode())
            seasonlist.append(metadata.get_season())
            yearlist.append(metadata.get_year())
            fflaglist.append(metadata.get_fflag())

        episodelist = self.clean_data(episodelist)
        seasonlist = self.clean_data(seasonlist)

        dict = {'name': namelist,
                'season': seasonlist,
                'episode': episodelist,
                'year': yearlist,
                'fflag': fflaglist,
                'basename': basenamelist,
                'parent': parent_basenamelist
                }

        #dataframe = DataFrame(raw_data, columns=['name', 'size', 'seed', 'leech', 'magnet'])
        dataframe = DataFrame(dict)
        print(dataframe)
        return dataframe


    def clean_data(self, list):
        for i in range(0, len(list), 1):
            if list[i] == '':
                list[i] = 'N/A'
            else:
                list[i] = str(int(list[i]))
        return list
