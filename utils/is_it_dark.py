#!/usr/bin/env python3

from astral.sun import sun
import datetime
from astral.geocoder import database, lookup
import pytz


def main():
    loc = lookup("Berlin", database())
    s = sun(loc.observer, date=datetime.date.today(), tzinfo=loc.timezone)
    sunrise = s["sunrise"]
    sunset = s["sunset"]
    tz = pytz.timezone("Europe/Berlin")
    now = datetime.datetime.now(tz)
    if now < sunrise or now > sunset:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
