from filemapper.check.checkcommonextension import CheckCommonExtension

check = CheckCommonExtension()
# Multimedia Check Tests
def test0_filemapper_check_multimedia():
    assert check.check_multimedia('multimedia_video_sample.mkv') is True


def test1_filemapper_check_multimedia():
    assert check.check_multimedia('multimedia_video_sample.mp4') is True


def test2_filemapper_check_multimedia():
    assert check.check_multimedia('multimedia_video_sample.mp3') is False

# Multimedia Subtitle Directory Tests
def test0_filemapper_check_subtitles_directory():
    assert check.check_subtitles_directory('multimpedia_directory_sample (subs)') is True


def test1_filemapper_check_subtitles_directory():
    assert check.check_subtitles_directory('multimpedia_directory_sample (subtitles)') is True


# TODO
def test2_filemapper_check_subtitles_directory():
    assert check.check_subtitles_directory('multimpedia_directory_sample (sub)') is True

# TODO
def test3_filemapper_check_subtitles_directory():
    assert check.check_subtitles_directory('multimpedia_directory_sample (subs)') is True


#Multimedia Subtitle File Tests
def test0_filemapper_check_subtitle_file():
    assert check.check_subtitles('multimedia_subitle_sample.srt') is True


def test1_filemapper_check_subtitle_file():
    assert check.check_subtitles('multimedia_subitle_sample.ass') is True


def test2_filemapper_check_subtitle_file():
    assert check.check_subtitles('multimedia_subitle_sample.sub') is True
