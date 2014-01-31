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
                set(re.match(TIME + r'\s*$', '16h32m64s  ').groupdict().iteritems()),
                set([('hours', '16'), ('secs', '64'), ('mins', '32')]))

    def test_timeparse_simple(self):
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
