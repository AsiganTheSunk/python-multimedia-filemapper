#!/usr/bin/python3
from os import getcwd
from os.path import normpath

from multimedia_filemapper.core.constants.media_file_flags import FileFlags
from multimedia_filemapper.core.cross_reference_engine.core.pandasengine import PandasEngine
from multimedia_filemapper.core.metadata_engine.plugins.regex_engine.core.regexengine import RegexEngine
from multimedia_filemapper.core.metadata_engine.plugins.regex_engine.extensions.regexfilmextension import \
    RegexFilmExtension
from multimedia_filemapper.core.metadata_engine.plugins.regex_engine.extensions.regexsubtitleextension import \
    RegexSubtitleExtension
from multimedia_filemapper.core.metadata_engine.plugins.subtitle_engine.extensions.subtitlesrtassextension import \
    SubtitleSrtAssExtension
from multimedia_filemapper.core.metadata_engine.struct_data.metadata import Metadata
from multimedia_filemapper.core.metadata_engine.struct_data.metadatatree import MetadataTree
from multimedia_filemapper.core.rename_engine.extensions.stringfilmextension import StringFilmExtension
from multimedia_filemapper.core.sieve_engine.core.sieve_engine import SieveEngine
from multimedia_filemapper.filemapper import FileMapper
from time import time

stream0 = 'D:\\Downloads\\New Movies\\Anthropoid.2016.1080p.BluRay.x265-RARBG\\Subs\\5_English.srt'
# Note: Alternative to for Tests
stream1 = 'D:\\Downloads\\New Movies\\Anthropoid.2016.1080p.BluRay.x265-RARBG\\Sub\\5_English.srt'
stream2 = 'D:\\Downloads\\New Movies\\Anthropoid.2016.1080p.BluRay.x265-RARBG\\Subtitle\\5_English.srt'
stream3 = 'D:\\Downloads\\New Movies\\Anthropoid.2016.1080p.BluRay.x265-RARBG\\Subtitles\\5_English.srt'

stream4 = 'D:\\Downloads\\New Movies\\Anthropoid.2016.1080p.BluRay.x265-RARBG\\Subs'
stream5 = 'D:\\Downloads\\New Movies\\Anthropoid.2016.1080p.BluRay.x265-RARBG\\Anthropoid.2016.1080p.BluRay.x265-RARBG.mkv'

# subtitle_str_extension = SubtitleSrtAssExtension()
# subtitle_language = subtitle_str_extension.get_language(stream0)
# print(subtitle_language)

# regex_subtitle_extension = RegexSubtitleExtension()
# print(regex_subtitle_extension.get_subtitles_directory(stream0))
# print(regex_subtitle_extension.get_subtitles_directory(stream1))
# print(regex_subtitle_extension.get_subtitles_directory(stream2))
# print(regex_subtitle_extension.get_subtitles_directory(stream3))

# film_folder_flag = FileFlags.FILM_DIRECTORY_FLAG
# film_file_flag = FileFlags.FILM_FLAG
# subtitle_film_file_flag = FileFlags.SUBTITLE_FILM_FLAG
# subtitle_film_folder_flag = FileFlags.SUBTITLE_DIRECTORY_FILM_FLAG
#
# regex_engine = RegexEngine()
#
#
# subtitle_folder_metadata = regex_engine.map(stream4, subtitle_film_folder_flag)
# string_film_extension = StringFilmExtension()
# print(string_film_extension.build_subtitle_name(subtitle_folder_metadata))

from os import rename, makedirs, listdir, remove
from os.path import exists, isfile, isdir, getsize


def publish(final_list_of_items, library_paths):
    """
    This function creates the new directory tree for the library
    :return:
    """
    try:
        # basedir = getcwd()
        # print(basedir)
        # basedir_dest = basedir + '/result'
        file_index_list = []
        dir_index_list = []

        # First we split the data into directory type of file type so we can create
        # the new directory structure and then move the files to the new location.
        print(f'total paths to review: {len(final_list_of_items)}')
        for old_path, new_path in final_list_of_items:
            if isfile(old_path):
                file_index_list.append((new_path, old_path))
            else:
                dir_index_list.append((new_path, old_path))
        print(f'len files: {len(file_index_list)} | len folders: {len(dir_index_list)}')

        for index, library_path in library_paths:
            # print(index, library_path)
            if not exists(library_path):
                print(f'Publish :: Creating {library_path}')
                makedirs(library_path)

        for new_path, _ in dir_index_list:
            if not exists(new_path):
                print(f'Publish :: Creating {new_path}')
                makedirs(new_path)

        for new_path, old_path in file_index_list:
            try:
                if not exists(new_path):
                    print(f'Publish :: Moving {new_path}')
                    rename(old_path, new_path)
                else:
                    if getsize(old_path) > getsize(new_path):
                        remove(new_path)
                        rename(old_path, new_path)
            except Exception as error:
                print(f'Publish :: Error moving: {old_path} to {new_path}: error: {error}\n')
    except Exception as error:
        print(f'Publish :: error: {error}')


def update_tree(multimedia_df):

    updated_metadata_tree = MetadataTree()
    libraries_df = multimedia_df[multimedia_df['fflag'] == FileFlags.LIBRARY_FLAG]

    multimedia_file_folder_df = multimedia_df[multimedia_df['fflag'] != FileFlags.LIBRARY_FLAG]
    multimedia_file_folder_df = multimedia_file_folder_df[multimedia_file_folder_df['fflag'] != FileFlags.UNKOWN_FLAG]

    print(multimedia_file_folder_df.shape[0])
    libraries_root = libraries_df['parent'].to_list()[0]
    libraries_base_names = libraries_df['basename'].tolist()

    updated_metadata_tree.add_node(basename=libraries_root)
    for library in libraries_base_names:
        library_metadata = Metadata(name=library)
        updated_metadata_tree.add_node(basename=library, parent_basename=libraries_root, metadata=library_metadata)

    lista_de_relacional_paths = dict()
    for _multimedia_index, _ in enumerate(multimedia_file_folder_df.index):
        # print(f'INDEX: {_multimedia_index}')
        try:
            _name = multimedia_file_folder_df.iloc[_multimedia_index]['name']
            _season = multimedia_file_folder_df.iloc[_multimedia_index]['season']
            _episode = multimedia_file_folder_df.iloc[_multimedia_index]['episode']
            _basename = multimedia_file_folder_df.iloc[_multimedia_index]['basename']
            _parent = multimedia_file_folder_df.iloc[_multimedia_index]['parent']
            _year = multimedia_file_folder_df.iloc[_multimedia_index]['year']
            _genre = multimedia_file_folder_df.iloc[_multimedia_index]['genre']
            _n_season = multimedia_file_folder_df.iloc[_multimedia_index]['n_season']
            _e_season = multimedia_file_folder_df.iloc[_multimedia_index]['e_season']
            _path = multimedia_file_folder_df.iloc[_multimedia_index]['path']
            # print(_basename, _parent)
            metadata = Metadata(name=_name, season=_season, episode=_episode, year=_year, genre=_genre, n_season=_n_season, e_season=_e_season)

            _node = updated_metadata_tree.add_node(basename=_basename, metadata=metadata, parent_basename=_parent)
            lista_de_relacional_paths[_node.identifier] = _path
        except Exception as error:
            print(f'rebuilding the tree {error}')

    # updated_metadata_tree.tree()
    # for metadata_node in updated_metadata_tree.nodes:
    #     basename_df = multimedia_file_folder_df.loc[multimedia_file_folder_df['basename'] == metadata_node.basename]
    #     parent_basename_df = basename_df.loc[basename_df['parent'] == basename_df.parent]
    #     print(parent_basename_df['path'].values)

    abs_paths = updated_metadata_tree.get_abs_paths()
    _offset = 4
    library_paths = abs_paths[:_offset]
    print(library_paths)
    final_list_of_items = []
    for index, items in enumerate(abs_paths[_offset:]):
        final_list_of_items.append((lista_de_relacional_paths[index + _offset], items[1]))
        print((lista_de_relacional_paths[index + _offset], items[1]))
    return final_list_of_items, library_paths


def main():
    start_time = time()
    file_mapper = FileMapper(basedir="D:\\Downloads\\New Movies")
    _tree = file_mapper.pre_map_multiprocessing()
    pandas_engine = PandasEngine()
    data_frame = pandas_engine.create_library(_tree)
    final_list_of_items, library_paths = update_tree(data_frame)
    publish(final_list_of_items, library_paths)
    print("--- %s seconds ---" % (time() - start_time))


if __name__ == '__main__':
    main()

