
# ------------------------------------------------------------
#  implementation
# ------------------------------------------------------------

from collections import defaultdict
import re

YEARS = r'(?P<years>\d+)\s*(?:ys?|yrs?.?|years?)'

MONTHS = r'(?P<months>\d+)\s*(?:mos?.?|mths?.?|months?)'

DAYS = r'(?P<days>\d+)\s*(?:d|dys?|days?)'

HOURS = r'(?P<hours>\d+)\s*(?:h|hrs?|hours?)'

MINS = r'(?P<mins>\d+)\s*(?:m|(mins?)|(minutes?))'

SECS = r'(?P<secs>\d+)\s*(?:s|secs?|seconds?)'

SEPARATORS = r'[,/]'

OPT    = lambda x: '(?:{x})?'.format(x=x, SEPARATORS=SEPARATORS)
OPTSEP = lambda x: '(?:{x}\s*(?:{SEPARATORS}\s*)?)?'.format(x=x, SEPARATORS=SEPARATORS)

#TIME = r'(?:{HOURS}\s*(?:{SEPARATORS}\s*)?)?(?:{MINS}\s*(?:{SEPARATORS}\s*)?\s*)?(?:{SECS})?'.format(HOURS=HOURS, SEPARATORS=SEPARATORS, MINS=MINS, SECS=SECS)

TIME = '{YEARS}\s*{MONTHS}\s*{DAYS}\s*{HOURS}\s*{MINS}\s*{SECS}'.format(
    YEARS=OPTSEP(YEARS),
    MONTHS=OPTSEP(MONTHS),
    DAYS=OPTSEP(DAYS),
    HOURS=OPTSEP(HOURS),
    MINS=OPTSEP(MINS),
    SECS=OPT(SECS))

#TIME = r'{HOURS}\s*{MINS}\s*{SECS}'.format(HOURS=HOURS, SEPARATORS=SEPARATORS, MINS=MINS, SECS=SECS)

def t(x, y):
    if re.match(x, y):
        print re.match(x, y).group(0)
        print re.match(x, y).groupdict()
#RE =


