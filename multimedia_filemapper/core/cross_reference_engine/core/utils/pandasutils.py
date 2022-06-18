import pandas as pd
from pandas import DataFrame
pd.set_option('display.max_rows', 750)
pd.set_option('display.max_columns', 750)
pd.set_option('display.width', 1400)


class PandasUtils():
    def __init__(self):
        return

    def update_parent_dataframe_row(self, dataframe, index, parent):
        """
        This function updates the parent of row from the dataframe using the index
        :param dataframe: It represents the dataframe input
        :param index: It represents the index you're about to modify
        :param parent: It represents the name of the parent folder
        :return: UPDATED_DATAFRAME
        """
        dataframe.loc[dataframe.index == index, 'parent'] = parent
        return dataframe

    def add_dataframe_row(self, dataframe, name, season, year, genre, episode,
                          fflag, basename, parent, n_season,
                          e_season):
        """
        This function adds a new row to the dataframe
        :param dataframe: It represents the dataframe input
        :param name: It represents metadata_engine name of the file or directory
        :param season: It represents metadata_engine season of the file or directory
        :param year: It represents metadata_engine year of the file or directory
        :param genre: It represents metadata_engine genre of the file or directory
        :param episode: It represents metadata_engine episode of the file or directory
        :param fflag: It represents metadata_engine fflag of the file or directory
        :param basename: It represents metadata_engine basename of the file or directory
        :param parent: It represents metadata_engine parent of the file or directory
        :param n_season: It represents metadata_engine n_season of the file or directory
        :param e_season: It represents metadata_engine e_season of the file or directory
        :return: UPDATED_DATAFRAME
        """
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

    def create_data_frame(self, tree):
        """
        This function transforms MetadataTree into Pandas Detaframe
        :param tree: It represents the MetadataTree input
        :return: DATAFRAME
        """

        dataframe = DataFrame()
        identifier_list = []
        basename_list = []
        new_basename_list = []
        parent_basename_list = []
        new_parent_basename_list = []
        name_list = []
        season_list = []
        episode_list = []
        fflag_list = []
        year_list = []
        genre_list = []
        n_season_list = []
        e_season_list = []

        try:
            for node in tree.get_nodes()[1:]:
                metadata = node.get_metadata()
                identifier_list.append(node.identifier)
                basename_list.append(node.basename)
                new_basename_list.append(node.new_basename)
                parent_basename_list.append(node.parent_basename)
                new_parent_basename_list.append(node.new_parent_basename)
                name_list.append(self.eval_empty_value(metadata.get_name()))
                episode_list.append(self.eval_empty_value(metadata.get_episode()))
                season_list.append(self.eval_empty_value(metadata.get_season()))
                year_list.append(self.eval_empty_value(metadata.get_year()))
                fflag_list.append(self.eval_empty_value(metadata.get_fflag()))
                genre_list.append(self.eval_empty_value(metadata.get_genre()))
                n_season_list.append(self.eval_empty_value(metadata.get_n_season()))
                e_season_list.append(self.eval_empty_value(metadata.get_e_season()))

            raw_data = {
                'fflag': fflag_list,
                'name': name_list,
                'season': season_list,
                'episode': episode_list,
                'year': year_list,
                'genre': genre_list,
                'n_season': n_season_list,
                'e_season': e_season_list,
                'basename': new_basename_list,
                'parent': new_parent_basename_list,
                'path': basename_list,
                # 'root_path': parent_basename_list,
            }

            # print(len(namelist)), '\n', namelist
            # print(len(seasonlist)), '\n', seasonlist
            # print(len(episodelist)), '\n', episodelist
            # print(len(fflaglist)), '\n', fflaglist
            # print(len(basenamelist)), '\n', basenamelist
            # print(len(parent_basenamelist)), '\n', parent_basenamelist
            # print(len(n_seasonlist)), '\n', n_seasonlist
            # print(len(e_seasonlist)), '\n', e_seasonlist
            # print(len(yearlist)), '\n', yearlist
            # print(len(genrelist)), '\n', genrelist

            dataframe = DataFrame(raw_data, columns=[
                'fflag', 'name', 'season', 'n_season', 'e_season', 'episode', 'year', 'genre',
                'basename', 'parent', 'path'
            ])
        except Exception as e:
            print('Create dataframe ERROR: ', e)
        return dataframe

    def eval_empty_value(self, value):
        if value == '':
            return 'N/A'
        return value

    def clean_empty_value(self, value):
        if value is 'N/A':
            return ''
        return value
