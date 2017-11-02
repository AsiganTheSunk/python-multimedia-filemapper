#!/usr/bin/python

import os

from check.checkengine import CheckEngine
from metadata.metadata import Metadata
from metadata.metadataengine import MetadataEngine
from metadata.metadatatree import MetadataTree
from pandas.pandasengine import PandasEngine
from sbuilder.stringbuilder import StringBuilder
from utils.fileflags import FileFlags as fflags


class FileMapper():
    def __init__(self, basedir):
        self.basedir = basedir
        self.directory_dict = {}
        self.multimedia_source = []

        self.tOriginal = MetadataTree()
        self.tUpdated = MetadataTree()

        self.metadata_engine = MetadataEngine()
        self.check_engine = CheckEngine()
        self.string_builder = StringBuilder()

    def add_source(self, path):
        self.multimedia_source.append(path)

    def get_sources(self):
        for item in self.multimedia_source:
            print item

    def set_tupdated(self, tree):
        self.tUpdated = tree

    def premap(self, verbose=False, debug=False):
        '''
        This function pre-maps the contents of the directory from a given path
        :param path:
        :param verbose:
        :return:
        '''
        if debug:
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8
            print 'CheckEngine  ::'
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8

        for root, directories, files in os.walk(self.basedir):
            for directory in directories:
                try:
                    if self.check_engine.check_main_directory(stream=directory, verbose=verbose, debug=debug):
                        if not os.listdir(os.path.join(root, directory)) == []:
                            self.directory_dict[
                                str(os.path.abspath(os.path.join(root, directory)))] = fflags.MAIN_SHOW_DIRECTORY_FLAG
                    elif self.check_engine.check_show_subtitles_directory(stream=directory, verbose=verbose,
                                                                          debug=debug):
                        self.directory_dict[
                            str(os.path.abspath(os.path.join(root, directory)))] = fflags.SUBTITLE_DIRECTORY_SHOW_FLAG
                    elif self.check_engine.check_anime_subtitles_directory(stream=directory, verbose=verbose,
                                                                           debug=debug):
                        self.directory_dict[
                            str(os.path.abspath(os.path.join(root, directory)))] = fflags.SUBTITLE_DIRECTORY_ANIME_FLAG
                    elif self.check_engine.check_film_subtitles_directory(stream=directory, verbose=verbose,
                                                                          debug=debug):
                        self.directory_dict[
                            str(os.path.abspath(os.path.join(root, directory)))] = fflags.SUBTITLE_DIRECTORY_FILM_FLAG
                    elif self.check_engine.check_show_directory(stream=directory, verbose=verbose, debug=debug):
                        self.directory_dict[
                            str(os.path.abspath(os.path.join(root, directory)))] = fflags.SHOW_DIRECTORY_FLAG
                    elif self.check_engine.check_anime_directory(stream=directory, verbose=verbose, debug=debug):
                        self.directory_dict[
                            str(os.path.abspath(os.path.join(root, directory)))] = fflags.ANIME_DIRECTORY_FLAG
                    elif self.check_engine.check_season_directory(stream=directory, verbose=verbose, debug=debug):
                        if not os.listdir(os.path.join(root, directory)) == []:
                            self.directory_dict[
                                str(os.path.abspath(os.path.join(root, directory)))] = fflags.SEASON_DIRECTORY_FLAG
                    elif self.check_engine.check_film(stream=directory, verbose=verbose, debug=debug):
                        self.directory_dict[
                            str(os.path.abspath(os.path.join(root, directory)))] = fflags.FILM_DIRECTORY_FLAG
                    else:
                        self.directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = fflags.UNKOWN_FLAG

                except Exception as e:
                    continue

            for file_ in files:
                try:
                    if self.check_engine.check_unwanted(file_):
                        continue
                    elif self.check_engine.check_show_subtitles(file_, verbose=verbose, debug=debug):
                        self.directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = fflags.SUBTITLE_SHOW_FLAG
                    elif self.check_engine.check_film_subtitles(file_, verbose=verbose, debug=debug):
                        self.directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = fflags.SUBTITLE_FILM_FLAG
                    elif self.check_engine.check_anime_subtitles(file_, verbose=verbose, debug=debug):
                        self.directory_dict[
                            str(os.path.abspath(os.path.join(root, file_)))] = fflags.SUBTITLE_ANIME_FLAG
                    elif self.check_engine.check_show(file_, verbose=verbose, debug=debug):
                        self.directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = fflags.SHOW_FLAG
                    elif self.check_engine.check_film(file_, verbose=verbose, debug=debug):
                        self.directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = fflags.FILM_FLAG
                    elif self.check_engine.check_anime(file_, verbose=verbose, debug=debug):
                        self.directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = fflags.ANIME_FLAG
                    else:
                        self.directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = fflags.UNKOWN_FLAG
                except Exception as e:
                    continue

        print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8
        if debug:
            print
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8
            print 'CheckEngine  :: results'
            self.list_directory(self.directory_dict)
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8
        return self.directory_dict

    def list_directory(self, dict):
        '''
        This function log the pre-map function into a file
        :param dict:
        :return: DIRECTORY
        '''
        for item in sorted(dict):
            print('  :: item: {item} : fflag: {fflag}').format(item=item, fflag=dict[item])

    def build_directory_tree(self, verbose=False, debug=False):
        '''
        This function creates a tree data structure from a given dictionary
        :param basedir:
        :param directory:
        :param verbose:
        :param debug:
        :param deep:
        :return:
        '''
        try:
            basedir = self.basedir
            metadata = Metadata()
            parent_metadata = Metadata()
            new_basename = ''
            new_parent_basename = ''

            self.tOriginal.add_node(basename=str(os.path.basename(basedir)))
            self.tUpdated.add_node(basename=str(os.path.basename(basedir)))
            if debug:
                print('MetadataTree ::')
                print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8
            for item in sorted(self.directory_dict):
                len_aux = len(str(os.path.basename(item)))
                parent = item[:-len_aux - 1]
                metadata = self.metadata_engine.map(stream=str(item), fflag=self.directory_dict[item], verbose=verbose,
                                                    debug=debug)
                new_basename = self.string_builder.rebuild_name(metadata=metadata)

                if parent in basedir:
                    parent_metadata = self.metadata_engine.map(stream=str(parent), fflag=fflags.LIBRARY_FLAG,
                                                               verbose=verbose, debug=debug)
                    new_parent_basename = self.string_builder.rebuild_name(metadata=parent_metadata)
                else:
                    parent_metadata = self.metadata_engine.map(stream=str(parent), fflag=self.directory_dict[parent],
                                                               verbose=verbose, debug=debug)
                    new_parent_basename = self.string_builder.rebuild_name(metadata=parent_metadata)

                self.tOriginal.add_node(basename=str(os.path.basename(item)), metadata=metadata,
                                        parent_basename=str(os.path.basename(parent)))
                self.tUpdated.add_node(basename=str(new_basename), metadata=metadata,
                                       parent_basename=str(new_parent_basename))
                if debug:
                    print(
                        'MetadataTree :: fflag: {fflag} : input_basename: {ibasename} input_parent: {iparentbasename}').format(
                        fflag=str(self.directory_dict[item]),
                        ibasename=str(os.path.basename(item)),
                        iparentbasename=str(os.path.basename(parent)))

                    print(
                        'MetadataTree :: fflag: {fflag} : input_basename: {obasename} input_parent: {oparentbasename}').format(
                        fflag=str(self.directory_dict[item]),
                        obasename=str(new_basename),
                        oparentbasename=str(new_parent_basename))
            if debug:
                print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8
        except Exception as e:
            print (str('build-directory-tree: ') + str(e))
        else:
            return [self.tUpdated, self.tOriginal]

    def map(self, verbose=False, debug=False):
        '''

        :param basedir:
        :param verbose:
        :param debug:
        :return:
        '''
        self.premap(verbose=verbose, debug=True)
        tree = self.build_directory_tree(verbose=verbose, debug=False)
        pandas_engine = PandasEngine(tree=tree[0])
        pandas_engine.create_library(debug=debug)
        tree = pandas_engine.update_tree(debug=debug)
        self.set_tupdated(tree=tree)

        list = self.tUpdated.get_abs_paths()
        for item in list:
            print item

    def test_map(self, verbose=False, debug=False):
        '''

        :param basedir:
        :param verbose:
        :param debug:
        :return:
        '''
        self.premap(verbose=verbose, debug=debug)
        tree = self.build_directory_tree(verbose=verbose, debug=debug)[0]

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
