# def premap(self):
#     '''
#     This function pre-maps the contents of the directory from a given path
#     :param path:
#     :param verbose:
#     :return:
#     '''
#
#     self.logger.info('{0}'.format(self.name))
#     # need to count instances, so len(directories) + len(files) / cpu_count()
#
#     for root, folders, files in os.walk(self.basedir):
#         for multimedia_folder in folders:
#             try:
#                 if self.sieve_engine.is_multimedia_folder(stream=multimedia_folder):
#                     if not os.listdir(os.path.join(root, multimedia_folder)) == []:
#                         self.directory_dict[
#                             str(os.path.abspath(os.path.join(root, multimedia_folder)))
#                         ] = fflags.MAIN_SHOW_DIRECTORY_FLAG
#
#                     elif self.sieve_engine.is_show_subtitle_folder(stream=multimedia_folder):
#                         self.directory_dict[
#                             str(os.path.abspath(os.path.join(root, multimedia_folder)))
#                         ] = fflags.SUBTITLE_DIRECTORY_SHOW_FLAG
#
#                     elif self.sieve_engine.is_anime_subtitle_folder(stream=multimedia_folder):
#                         self.directory_dict[
#                             str(os.path.abspath(os.path.join(root, multimedia_folder)))
#                         ] = fflags.SUBTITLE_DIRECTORY_ANIME_FLAG
#
#                     elif self.sieve_engine.is_film_subtitle_folder(stream=multimedia_folder):
#                         self.directory_dict[
#                             str(os.path.abspath(os.path.join(root, multimedia_folder)))
#                         ] = fflags.SUBTITLE_DIRECTORY_FILM_FLAG
#
#                     elif self.sieve_engine.is_show_folder(stream=multimedia_folder):
#                         self.directory_dict[
#                             str(os.path.abspath(os.path.join(root, multimedia_folder)))
#                         ] = fflags.SHOW_DIRECTORY_FLAG
#
#                     elif self.sieve_engine.is_anime_folder(stream=multimedia_folder):
#                         self.directory_dict[
#                             str(os.path.abspath(os.path.join(root, multimedia_folder)))
#                         ] = fflags.ANIME_DIRECTORY_FLAG
#
#                     elif self.sieve_engine.is_season_folder(stream=multimedia_folder):
#                         if not os.listdir(os.path.join(root, multimedia_folder)) == []:
#                             self.directory_dict[
#                                 str(os.path.abspath(os.path.join(root, multimedia_folder)))
#                             ] = fflags.SEASON_DIRECTORY_FLAG
#
#                     elif self.sieve_engine.is_film_folder(stream=multimedia_folder):
#                         self.directory_dict[
#                             str(os.path.abspath(os.path.join(root, multimedia_folder)))
#                         ] = fflags.FILM_DIRECTORY_FLAG
#
#                     else:
#                         self.directory_dict[
#                             str(os.path.abspath(os.path.join(root, multimedia_folder)))
#                         ] = fflags.UNKOWN_FLAG
#
#             except Exception as e:
#                 continue
#
#         for _multimedia_file in files:
#             try:
#                 if self.sieve_engine.check_unwanted(_multimedia_file):
#                     continue
#                 elif self.sieve_engine.check_show_subtitles(_multimedia_file):
#                     self.directory_dict[
#                         str(os.path.abspath(os.path.join(root, _multimedia_file)))
#                     ] = fflags.SUBTITLE_SHOW_FLAG
#
#                 elif self.sieve_engine.check_film_subtitles(_multimedia_file):
#                     self.directory_dict[
#                         str(os.path.abspath(os.path.join(root, _multimedia_file)))
#                     ] = fflags.SUBTITLE_FILM_FLAG
#
#                 elif self.sieve_engine.check_anime_subtitles(_multimedia_file):
#                     self.directory_dict[
#                         str(os.path.abspath(os.path.join(root, _multimedia_file)))
#                     ] = fflags.SUBTITLE_ANIME_FLAG
#
#                 elif self.sieve_engine.check_show(_multimedia_file):
#                     self.directory_dict[
#                         str(os.path.abspath(os.path.join(root, _multimedia_file)))
#                     ] = fflags.SHOW_FLAG
#
#                 elif self.sieve_engine.check_film(_multimedia_file):
#                     self.directory_dict[
#                         str(os.path.abspath(os.path.join(root, _multimedia_file)))
#                     ] = fflags.FILM_FLAG
#
#                 elif self.sieve_engine.check_anime(_multimedia_file):
#                     self.directory_dict[
#                         str(os.path.abspath(os.path.join(root, _multimedia_file)))
#                     ] = fflags.ANIME_FLAG
#
#                 else:
#                     self.directory_dict[
#                         str(os.path.abspath(os.path.join(root, _multimedia_file)))
#                     ] = fflags.UNKOWN_FLAG
#
#             except Exception as e:
#                 continue
#
#     return self.directory_dict

# @staticmethod
# def sieve_directories(_root, _directory):
#     sieve_engine = SieveEngine()
#     try:
#         if sieve_engine.is_multimedia_folder(_directory):
#             if not os.listdir(os.path.join(_root, _directory)) == []:
#                 return str(os.path.abspath(os.path.join(_root, _directory))), fflags.MAIN_SHOW_DIRECTORY_FLAG
#         elif sieve_engine.is_show_subtitle_folder(_directory):
#             return str(os.path.abspath(os.path.join(_root, _directory))), fflags.SUBTITLE_DIRECTORY_SHOW_FLAG
#         elif sieve_engine.is_anime_subtitle_folder(_directory):
#             return str(os.path.abspath(os.path.join(_root, _directory))), fflags.SUBTITLE_DIRECTORY_ANIME_FLAG
#         elif sieve_engine.is_film_subtitle_folder(_directory):
#             return str(os.path.abspath(os.path.join(_root, _directory))), fflags.SUBTITLE_DIRECTORY_FILM_FLAG
#         elif sieve_engine.is_show_folder(_directory):
#             return str(os.path.abspath(os.path.join(_root, _directory))), fflags.SHOW_DIRECTORY_FLAG
#         elif sieve_engine.is_anime_folder(_directory):
#             return str(os.path.abspath(os.path.join(_root, _directory))), fflags.ANIME_DIRECTORY_FLAG
#         elif sieve_engine.is_season_folder(_directory):
#             if not os.listdir(os.path.join(_root, _directory)) == []:
#                 return str(os.path.abspath(os.path.join(_root, _directory))), fflags.SEASON_DIRECTORY_FLAG
#         elif sieve_engine.check_film(_directory):
#             return str(os.path.abspath(os.path.join(_root, _directory))), fflags.FILM_DIRECTORY_FLAG
#         else:
#             return str(os.path.abspath(os.path.join(_root, _directory))), fflags.UNKOWN_FLAG
#     except WindowsError as err:
#         if err.winerror == 3:
#             print('log file not found')
#     except Exception as err:
#         print('<< Fatal >>', err)


# def build_directory_tree(self):
#     """
#     This function creates a tree data structure from a given dictionary
#     :param basedir:
#     :param directory:
#     :param deep:
#     :return:
#     """
#     try:
#         basedir = self.basedir
#         metadata = Metadata()
#         parent_metadata = Metadata()
#         new_basename = ''
#         new_parent_basename = ''
#
#         self.tOriginal.add_node(basename=str(os.path.basename(basedir)))
#         self.tUpdated.add_node(basename=str(os.path.basename(basedir)))
#         # if debug:
#         #     print('MetadataTree ::')
#         #     print('~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8)
#         for item in sorted(self.directory_dict):
#             len_aux = len(str(os.path.basename(item)))
#             parent = item[:-len_aux - 1]
#             metadata = self.metadata_engine.map(stream=str(item), fflag=self.directory_dict[item])
#             new_basename = self.string_builder.rebuild_name(metadata=metadata)
#
#             if parent in basedir:
#                 parent_metadata = self.metadata_engine.map(stream=str(parent), fflag=fflags.LIBRARY_FLAG)
#                 new_parent_basename = self.string_builder.rebuild_name(metadata=parent_metadata)
#             else:
#                 parent_metadata = self.metadata_engine.map(stream=str(parent), fflag=self.directory_dict[parent])
#                 new_parent_basename = self.string_builder.rebuild_name(metadata=parent_metadata)
#
#             self.tOriginal.add_node(basename=str(os.path.basename(item)), metadata=metadata,
#                                     parent_basename=str(os.path.basename(parent)))
#
#             self.tUpdated.add_node(basename=str(new_basename), metadata=metadata,
#                                    parent_basename=str(new_parent_basename))
#
#         #     if debug:
#         #         print(
#         #             'MetadataTree :: fflag: {fflag} : input_basename: {ibasename} input_parent: {iparentbasename}').format(
#         #             fflag=str(self.directory_dict[item]),
#         #             ibasename=str(os.path.basename(item)),
#         #             iparentbasename=str(os.path.basename(parent)))
#         #
#         #         print(
#         #             'MetadataTree :: fflag: {fflag} : input_basename: {obasename} input_parent: {oparentbasename}').format(
#         #             fflag=str(self.directory_dict[item]),
#         #             obasename=str(new_basename),
#         #             oparentbasename=str(new_parent_basename))
#         # if debug:
#         #     print('~~~~~~~~~~~~~~~~~~~~~~~~~~' * 8)
#
#     except Exception as e:
#         print(str('build-directory-tree: ') + str(e))
#     else:
#         return [self.tUpdated, self.tOriginal]