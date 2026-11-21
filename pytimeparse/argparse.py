"""Type converters for use with :mod:`argparse`."""

from argparse import ArgumentTypeError
from datetime import timedelta

from .timeparse import timeparse


def parse_timedelta(value: str) -> timedelta:
    """Parse a duration for ``ArgumentParser.add_argument(type=...)``.

    Raise :class:`argparse.ArgumentTypeError` for invalid expressions or
    durations that cannot be represented by :class:`datetime.timedelta`.
    """
    seconds = timeparse(value)
    if seconds is None:
        raise ArgumentTypeError(f"invalid time expression: {value!r}")
    try:
        return timedelta(seconds=seconds)
    except OverflowError as exc:
        raise ArgumentTypeError(
            f"time expression is outside the timedelta range: {value!r}"
        ) from exc
