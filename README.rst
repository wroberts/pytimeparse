======================================
 timeparse.py: time expression parser
======================================

Copyright (c) 2014 Will Roberts <wildwilhelm@gmail.com>

Licensed under the MIT License (see source file ``timeparse.py`` for
details).

A small Python library to parse various kinds of time expressions,
inspired by
`this StackOverflow question <http://stackoverflow.com/questions/4628122/how-to-construct-a-timedelta-object-from-a-simple-string>`_.

The single function ``timeparse`` defined in the module parses time
expressions like the following:

- ``32m``
- ``2h32m``
- ``3d2h32m``
- ``1w3d2h32m``
- ``1w 3d 2h 32m``
- ``1 w 3 d 2 h 32 m``
- ``4:13``
- ``4:13:02``
- ``4:13:02.266``
- ``2:04:13:02.266``
- ``2 days,  4:13:02`` (``uptime`` format)
- ``2 days,  4:13:02.266``
- ``5hr34m56s``
- ``5 hours, 34 minutes, 56 seconds``
- ``5 hrs, 34 mins, 56 secs``
- ``2 days, 5 hours, 34 minutes, 56 seconds``
- ``1.2 m``
- ``1.2 min``
- ``1.2 mins``
- ``1.2 minute``
- ``1.2 minutes``
- ``172 hours``
- ``172 hr``
- ``172 h``
- ``172 hrs``
- ``172 hour``
- ``1.24 days``
- ``5 d``
- ``5 day``
- ``5 days``
- ``5.6 wk``
- ``5.6 week``
- ``5.6 weeks``

It returns the time as a number of seconds (an integer value of
possible, otherwise a floating-point number)::

    from timeparse.timeparse import timeparse
    >>> timeparse('1.2 minutes')
    72

A number of seconds can be converted back into a string using the
``datetime`` module in the standard library, as noted in
`this other StackOverflow question <http://stackoverflow.com/questions/538666/python-format-timedelta-to-string>`_::

    from timeparse.timeparse import timeparse
    import datetime
    >>> timeparse('10:33:36')
    38016
    >>> str(datetime.timedelta(seconds=38016))
    '10:33:36'

Future work
-----------

1. Give the user more flexibility over which characters to use as
   separators between fields in a time expression (e.g., ``+`` might
   be useful).
