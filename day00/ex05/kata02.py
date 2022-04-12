import sys

t = (3, 30, 2019, 9, 25)

print("{month:02d}/{day:02d}/{year:04d} {hour:02d}:{minutes:02d}"
        .format(month=t[3], day=t[4],
                year=t[2], hour=t[0],
                minutes=t[1]))
