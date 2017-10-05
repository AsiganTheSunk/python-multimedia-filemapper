#!/usr/bin/python

from filemapper.FileMapper import FileMapper
import os

def file_mapper():
    basedir = str(os.getcwd()) + '/test-library'
    file_mapper = FileMapper()
    file_mapper.map(basedir=basedir, verbose=False, debug=True)
    file_mapper.publish(library=basedir)

def main():
    file_mapper()

if __name__ == '__main__':
    main()

# todo validar los cambios
