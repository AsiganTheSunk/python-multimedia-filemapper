#!/usr/bin/python

from filemapper.FileMapper import FileMapper
from filemapper.metadata.MetadataEngine import MetadataEngine

import os
import guessit
from pipes import quote
import subprocess
import time

def file_mapper():
    basedir = str(os.getcwd()) + '/test-library'
    big_test = '/media/asigan/Pila/Peliculos/Peliculas'
    file_mapper = FileMapper(basedir=basedir)
    file_mapper.map(verbose=True, debug=False)
    #file_mapper.publish(debug=True)


def ttest():
    t0 = time.time()
    p = subprocess.Popen('guessit "Battle Royale (Batoru.Rowaiaru) (2000)" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Battle.Royale.(Batoru.Rowaiaru).(2000).(Special.Edition).CD1of2.DVDRiP.XviD-[ZeaL].mkv" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Howls_Moving_Castle_(2004)_[720p,HDTV,x264,DTS]-FlexGet" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Howls_Moving_Castle_(2004)_[720p,HDTV,x264,DTS]-FlexGet.mkv" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Un Espia y Medio (2016) [MicroHD 1080p][AC3 5.1-DTS 5.1-Castellano-AC3 5.1 Ingles+Subs][ES-EN]" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Un Espia y Medio (2016) [MicroHD 1080p][AC3 5.1-DTS 5.1-Castellano-AC3 5.1 Ingles+Subs][ES-EN].mkv" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Game Of Thrones S01E02 1080p" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Game Of Thrones S01E02 1080p.mkv" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv].mkv" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv]" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Un Espia y Medio (2016) [MicroHD 1080p][AC3 5.1-DTS 5.1-Castellano-AC3 5.1 Ingles+Subs][ES-EN].mkv" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Game Of Thrones S01E02 1080p" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Game Of Thrones S01E02 1080p.mkv" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv].mkv" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    p = subprocess.Popen('guessit "Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv]" ', stdout=subprocess.PIPE, shell=True)
    p.communicate()
    p.stdout.close()

    t1 = time.time() - t0
    print 'total time elapsed: ', t1

    t0 = time.time()
    basedir = str(os.getcwd()) + '/test-library'
    file_mapper = FileMapper(basedir=basedir)
    file_mapper.test_map()
    t1 = time.time() - t0
    print 'total time elapsed: ', t1

    return

def main():
    # file_mapper()
    ttest()

if __name__ == '__main__':
    main()

# todo validar los cambios
