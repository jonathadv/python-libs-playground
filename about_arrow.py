"""
# Arrow: Better dates & times for Python

Arrow is a Python library that offers a sensible and human-friendly approach
to creating, manipulating, formatting and converting dates, times and timestamps.
It implements and updates the datetime type, plugging gaps in functionality and
providing an intelligent module API that supports many common creation scenarios.
Simply put, it helps you work with dates and times with fewer imports and a lot less code.

Arrow is named after the arrow of time and is heavily inspired by moment.js and requests.

source: https://arrow.readthedocs.io/en/latest/
"""
import arrow


def arrow_date():
    now_local = arrow.now()
    print(f"{now_local=}")

    now_utc = arrow.utcnow()
    print(f"{now_utc=}")

    now_utc_minus_one_hour = now_utc.shift(hours=-1)
    print(f"{now_utc_minus_one_hour=}")

    now_us_new_your = now_utc.to("America/New_York")
    print(f"{now_us_new_your=}")


def arrow_date_parsing():
    yyyy_mm_dd_parsed_date = arrow.get("2021-01-22")
    print(f"{yyyy_mm_dd_parsed_date=}")

    mm_yyyy_dd_parsed_date = arrow.get("01-2021-22", "MM-YYYY-DD")
    print(f"{mm_yyyy_dd_parsed_date=}")

    mm_yy_dd_parsed_date = arrow.get("01-21-22", "MM-YY-DD")
    print(f"{mm_yy_dd_parsed_date=}")

    yyyy_mm_dd_parsed_to_datetime = arrow.get("2021-01-22").datetime
    print(f"{yyyy_mm_dd_parsed_to_datetime=}")


def arrow_properties():
    now = arrow.now()
    print(f"{now=}")

    print(f"now.naive: {now.naive}")
    print(f"now.tzinfo: {now.tzinfo}")
    print(f"now.year: {now.year}")
    print(f"now.month: {now.month}")
    print(f"now.day: {now.day}")


def arrow_humanize():
    now = arrow.now()
    print(f"now.humanize(): {now.humanize()}")

    past = now.shift(hours=-1)
    print(f"past.humanize(): {past.humanize()}")

    past2 = now.shift(minutes=-30)
    print(f"past2.humanize(): {past2.humanize()}")

    future = now.shift(hours=1)
    print(f"future.humanize(): {future.humanize()}")

    future2 = now.shift(minutes=30)
    print(f"future2.humanize(): {future2.humanize()}")


if __name__ == "__main__":
    print("-" * 20)
    arrow_date()

    print("-" * 20)
    arrow_date_parsing()

    print("-" * 20)
    arrow_properties()

    print("-" * 20)
    arrow_humanize()
