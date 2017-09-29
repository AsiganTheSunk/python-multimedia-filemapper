#!/usr/bin/python

class Library:
    def __init__(self, default_dest):
        self.default_dest = default_dest
        self.default_film_dest = self.default_dest
        self.default_show_dest = self.default_dest
        self.default_anime_dest = self.default_dest
        self.library_list = []

    def get_default_dest(self):
        return self.default_dest

    def get_default_film_dest(self):
        return self.default_film_dest

    def get_default_show_dest(self):
        return self.default_show_dest

    def get_default_anime_dest(self):
        return self.default_anime_dest

    def set_default_dest(self, value):
        self.default_dest = value
        return self.default_dest

    def set_default_film_dest(self, value):
        self.default_film_dest = value
        return

    def set_default_show_dest(self, value):
        self.default_show_dest = value
        return self.default_show_dest

    def set_default_anime_dest(self, value):
        self.default_anime_dest = value
        return self.default_anime_dest

    def add_library_source(self, path):
        try:
            return self.library_list.append(path)
        except:
            return None

    def remove_library_source(self, path):
        return self.library_list.remove(path)

    def list_library_source(self):
        for i in self.library_list:
            print (self.library_list[i])