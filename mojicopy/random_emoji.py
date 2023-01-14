"""
Based on https://gist.github.com/shello/efa2655e8a7bce52f273
"""

from bisect import bisect
from itertools import accumulate
from random import randrange

from mojicopy.emoji_unicode import EMOJI_RANGES_UNICODE
from mojicopy.settings import RandomEmojiSettings


def _weighted_distribution(emoji_ranges):
    count = [ord(r[-1]) - ord(r[0]) + 1 for r in emoji_ranges]
    weight_distr = list(accumulate(count))
    return weight_distr


def _single_point(weight_distr):
    return randrange(weight_distr[-1])


def _correct_emoji_range(emoji_ranges, weight_distr, point):
    emoji_range_idx = bisect(weight_distr, point)
    emoji_range = emoji_ranges[emoji_range_idx]
    return emoji_range_idx, emoji_range


def _index_in_range(weight_distr, point, emoji_range_idx):
    point_in_range = point
    if emoji_range_idx != 0:
        point_in_range = point - weight_distr[emoji_range_idx - 1]
    return point_in_range


def _emoji_character(emoji_range, point_in_range):
    return chr(ord(emoji_range[0]) + point_in_range)


def random_emoji(settings: RandomEmojiSettings):
    emoji_ranges = EMOJI_RANGES_UNICODE[settings.unicode_version]

    weight_distr = _weighted_distribution(emoji_ranges)

    point = _single_point(weight_distr)

    emoji_range_idx, emoji_range = _correct_emoji_range(
        emoji_ranges, weight_distr, point
    )

    point_in_range = _index_in_range(weight_distr, point, emoji_range_idx)

    return _emoji_character(emoji_range, point_in_range)
