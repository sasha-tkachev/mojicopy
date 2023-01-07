"""
Based on https://gist.github.com/shello/efa2655e8a7bce52f273
"""

from bisect import bisect
from itertools import accumulate
from random import randrange

# Set the unicode version.
# Your system may not support Unicode 7.0 charecters just yet! So hipster.
_DEFAULT_UNICODE_VERSION = 6

# Sauce: http://www.unicode.org/charts/PDF/U1F300.pdf
_EMOJI_RANGES_UNICODE = {
    6: [
        ("\U0001F300", "\U0001F320"),
        ("\U0001F330", "\U0001F335"),
        ("\U0001F337", "\U0001F37C"),
        ("\U0001F380", "\U0001F393"),
        ("\U0001F3A0", "\U0001F3C4"),
        ("\U0001F3C6", "\U0001F3CA"),
        ("\U0001F3E0", "\U0001F3F0"),
        ("\U0001F400", "\U0001F43E"),
        ("\U0001F440",),
        ("\U0001F442", "\U0001F4F7"),
        ("\U0001F4F9", "\U0001F4FC"),
        ("\U0001F500", "\U0001F53C"),
        ("\U0001F540", "\U0001F543"),
        ("\U0001F550", "\U0001F567"),
        ("\U0001F5FB", "\U0001F5FF"),
    ],
    7: [
        ("\U0001F300", "\U0001F32C"),
        ("\U0001F330", "\U0001F37D"),
        ("\U0001F380", "\U0001F3CE"),
        ("\U0001F3D4", "\U0001F3F7"),
        ("\U0001F400", "\U0001F4FE"),
        ("\U0001F500", "\U0001F54A"),
        ("\U0001F550", "\U0001F579"),
        ("\U0001F57B", "\U0001F5A3"),
        ("\U0001F5A5", "\U0001F5FF"),
    ],
    8: [
        ("\U0001F300", "\U0001F579"),
        ("\U0001F57B", "\U0001F5A3"),
        ("\U0001F5A5", "\U0001F5FF"),
    ],
}


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
    if emoji_range_idx is not 0:
        point_in_range = point - weight_distr[emoji_range_idx - 1]
    return point_in_range


def _emoji_character(emoji_range, point_in_range):
    return chr(ord(emoji_range[0]) + point_in_range)


def random_emoji(unicode_version=_DEFAULT_UNICODE_VERSION):
    if unicode_version in _EMOJI_RANGES_UNICODE:
        emoji_ranges = _EMOJI_RANGES_UNICODE[unicode_version]
    else:
        emoji_ranges = _EMOJI_RANGES_UNICODE[-1]

    weight_distr = _weighted_distribution(emoji_ranges)

    point = _single_point(weight_distr)

    emoji_range_idx, emoji_range = _correct_emoji_range(
        emoji_ranges, weight_distr, point
    )

    point_in_range = _index_in_range(weight_distr, point, emoji_range_idx)

    return _emoji_character(emoji_range, point_in_range)
