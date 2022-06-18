#!/usr/bin/env python3

# Show Patterns SieveEngine
SHOW_PATTERNS = {
    'file_pattern': r'(\w+.+)([s]\d{1,3}[e]\d{1,3}).?(?=(\d{3,4}p)?).*(\[.*\])?',
    'season_episode_pattern': r'([s]\d{1,2}[e]\d{1,2})',
    'season_directory_pattern': r'(\-|\s|\.)(\(|\[)?s(eason)?(\-|\s|\.)?(\d{1,2})(\)|\])?'
}

# Film Patterns SieveEngine
FILM_PATTERNS = {
    'file_pattern': r'(.*)(([1-2])([890])(\d{2}))(?!p)'
}

# Anime Patterns SieveEngine
ANIME_PATTERNS = {
    'anime_show_pattern': {
        'full_pattern': r'\[(\w+-?)*\](\s\w+)*\s(.?\s)?(\d{0,3}|E\w{0,6}.?\d{0,3})\s\(?\[?(\d{3,4}p|.*)\)?\]?(.mp4|.mkv)',
        'head_pattern': r'(^\[(\w+(\s|\-|.?))+\])',
        'tail_pattern': r'(\-)(.?)\d{1,3}|(x|E(pisode)?)(\s|\.|\-)?\d{1,3}'},

    'anime_directory_pattern': {
        'head_pattern': r'^\[(\w+(\s|\-|.?))+\]',
        'tail_pattern': r'\-(.?)\d{1,3}|(x|E(pisode)?)(\s|\.|\-)?\d{1,3}'}
    }

# Common Patterns Sieve Engine
COMMON_PATTERNS = {
    'unwanted_file_extension_patterns': r'(\.exe|\.com|\.txt|\.nfo)$',
    'multimedia_file_extension_patterns': r'(\.mkv|\.mp4\.avi)$',
    'subtitle_extension_patterns': r'(\.sub|\.srt|\.ass)$',
    'subtitle_directory_patterns': r'subtitle|subtitles|subs'
}
