import pandas as pd
from pandas import DataFrame

pd.set_option('display.max_rows', 750)
pd.set_option('display.max_columns', 750)
pd.set_option('display.width', 1400)


class PandasUtils():
    def __init__(self):
        return

    def update_parent_dataframe_row(self, dataframe, index, parent):
        '''
        This function updates the parent of row from the dataframe using the index
        :param dataframe: It represents the dataframe input
        :param index: It represents the index you're about to modify
        :param parent: It represents the name of the parent folder
        :return: UPDATED_DATAFRAME
        '''
        dataframe.loc[dataframe.index == index, 'parent'] = parent
        return dataframe

    def add_dataframe_row(self, dataframe, name, season, year, genre, episode,
                          fflag, basename, parent, n_season,
                          e_season):
        '''
        This function adds a new row to the dataframe
        :param dataframe: It represents the dataframe input
        :param name: It represents metadata name of the file or directory
        :param season: It represents metadata season of the file or directory
        :param year: It represents metadata year of the file or directory
        :param genre: It represents metadata genre of the file or directory
        :param episode: It represents metadata episode of the file or directory
        :param fflag: It represents metadata fflag of the file or directory
        :param basename: It represents metadata basename of the file or directory
        :param parent: It represents metadata parent of the file or directory
        :param n_season: It represents metadata n_season of the file or directory
        :param e_season: It represents metadata e_season of the file or directory
        :return: UPDATED_DATAFRAME
        '''
        raw_data = {'name': [name],
                    'season': [season],
                    'episode': [episode],
                    'year': [year],
                    'genre': [genre],
                    'fflag': [fflag],
                    'basename': [basename],
                    'parent': [parent],
                    'n_season': [n_season],
                    'e_season': [e_season]
                    }

        new_row = DataFrame(raw_data,
                            columns=['name', 'season', 'episode', 'year',
                                     'genre', 'fflag', 'basename', 'parent',
                                     'n_season', 'e_season'])
        dataframe = dataframe.append(new_row, ignore_index=True)
        return dataframe

    def create_data_frame(self, tree, verbose=False, debug=False):
        '''
        This function transforms MetadataTree into Pandas Detaframe
        :param tree: It respresents the the MetadataTree input
        :param debug: It represents the debug status of the function, default it's False
        :return: DATAFRAME
        '''

        dataframe = DataFrame()
        basenamelist = []
        identifierlist = []
        parent_basenamelist = []
        namelist = []
        seasonlist = []
        episodelist = []
        fflaglist = []
        yearlist = []
        genrelist = []
        n_seasonlist = []
        e_seasonlist = []

        try:
            for node in tree.get_nodes():
                metadata = node.get_metadata()
                identifierlist.append(node.identifier)
                basenamelist.append(node.basename)
                parent_basenamelist.append(node.parent_basename)
                namelist.append(self.eval_empty_value(metadata.get_name()))
                episodelist.append(
                    self.eval_empty_value(metadata.get_episode()))
                seasonlist.append(self.eval_empty_value(metadata.get_season()))
                yearlist.append(self.eval_empty_value(metadata.get_year()))
                fflaglist.append(self.eval_empty_value(metadata.get_fflag()))
                genrelist.append(self.eval_empty_value(metadata.get_genre()))
                n_seasonlist.append(
                    self.eval_empty_value(metadata.get_n_season()))
                e_seasonlist.append(
                    self.eval_empty_value(metadata.get_e_season()))

            raw_data = {'name': namelist,
                        'season': seasonlist,
                        'episode': episodelist,
                        'year': yearlist,
                        'genre': genrelist,
                        'fflag': fflaglist,
                        'basename': basenamelist,
                        'parent': parent_basenamelist,
                        'n_season': n_seasonlist,
                        'e_season': e_seasonlist
                        }

            if verbose:
                print (len(namelist)), '\n', namelist
                print (len(seasonlist)), '\n', seasonlist
                print (len(episodelist)), '\n', episodelist
                print (len(fflaglist)), '\n', fflaglist
                print (len(basenamelist)), '\n', basenamelist
                print (len(parent_basenamelist)), '\n', parent_basenamelist
                print (len(n_seasonlist)), '\n', n_seasonlist
                print (len(e_seasonlist)), '\n', e_seasonlist
                print (len(yearlist)), '\n', yearlist
                print (len(genrelist)), '\n', genrelist
            dataframe = DataFrame(raw_data,
                                  columns=['name', 'season', 'episode', 'year',
                                           'genre', 'fflag', 'basename',
                                           'parent',
                                           'n_season', 'e_season'])
        except Exception as e:
            print 'Create dataframe ERROR: ', e
        return dataframe

    def eval_empty_value(self, value):
        if value is '':
            return 'N/A'
        return value

    def clean_empty_value(self, value):
        if value is 'N/A':
            return ''
        return value
