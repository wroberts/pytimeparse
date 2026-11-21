"""Tests for the argparse timedelta converter."""

import argparse
from datetime import timedelta
import unittest

from pytimeparse.argparse import parse_timedelta


class TestArgparse(unittest.TestCase):
    def test_optional_duration(self):
        parser = argparse.ArgumentParser(exit_on_error=False)
        parser.add_argument("--duration", type=parse_timedelta)
        for value, expected in [
            ("1h30m", timedelta(hours=1, minutes=30)),
            ("0s", timedelta(0)),
            ("-2m", timedelta(minutes=-2)),
            ("1.25s", timedelta(seconds=1, microseconds=250000)),
            ("1:24", timedelta(seconds=84)),
        ]:
            with self.subTest(value=value):
                args = parser.parse_args(["--duration=" + value])
                self.assertEqual(args.duration, expected)

    def test_positional_durations(self):
        parser = argparse.ArgumentParser(exit_on_error=False)
        parser.add_argument("durations", type=parse_timedelta, nargs="+")
        self.assertEqual(
            parser.parse_args(["1d", "2h", "0s"]).durations,
            [timedelta(days=1), timedelta(hours=2), timedelta(0)],
        )

    def test_invalid_expression(self):
        parser = argparse.ArgumentParser(exit_on_error=False)
        parser.add_argument("--duration", type=parse_timedelta)
        for value in ["", "tomorrow", "1.2.3s", "1h garbage"]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                    argparse.ArgumentError, "argument --duration: invalid time expression"
                ):
                    parser.parse_args(["--duration=" + value])

    def test_out_of_range(self):
        parser = argparse.ArgumentParser(exit_on_error=False)
        parser.add_argument("duration", type=parse_timedelta)
        for value in ["1000000000d", "-1000000000d"]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(
                    argparse.ArgumentError, "outside the timedelta range"
                ):
                    parser.parse_args(["--", value])

    def test_timedelta_boundaries(self):
        self.assertEqual(parse_timedelta("999999999d"), timedelta(days=999999999))
        self.assertEqual(parse_timedelta("-999999999d"), timedelta.min)

    def test_converter_error_type(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_timedelta("invalid")
