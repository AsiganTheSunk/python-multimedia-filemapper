from filemapper.datastructure.FileFlags import FileFlags as fflags
import tvdb_api

class TVDbExtension():
    def __init__(self):
        self.name = 'TDVbExtension'
        self.tvdb = tvdb_api.Tvdb()
        self.supported_fflags = [fflags.SHOW_FLAG, fflags.SHOW_DIRECTORY_FLAG, fflags]
        return

    def get_genre(self, name, debug=False):
        '''
         This function retrieves genre values from a given show using tvdb_api
        :param name: It represents the input string you're parsing
        :param debug: It represents the debug status of the function, default it's False
        :return: GENRE
        '''
        try:
            genres = self.t[name]['genre']
            genre = genres[1:-1].split('|')[0]
        except tvdb_api.tvdb_error or tvdb_api.tvdb_episodenotfound:
            # raise error that would be corrected in ReEngine turning exception into blank field
            genre = ''
            return genre
        else:
            if debug:
                print('{extension_engine}: {stream} :: {value}').format(extension_engine=self.name,
                                                                        stream=name,
                                                                        value=genre)
            return genre

    def get_episode_name(self, name, season, episode, debug=False):
        '''
        This function retrieves episode name values from a given show using tvdb_api
        :param name: It represents the name of the show you're searching for
        :param season: It represents the season of the show you're searching for
        :param episode: It represents the episode of the show you're searching for
        :param debug: It represents the debug status of the function, default it's False
        :return: EPISODE_NAME
        '''
        try:
            episode = self.tvdb[name][int(season)][int(episode)]
        except tvdb_api.tvdb_error or tvdb_api.tvdb_episodenotfound:
            # raise error that would be corrected in ReEngine turning exception into blank field
            episode_name = ''
            return episode_name
        else:
            episode_name = episode['episodename']
            if debug:
                print('{extension_engine}: {stream0},{stream1} :: {value}').format(extension_engine=self.name,
                                                                                   stream0=name, stream1=season,
                                                                                   value=episode_name)
            return episode['episodename']


    def get_number_of_season_episodes(self, name, season, debug=False):
        '''
        This function retrieves number of episodes per season from a given show using tvdb_api
        :param name: It represents the name of the show you're searching for
        :param season: It represents the season of the show you're searching for
        :return: EPISODE_COUNT
        '''
        try:
            episode_count =  len(self.tvdb[name][int(season)])
        except tvdb_api.tvdb_error or tvdb_api.tvdb_episodenotfound:
            # raise error that would be corrected in ReEngine turning exception into blank field
            episode_count = 0
            return episode_count
        else:
            if debug:
                print('{extension_engine}: {name},{season} :: {value}').format(extension_engine=self.name,
                                                                               name=name, season=season,
                                                                               value=episode_count)
            return episode_count


    def get_number_of_seasons(self, name, debug=False):
        '''
        This function retrieves number of seasons from a given show using tvdb_api
        :param name: It represents the name of the show you're searching for
        :return: SEASON_COUNT
        '''
        try:
            season_count = len(self.tvdb[name])
        except tvdb_api.tvdb_error or tvdb_api.tvdb_seasonnotfound:
            season_count = 0
            return season_count
        else:
            if debug:
                print('{extension_engine}: {name},{season} :: {value}').format(extension_engine=self.name,
                                                                               name=name,
                                                                               value=season_count)
            return season_count