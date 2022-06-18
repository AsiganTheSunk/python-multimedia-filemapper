#!/usr/bin/python


class Library:
    def __init__(self, default_dest):
        '''

        :param default_dest:
        '''
        self.default_dest = default_dest
        self.default_film_dest = self.default_dest
        self.default_show_dest = self.default_dest
        self.default_anime_dest = self.default_dest

    def get_default_dest(self):
        '''

        :return:
        '''
        return self.default_dest

    def get_default_film_dest(self):
        '''

        :return:
        '''
        return self.default_film_dest

    def get_default_show_dest(self):
        '''

        :return:
        '''
        return self.default_show_dest

    def get_default_anime_dest(self):
        '''

        :return:
        '''
        return self.default_anime_dest

    def set_default_dest(self, value):
        '''

        :param value:
        :return:
        '''
        self.default_dest = value
        return self.default_dest

    def set_default_film_dest(self, value):
        '''

        :param value:
        :return:
        '''
        self.default_film_dest = value
        return

    def set_default_show_dest(self, value):
        '''

        :param value:
        :return:
        '''
        self.default_show_dest = value
        return self.default_show_dest

    def set_default_anime_dest(self, value):
        '''

        :param value:
        :return:
        '''
        self.default_anime_dest = value
        return self.default_anime_dest
