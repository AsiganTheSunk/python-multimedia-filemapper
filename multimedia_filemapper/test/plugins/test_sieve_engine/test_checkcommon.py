from multimedia_filemapper.core.sieve_engine.extensions.sieve_anime_extension import SieveAnimeExtension
from multimedia_filemapper.core.sieve_engine.extensions.sieve_common_extension import SieveCommonExtension


sieve_common_extension = SieveCommonExtension()

MULTIMEDIA_FILE_SAMPLE_0 = 'multimedia_video_sample.mkv'
MULTIMEDIA_FILE_SAMPLE_1 = 'multimedia_video_sample.mp3'

SUBTITLE_FOLDER_SAMPLE_0 = 'multimpedia_directory_sample (sub)'
SUBTITLE_FOLDER_SAMPLE_1 = 'multimpedia_directory_sample (subs)'
SUBTITLE_FOLDER_SAMPLE_2 = 'multimpedia_directory_sample (subtitles)'
SUBTITLE_FOLDER_SAMPLE_3 = 'subtitles'
SUBTITLE_FOLDER_SAMPLE_4 = 'sub'
SUBTITLE_FOLDER_SAMPLE_5 = 'Subs'

SUBTITLE_FILE_SAMPLE_0 = 'multimedia_subitle_sample.srt'
SUBTITLE_FILE_SAMPLE_1 = 'multimedia_subitle_sample.ass'
SUBTITLE_FILE_SAMPLE_2 = 'multimedia_subitle_sample.sub'
check = SieveCommonExtension()

# Multimedia Check Tests
def test0_filemapper_check_multimedia():
    assert check.check_multimedia_extension('multimedia_video_sample.mkv') is True


def test1_filemapper_check_multimedia():
    assert check.check_multimedia_extension('multimedia_video_sample.mp4') is True


def test2_filemapper_check_multimedia():
    assert check.check_multimedia_extension('multimedia_video_sample.mp3') is False

# Multimedia Subtitle Directory Tests
def test0_filemapper_check_subtitles_directory():
    assert check.is_subtitle_folder('multimpedia_directory_sample (subtitle_engine)') is True


def test1_filemapper_check_subtitles_directory():
    assert check.is_subtitle_folder('multimpedia_directory_sample (subtitles)') is True


# TODO
def test2_filemapper_check_subtitles_directory():
    assert check.is_subtitle_folder('multimpedia_directory_sample (sub)') is True

# TODO
def test3_filemapper_check_subtitles_directory():
    assert check.is_subtitle_folder('multimpedia_directory_sample (subtitle_engine)') is True


#Multimedia Subtitle File Tests
def test0_filemapper_check_subtitle_file():
    assert check.check_subtitles_extension('multimedia_subitle_sample.srt') is True


def test1_filemapper_check_subtitle_file():
    assert check.check_subtitles_extension('multimedia_subitle_sample.ass') is True


def test2_filemapper_check_subtitle_file():
    assert check.check_subtitles_extension('multimedia_subitle_sample.sub') is True
