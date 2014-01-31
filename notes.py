# http://stackoverflow.com/questions/4628122/how-to-construct-a-timedelta-object-from-a-simple-string

32m
2h32m
3d2h32m
1w3d2h32m
1w 3d 2h 32m
1 w 3 d 2 h 32 m
4:13
4:13:02
4:13:02.266
2:04:13:02.266
2 days,  4:13:02         # uptime format
2 days,  4:13:02.266
5hr34m56s
5 hours, 34 minutes, 56 seconds
5 hrs, 34 mins, 56 secs
2 days, 5 hours, 34 minutes, 56 seconds
1.2 m
1.2 min
1.2 mins
1.2 minute
1.2 minutes
172 hours
172 hr
172 h
172 hrs
172 hour
1.24 days
5 d
5 day
5 days
5.6 wk
5.6 week
5.6 weeks
3.1 months
12.24 year
12.24 years
12.24 yr
12.24 y
12 years, 3 months, 2 days, 5 hours, 34 minutes, 56 seconds
12 years, 3 months, 2 days,  4:13:02

# http://stackoverflow.com/questions/538666/python-format-timedelta-to-string
# standard format using
# str(datetime.timedelta(hours=10.56))



def interpret_time_since ( s ):
    '''Attempts to parse a "time since", such as 5.6 wk.  If successful,
    returns the time referred to.'''
    m = re.match ( r'^([0-9.]+)\s*([a-z]*)$', s.strip().lower() )
    if m is not None:
        number, units = m.groups()
        if not units:
            units = ''
        number, units = float(number), units.strip()
        if units in [ 'm', 'min', 'mins', 'minute', 'minutes' ]:
            return ( datetime.datetime.now() -
                     datetime.timedelta ( minutes = number ) )
        elif units in [ 'h', 'hr', 'hrs', 'hour', 'hours' ]:
            return ( datetime.datetime.now() -
                     datetime.timedelta ( hours = number ) )
        elif units in [ 'd', 'day', 'days' ]:
            return ( datetime.datetime.now() -
                     datetime.timedelta ( days = number ) )
        elif units in [ 'w', 'week', 'weeks' ]:
            return ( datetime.datetime.now() -
                     datetime.timedelta ( weeks = number ) )
        elif units in [ 'y', 'year', 'years' ]:
            return ( datetime.datetime.now() -
                     datetime.timedelta ( weeks = number * 52 ) )
    assert False
