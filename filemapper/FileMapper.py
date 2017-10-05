#!/usr/bin/python

import os

from utils.FileFlags import FileFlags as fflags
from filemapper.check.CheckEngine import CheckEngine
from filemapper.metadata.Metadata import Metadata
from filemapper.metadata.MetadataEngine import MetadataEngine
from filemapper.metadata.MetadataTree import MetadataTree
from filemapper.sbuilder.StringBuilder import StringBuilder


class FileMapper():
    def __init__(self):
        self.multimedia_source = []
        self.tOriginal = MetadataTree()
        self.tUpdated = MetadataTree()
        self.directory_dict = {}
        self.metadata_engine = MetadataEngine()
        self.check_engine = CheckEngine()
        self.string_builder = StringBuilder()

    def add_multimedia_source(self, path):
        self.multimedia_source.append(path)

    def premap(self, path, verbose=False, debug=False):
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

        for root, directories, files in os.walk(path):
            for directory in directories:
                try:
                    if self.check_engine.check_main_directory(stream=directory, verbose=verbose, debug=debug):
                        if not os.listdir(os.path.join(root, directory)) == []:
                            self.directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = fflags.MAIN_SHOW_DIRECTORY_FLAG
                    elif self.check_engine.check_show_subtitles_directory(stream=directory, verbose=verbose, debug=debug):
                        self.directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = fflags.SUBTITLE_DIRECTORY_SHOW_FLAG
                    elif self.check_engine.check_anime_subtitles_directory(stream=directory, verbose=verbose, debug=debug):
                        self.directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = fflags.SUBTITLE_DIRECTORY_ANIME_FLAG
                    elif self.check_engine.check_film_subtitles_directory(stream=directory, verbose=verbose, debug=debug):
                        self.directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = fflags.SUBTITLE_DIRECTORY_FILM_FLAG
                    elif self.check_engine.check_show_directory(stream=directory, verbose=verbose, debug=debug):
                        self.directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = fflags.SHOW_DIRECTORY_FLAG
                    elif self.check_engine.check_anime_directory(stream=directory, verbose=verbose, debug=debug):
                        self.directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = fflags.ANIME_DIRECTORY_FLAG
                    elif self.check_engine.check_season_directory(stream=directory, verbose=verbose, debug=debug):
                        if not os.listdir(os.path.join(root, directory)) == []:
                            self.directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = fflags.SEASON_DIRECTORY_FLAG
                    elif self.check_engine.check_film(stream=directory, verbose=verbose, debug=debug):
                        self.directory_dict[str(os.path.abspath(os.path.join(root, directory)))] = fflags.FILM_DIRECTORY_FLAG
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
                        self.directory_dict[str(os.path.abspath(os.path.join(root, file_)))] = fflags.SUBTITLE_ANIME_FLAG
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
            print('  :: item: {item} : fflag: {fflag}').format(item=item,fflag=dict[item])

    def build_directory_tree(self, basedir, verbose=False, debug=False):
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
                metadata = self.metadata_engine.map(stream=str(item), fflag=self.directory_dict[item], verbose=verbose, debug=debug)
                new_basename = self.string_builder.rebuild_name(metadata=metadata)

                if parent in basedir:
                    parent_metadata = self.metadata_engine.map(stream=str(parent), fflag=fflags.LIBRARY_FLAG, verbose=verbose, debug=debug)
                    new_parent_basename = self.string_builder.rebuild_name(metadata=parent_metadata)
                else:
                    parent_metadata = self.metadata_engine.map(stream=str(parent), fflag=self.directory_dict[parent], verbose=verbose, debug=debug)
                    new_parent_basename = self.string_builder.rebuild_name(metadata=parent_metadata)

                self.tOriginal.add_node(basename=str(os.path.basename(item)), metadata=metadata, parent_basename=str(os.path.basename(parent)))
                self.tUpdated.add_node(basename=str(new_basename), metadata=metadata, parent_basename=str(new_parent_basename))
                if debug:
                    print(
                        'MetadataTree :: fflag{fflag} : input_basename{ibasename} input_parent{iparentbasename}').format(
                        fflag=str(self.directory_dict[item]),
                        ibasename=str(os.path.basename(item)),
                        iparentbasename=str(os.path.basename(parent)))

                    print(
                        'MetadataTree :: fflag{fflag} : input_basename{obasename} input_parent{oparentbasename}').format(
                        fflag=str(self.directory_dict[item]),
                        obasename=str(new_basename),
                        oparentbasename=str(new_parent_basename))
            if debug:
                print '~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8
        except Exception as e:
            print (str('build-directory-tree: ') + str(e))
        else:
            return [self.tUpdated, self.tOriginal]

    # def publish_library(self, library):
    #     '''
    #     This function creates the new directory tree for the library
    #     :param old_tree:
    #     :param new_tree:
    #     :param library:
    #     :return:
    #     '''
    #     new_tree_list = self.tUpdated.build_full_path_tree()
    #     old_tree_list = self.tOriginal.build_full_path_tree()
    #
    #     basedir = os.getcwd()
    #     list_index_files = []
    #     list_index_dir = []
    #
    #     for index in range(1, len(old_tree_list), 1):
    #         current_item = basedir + old_tree_list[index]
    #         if os.path.isfile(current_item):
    #             list_index_files.append(index)
    #
    #         if os.path.isdir(current_item):
    #             if os.listdir(current_item) != []:
    #                 list_index_dir.append(index)
    #
    #     # TODO: cambiar os.path.join(a,b) para compatibilidad con linux y windows
    #     for index in range(len(old_tree_list), len(new_tree_list), 1):
    #         new_file = basedir + '/result' + new_tree_list[index]
    #         if not os.path.exists(new_file):
    #             os.makedirs(new_file)
    #
    #     for index in list_index_dir:
    #         new_file = basedir + '/result' +new_tree_list[index]
    #         if not os.path.exists(new_file):
    #             os.makedirs(new_file)
    #
    #     for index in list_index_files:
    #         new_file = basedir + '/result' + new_tree_list[index]
    #         old_file = basedir + old_tree_list[index]
    #         try:
    #             os.rename(old_file, new_file)
    #         except Exception as e:
    #             print 'Error Moving File {current_file}, {error}'.format(current_file=old_file, error=str(e))
    #
    #     try:
    #         library_basename = os.path.basename(library)
    #         shutil.rmtree(library, ignore_errors=True)
    #         os.rename(os.path.join(os.path.join(basedir, 'result'), library_basename), library)
    #         shutil.rmtree(os.path.join(basedir, 'result'), ignore_errors=True)
    #     except Exception as e:
    #         print e
