import unittest

from pytimeparse import parse


class DefaultUnitTests(unittest.TestCase):
    def test_opt_in(self):
        self.assertIsNone(parse("10"))
        self.assertIsNone(parse("10", default_unit=None))
        for unit, seconds in [
            ("seconds", 1),
            ("minutes", 60),
            ("hours", 3600),
            ("days", 86400),
            ("weeks", 604800),
        ]:
            with self.subTest(unit=unit):
                self.assertEqual(parse("10", default_unit=unit), 10 * seconds)

    def test_signed_fractional_and_zero(self):
        for text, unit, expected in [
            (" - 1.5 ", "minutes", -90),
            ("+2", "hours", 7200),
            (".25", "seconds", 0.25),
            ("4.1", "minutes", 246),
            ("0", "days", 0),
        ]:
            with self.subTest(text=text):
                self.assertEqual(parse(text, default_unit=unit), expected)

    def test_explicit_units_and_clocks(self):
        self.assertEqual(parse("10s", default_unit="hours"), 10)
        self.assertEqual(parse("1:30", default_unit="hours"), 90)
        self.assertEqual(
            parse("1:30", granularity="minutes", default_unit="seconds"), 5400
        )

    def test_invalid_input(self):
        for text in ["", " ", "-", ".", "1.2.3", "1e3", "nan", "inf", "one"]:
            with self.subTest(text=text):
                self.assertIsNone(parse(text, default_unit="seconds"))

    def test_invalid_unit(self):
        for text in ["10", "10s"]:
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    parse(text, default_unit="fortnights")
