#!/usr/bin/python
from functools import partial
from multiprocessing import Pool, cpu_count
from os import listdir, walk
from os.path import normpath, basename, abspath, join
from typing import Any, List

from attr import dataclass


class ProcessedItem:
    def __init__(self, root, item):
        self.root = root
        self.item = item


from multimedia_filemapper.core.sieve_engine.core.sieve_engine import SieveEngine
from multimedia_filemapper.core.metadata_engine.struct_data.metadata import Metadata
from multimedia_filemapper.core.metadata_engine.struct_data.metadatanode import MetadataNode
from multimedia_filemapper.core.metadata_engine.struct_data.metadatatree import MetadataTree
from multimedia_filemapper.core.metadata_engine.core.metadataengine import MetadataEngine
from multimedia_filemapper.core.cross_reference_engine.core.pandasengine import PandasEngine
from multimedia_filemapper.core.rename_engine.core.stringbuilder import StringBuilder
from multimedia_filemapper.core.constants.media_file_flags import FileFlags as fflags

# Importing Custom Logger & Logging Modules
from multimedia_filemapper.logger.custom_logger import CustomLogger
from logging import INFO, DEBUG, WARNING
import logging


@dataclass
class MultimediaItem:
    root: str
    item: str
    file_type: fflags = None

    def path(self):
        return normpath(abspath(join(self.root, self.item)))


class FileMapper:
    def __init__(self, basedir, logging_lvl=INFO):
        self.name = self.__class__.__name__
        self.basedir = basedir
        self.directory_dict = {}
        self.multimedia_source = []

        self.tUpdated = MetadataTree()
        self.tOriginal = MetadataTree()

        self.sieve_engine = SieveEngine()
        self.string_builder = StringBuilder()
        self.metadata_engine = MetadataEngine()

        self.logger = CustomLogger(name=__name__, level=logging_lvl)

        # CustomLogger Format Definition
        formatter = logging.Formatter(fmt='%(asctime)s - [%(levelname)s]: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        # Custom Logger File Configuration: File Init Configuration
        file_handler = logging.FileHandler('./multimedia_filemapper/log/engine/file_mapper.log', 'w')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level=logging_lvl)

        # Custom Logger Console Configuration: Console Init Configuration
        # console_handler = logging.StreamHandler()
        # console_handler.setFormatter(formatter)
        # console_handler.setLevel(level=logging_lvl)

        # Custom Logger Console/File Handler Configuration
        self.logger.addHandler(file_handler)
        # self.logger.addHandler(console_handler)

    def add_source(self, path):
        self.multimedia_source.append(path)

    def get_sources(self):
        for item in self.multimedia_source:
            print(item)

    def set_tupdated(self, tree):
        self.tUpdated = tree

    @staticmethod
    def sieve_folders(multimedia_item):
        _sieve_engine = SieveEngine()
        try:
            if _sieve_engine.is_multimedia_folder(multimedia_item.item):
                # Note: I don't remember the case use of this ??
                # multimedia_item.file_type = fflags.MAIN_SHOW_DIRECTORY_FLAG

                if _sieve_engine.is_show_subtitle_folder(multimedia_item.path()):
                    multimedia_item.file_type = fflags.SUBTITLE_DIRECTORY_SHOW_FLAG

                elif _sieve_engine.is_anime_subtitle_folder(multimedia_item.path()):
                    multimedia_item.file_type = fflags.SUBTITLE_DIRECTORY_ANIME_FLAG

                elif _sieve_engine.is_film_subtitle_folder(multimedia_item.path()):
                    multimedia_item.file_type = fflags.SUBTITLE_DIRECTORY_FILM_FLAG

                elif _sieve_engine.is_show_folder(multimedia_item.item):
                    multimedia_item.file_type = fflags.SHOW_DIRECTORY_FLAG

                elif _sieve_engine.is_anime_folder(multimedia_item.item):
                    multimedia_item.file_type = fflags.ANIME_DIRECTORY_FLAG

                elif _sieve_engine.is_season_folder(multimedia_item.item) and listdir(multimedia_item.path()):
                    multimedia_item.file_type = fflags.SEASON_DIRECTORY_FLAG

                elif _sieve_engine.check_film(multimedia_item.item):
                    multimedia_item.file_type = fflags.FILM_DIRECTORY_FLAG

                else:
                    multimedia_item.file_type = fflags.UNKOWN_FLAG
            else:
                multimedia_item.file_type = fflags.UNKOWN_FLAG

            return multimedia_item

        except WindowsError as err:
            if err.winerror == 3:
                print('log file not found')
        except Exception as err:
            print('<< Fatal >>', err)

    @staticmethod
    def sieve_files(multimedia_item):
        _sieve_engine = SieveEngine()
        try:
            # Note: Unwanted FileType >> No Category For Unwanted ??
            if _sieve_engine.check_unwanted(multimedia_item.item):
                multimedia_item.file_type = fflags.UNKOWN_FLAG

            # Note: Show Subtitle FileType
            elif _sieve_engine.check_show_subtitles(multimedia_item.path()):
                multimedia_item.file_type = fflags.SUBTITLE_SHOW_FLAG

            # Note: Film Subtitle FileType
            elif _sieve_engine.check_film_subtitles(multimedia_item.path()):
                multimedia_item.file_type = fflags.SUBTITLE_FILM_FLAG

            # Note: Anime Subtitle FileType
            elif _sieve_engine.check_anime_subtitles(multimedia_item.path()):
                multimedia_item.file_type = fflags.SUBTITLE_ANIME_FLAG

            # Note: Show FileType
            elif _sieve_engine.check_show(multimedia_item.item):
                multimedia_item.file_type = fflags.SHOW_FLAG

            # Note: Film FileType
            elif _sieve_engine.check_film(multimedia_item.item):
                multimedia_item.file_type = fflags.FILM_FLAG

            # Note: Film FileType
            elif _sieve_engine.check_anime(multimedia_item.item):
                multimedia_item.file_type = fflags.ANIME_FLAG

            else:
                multimedia_item.file_type = fflags.UNKOWN_FLAG
            return multimedia_item

        except WindowsError as err:
            if err.winerror == 3:
                print('log file not found')
        except Exception as err:
            print('<< Fatal >>', err)

    def pre_map_multiprocessing(self):
        """
        This function pre-maps the contents of the directory from a given path
        :param path:
        :param verbose:
        :return:
        """

        _processed_multimedia_files: List[MultimediaItem] = []
        _processed_multimedia_folders: List[MultimediaItem] = []
        _multimedia_folders: List[MultimediaItem] = []
        _multimedia_files = []

        try:
            pool = Pool(cpu_count())
            try:
                [_multimedia_folders.append(MultimediaItem(normpath(root), normpath(folder)))
                 for root, folders, files in walk(self.basedir)
                 for folder in folders]
                [_multimedia_files.append(MultimediaItem(normpath(root), normpath(_multimedia_file)))
                 for root, folder, files in walk(self.basedir)
                 for _multimedia_file in files]
            except Exception as error:
                print(f'os.walk {error}')

            try:
                _processed_multimedia_folders = pool.map(self.sieve_folders, _multimedia_folders, 8)
            except Exception as error:
                print(f'{error}')

            try:
                _processed_multimedia_files = pool.map(self.sieve_files, _multimedia_files, 8)
            except Exception as error:
                print(f'{error}')

            # for item in _processed_multimedia_folders:
            #     print(item)
            # for item in _processed_multimedia_files:
            #     print(item)
            # print('\n\n')
            print('=============' * 12)

            un_sorted_multimedia_folder = _processed_multimedia_folders + _processed_multimedia_files
            _sorted_resolved_futures: List[MultimediaItem] = []
            try:
                for _sorted_monthly_report_df in sorted(un_sorted_multimedia_folder, key=lambda tup: tup.path()):
                    self.directory_dict[_sorted_monthly_report_df.path()] = _sorted_monthly_report_df

            except Exception as error:
                print(f'peta ordendar {error}')

            multimedia_tree = self.build_directory_tree()
            return multimedia_tree
        except Exception as err:
            self.logger.fatal(err)

    def build_directory_tree(self):
        """
        This function creates a tree data structure from a given dictionary
        :param basedir:
        :param directory:
        :param deep:
        :return:
        """
        try:
            basedir = self.basedir
            base_node_metadata = self.metadata_engine.map(stream=basedir, fflag=fflags.LIBRARY_FLAG)
            self.tOriginal.add_node(basename=basedir, new_basename=basedir, metadata=base_node_metadata)

            for _multimedia_index, _multimedia_item in enumerate(self.directory_dict):
                _parent_basename = _multimedia_item[:-len(basename(_multimedia_item)) - 1]

                metadata = self.metadata_engine.map(
                    stream=_multimedia_item, fflag=self.directory_dict[_multimedia_item].file_type
                )
                _new_basename = self.string_builder.rebuild_name(metadata=metadata)

                if self.directory_dict[_multimedia_item].root == basedir:
                    _parent_metadata = self.metadata_engine.map(stream=basedir, fflag=fflags.LIBRARY_FLAG)
                    _new_parent_basename = self.string_builder.rebuild_name(metadata=_parent_metadata)
                else:
                    _parent_metadata = self.metadata_engine.map(
                        stream=_parent_basename, fflag=self.directory_dict[_parent_basename].file_type
                    )
                    _new_parent_basename = self.string_builder.rebuild_name(metadata=_parent_metadata)

                self.tOriginal.add_node(basename=_multimedia_item, metadata=metadata,
                                        parent_basename=_parent_basename,
                                        new_basename=_new_basename,
                                        new_parent_basename=_new_parent_basename)
            print('=============' * 12)
            # # self.tOriginal.tree()
            # print(self.tOriginal.get_abs_paths())

        except Exception as error:
            print(f'build-directory-tree: {error}')
        else:
            return self.tOriginal

    def list_directory(self, dict):
        '''
        This function log the pre-map function into a file
        :param dict:
        :return: DIRECTORY
        '''

        self.logger.info('\n{0} Current Directory'.format(self.name))
        for item in sorted(dict):
            if dict[item] == fflags.UNKOWN_FLAG:
                self.logger.info(' (?) << {0} >> {1} '.format(str(dict[item])[10:], item))
            else:
                self.logger.info(' (+) << {0} >> {1} '.format(str(dict[item])[10:], item))

    def map(self, verbose=False, debug=False):
        '''

        :param basedir:
        :param verbose:
        :param debug:
        :return:
        '''
        self.premap()
        tree = self.build_directory_tree()
        pandas_engine = PandasEngine(tree=tree[0])
        pandas_engine.create_library(debug=debug)
        tree = pandas_engine.update_tree(debug=debug)
        self.set_tupdated(tree=tree)

        list = self.tUpdated.get_abs_paths()
        for item in list:
            print(item)

    def test_map(self, verbose=False, debug=False):
        '''

        :param basedir:
        :param verbose:
        :param debug:
        :return:
        '''
        self.premap()
        tree = self.build_directory_tree()[0]

        return

    def publish(self, debug=False):
        '''
        This function creates the new directory tree for the library
        :param path:
        :return:
        '''
        try:
            new_basename_list = self.tUpdated.get_tree_basename()
            old_basename_list = self.tOriginal.get_tree_basename()

            basedir = os.getcwd()
            basedir_dest = basedir + '/result'
            file_index_list = []
            dir_index_list = []

            # First we split the data into directory type of file type so we can create
            # the new directory structure and then move the files to the new location.
            for index in range(1, len(old_basename_list), 1):
                current_item = basedir + old_basename_list[index]
                if os.path.isfile(current_item):
                    file_index_list.append(index)

                if os.path.isdir(current_item):
                    if os.listdir(current_item) != []:
                        dir_index_list.append(index)

            # TODO: cambiar os.path.join(a,b) para compatibilidad con linux y windows
            # Second we create the new directory tree and then we move + rename the files to it's new location.
            for index in range(len(old_basename_list), len(new_basename_list), 1):
                new_file = basedir_dest + new_basename_list[index]
                if not os.path.exists(new_file):
                    if debug:
                        print ('Publish :: Creating {new_dir}').format(new_dir=new_file)
                    os.makedirs(new_file)

            for index in dir_index_list:
                new_file = basedir_dest + new_basename_list[index]
                if not os.path.exists(new_file):
                    if debug:
                        print ('Publish :: Creating {old_dir}').format(old_dir=new_file)
                    os.makedirs(new_file)

            for index in file_index_list:
                new_file = basedir_dest + new_basename_list[index]
                old_file = basedir + old_basename_list[index]
                try:
                    if debug:
                        print ('Publish :: Moving {new_file}').format(new_file=new_file)
                    os.rename(old_file, new_file)
                except Exception as e:
                    if debug:
                        print ('Publish :: Error moving: {old_file} to {new_file}: error: {error}\n').format(
                            old_file=old_file, new_file=new_file, error=str(e))
        except Exception as e:
            if debug:
                print ('Publish :: error: {error}').format(error=str(e))
