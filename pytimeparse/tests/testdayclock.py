"""Tests for Slurm's days-HH:MM:SS elapsed-time format."""

import unittest

from pytimeparse import parse


class TestSlurmDayClock(unittest.TestCase):
    def test_elapsed_time(self):
        self.assertEqual(parse('1-04:18:35'), 101915)
        self.assertIsInstance(parse('1-04:18:35'), int)

    def test_zero_and_multiple_days(self):
        self.assertEqual(parse('0-00:00:00'), 0)
        self.assertEqual(parse('12-04:18:35'), 1052315)

    def test_signed_elapsed_time(self):
        self.assertEqual(parse('-1-04:18:35'), -101915)
        self.assertEqual(parse('+1-04:18:35'), 101915)
        self.assertEqual(parse('  - 1-04:18:35  '), -101915)

    def test_fractional_seconds(self):
        self.assertEqual(parse('1-04:18:35.25'), 101915.25)
        self.assertEqual(parse('-1-04:18:35.25'), -101915.25)

    def test_minutes_granularity_does_not_change_day_clock(self):
        self.assertEqual(parse('1-04:18:35', granularity='minutes'), 101915)

    def test_existing_clock_formats(self):
        self.assertEqual(parse('1:04:18:35'), 101915)
        self.assertEqual(parse('12:25:02'), 44702)
        self.assertEqual(parse('04:18'), 258)
        self.assertEqual(parse('04:18', granularity='minutes'), 15480)

    def test_malformed_day_clock(self):
        for value in ('1--04:18:35', '1-4:18:35', '1-04:18',
                      '1-04:18:35 extra', '1.5-04:18:35',
                      '1-04-18:35', '1-04:18-35'):
            self.assertIsNone(parse(value))
