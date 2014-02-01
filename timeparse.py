
# ------------------------------------------------------------
#  implementation
# ------------------------------------------------------------

import re

#YEARS     = r'(?P<years>\d+)\s*(?:ys?|yrs?.?|years?)'
#MONTHS    = r'(?P<months>\d+)\s*(?:mos?.?|mths?.?|months?)'
WEEKS      = r'(?P<weeks>[\d.]+)\s*(?:w|wks?|weeks?)'
DAYS       = r'(?P<days>[\d.]+)\s*(?:d|dys?|days?)'
HOURS      = r'(?P<hours>[\d.]+)\s*(?:h|hrs?|hours?)'
MINS       = r'(?P<mins>[\d.]+)\s*(?:m|(mins?)|(minutes?))'
SECS       = r'(?P<secs>[\d.]+)\s*(?:s|secs?|seconds?)'
SEPARATORS = r'[,/]'

OPT    = lambda x: '(?:{x})?'.format(x=x, SEPARATORS=SEPARATORS)
OPTSEP = lambda x: '(?:{x}\s*(?:{SEPARATORS}\s*)?)?'.format(
    x=x, SEPARATORS=SEPARATORS)

TIME = '{WEEKS}\s*{DAYS}\s*{HOURS}\s*{MINS}\s*{SECS}'.format(
    #YEARS=OPTSEP(YEARS),
    #MONTHS=OPTSEP(MONTHS),
    WEEKS=OPTSEP(WEEKS),
    DAYS=OPTSEP(DAYS),
    HOURS=OPTSEP(HOURS),
    MINS=OPTSEP(MINS),
    SECS=OPT(SECS))

def t(x, y):
    if re.match(x, y):
        print re.match(x, y).group(0)
        print re.match(x, y).groupdict()

MULTIPLIERS = dict([
    #('years',  60 * 60 * 24 * 365),
    #('months', 60 * 60 * 24 * 30),
    ('weeks',   60 * 60 * 24 * 7),
    ('days',    60 * 60 * 24),
    ('hours',   60 * 60),
    ('mins',    60),
    ('secs',    1)
    ])

def timeparse(sval):
    match = re.match(TIME + r'\s*$', sval)
    if match and match.group(0).strip():
        mdict = match.groupdict()
        # if all of the fields are integer numbers
        if all(v.isdigit() for v in mdict.values() if v):
            return sum([MULTIPLIERS[k] * int(v, 10) for (k, v) in
                        mdict.items() if v is not None])
        # if SECS is an integer number
        elif ('secs' not in mdict or
              mdict['secs'] is None or
              mdict['secs'].isdigit()):
            # we will return an integer
            return (
                int(sum([MULTIPLIERS[k] * float(v) for (k, v) in
                         mdict.items() if k != 'secs' and v is not None])) +
                (int(mdict['secs'], 10) if mdict['secs'] else 0))
        else:
            # SECS is a float, we will return a float
            return sum([MULTIPLIERS[k] * float(v) for (k, v) in
                        mdict.items() if v is not None])
