from timeparse import *
import unittest

class TestRegexes(unittest.TestCase):

    def setUp(self):
        pass

    def test_mins(self):
        self.assertEqual(re.match(MINS, '32min').groupdict(),
                         {'mins': '32'})
        self.assertEqual(re.match(MINS, '32mins').groupdict(),
                         {'mins': '32'})
        self.assertEqual(re.match(MINS, '32minute').groupdict(),
                         {'mins': '32'})
        self.assertEqual(re.match(MINS, '32minutes').groupdict(),
                         {'mins': '32'})
        self.assertEqual(re.match(MINS, '32mins').groupdict(),
                         {'mins': '32'})
        self.assertEqual(re.match(MINS, '32min').groupdict(),
                         {'mins': '32'})

    def test_hrs(self):
        self.assertEqual(re.match(HOURS, '32h').groupdict(),
                         {'hours': '32'})
        self.assertEqual(re.match(HOURS, '32hr').groupdict(),
                         {'hours': '32'})
        self.assertEqual(re.match(HOURS, '32hrs').groupdict(),
                         {'hours': '32'})
        self.assertEqual(re.match(HOURS, '32hour').groupdict(),
                         {'hours': '32'})
        self.assertEqual(re.match(HOURS, '32hours').groupdict(),
                         {'hours': '32'})
        self.assertEqual(re.match(HOURS, '32 hours').groupdict(),
                         {'hours': '32'})
        self.assertEqual(re.match(HOURS, '32 h').groupdict(),
                         {'hours': '32'})

    def test_time(self):
            self.assertGreater(
                set(re.match(TIME + r'\s*$',
                             '16h32m64s  ').groupdict().iteritems()),
                set([('hours', '16'), ('mins', '32'), ('secs', '64')]))

    def test_timeparse_multipliers(self):
        self.assertEqual(timeparse('32 min'),
                         1920)
        self.assertEqual(timeparse('1 min'),
                         60)
        self.assertEqual(timeparse('1 hours'),
                         3600)
        self.assertEqual(timeparse('1 day'),
                         86400)
        self.assertEqual(timeparse('1 sec'),
                         1)

    def test_timeparse_1(self):
        self.assertEqual(timeparse('32m'), 1920)

    def test_timeparse_2(self):
        self.assertEqual(timeparse('2h32m'), 9120)

    def test_timeparse_3(self):
        self.assertEqual(timeparse('3d2h32m'), 268320)

    def test_timeparse_4(self):
        self.assertEqual(timeparse('1w3d2h32m'), None)   # NYI

    def test_timeparse_5(self):
        self.assertEqual(timeparse('1w 3d 2h 32m'), None)   # NYI

    def test_timeparse_6(self):
        self.assertEqual(timeparse('1 w 3 d 2 h 32 m'), None)   # NYI

    def test_timeparse_7(self):
        self.assertEqual(timeparse('4:13'), None)   # NYI

    def test_timeparse_8(self):
        self.assertEqual(timeparse('4:13:02'), None)   # NYI

    def test_timeparse_9(self):
        self.assertEqual(timeparse('4:13:02.266'), None)   # NYI

    def test_timeparse_10(self):
        self.assertEqual(timeparse('2:04:13:02.266'), None)   # NYI

    def test_timeparse_11(self):
        # uptime format
        self.assertEqual(timeparse('2 days,  4:13:02'), None)   # NYI

    def test_timeparse_12(self):
        self.assertEqual(timeparse('2 days,  4:13:02.266'), None)   # NYI

    def test_timeparse_13(self):
        self.assertEqual(timeparse('5hr34m56s'), 20096)

    def test_timeparse_14(self):
        self.assertEqual(timeparse('5 hours, 34 minutes, 56 seconds'), 20096)

    def test_timeparse_15(self):
        self.assertEqual(timeparse('5 hrs, 34 mins, 56 secs'), 20096)

    def test_timeparse_16(self):
        self.assertEqual(timeparse('2 days, 5 hours, 34 minutes, 56 seconds'),
                         192896)

    def test_timeparse_17(self):
        self.assertEqual(timeparse('1.2 m'), None)   # NYI

    def test_timeparse_18(self):
        self.assertEqual(timeparse('1.2 min'), None)   # NYI

    def test_timeparse_19(self):
        self.assertEqual(timeparse('1.2 mins'), None)   # NYI

    def test_timeparse_20(self):
        self.assertEqual(timeparse('1.2 minute'), None)   # NYI

    def test_timeparse_21(self):
        self.assertEqual(timeparse('1.2 minutes'), None)   # NYI

    def test_timeparse_22(self):
        self.assertEqual(timeparse('172 hours'), 619200)

    def test_timeparse_23(self):
        self.assertEqual(timeparse('172 hr'), 619200)

    def test_timeparse_24(self):
        self.assertEqual(timeparse('172 h'), 619200)

    def test_timeparse_25(self):
        self.assertEqual(timeparse('172 hrs'), 619200)

    def test_timeparse_26(self):
        self.assertEqual(timeparse('172 hour'), 619200)

    def test_timeparse_27(self):
        self.assertEqual(timeparse('1.24 days'), None)   # NYI

    def test_timeparse_28(self):
        self.assertEqual(timeparse('5 d'), 432000)

    def test_timeparse_29(self):
        self.assertEqual(timeparse('5 day'), 432000)

    def test_timeparse_30(self):
        self.assertEqual(timeparse('5 days'), 432000)

    def test_timeparse_31(self):
        self.assertEqual(timeparse('5.6 wk'), None)   # NYI

    def test_timeparse_32(self):
        self.assertEqual(timeparse('5.6 week'), None)   # NYI

    def test_timeparse_33(self):
        self.assertEqual(timeparse('5.6 weeks'), None)   # NYI
