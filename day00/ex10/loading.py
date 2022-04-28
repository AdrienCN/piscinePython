import sys
import time

lst = range(0, 11, 1)


def ft_progress(lst):
    start = 0
    eta = 0
    elapsed = time.time()
    bar = 0
    range_size = max(lst)
    for j in lst:
        equal = (j / range_size) * 10
        space = 10 - equal
        tmp = 0
        arrow = ""
        # cree la fleche de chargement
        while tmp < 11:
            if tmp <= equal:
                arrow += "="
                if tmp + 1 > equal:
                    arrow += ">"
            else:
                arrow += " "
            tmp += 1

        # update time
        remaining = range_size - j
        loopend = time.time()
        if j:
            eta = (remaining * (loopend - elapsed)) / j
        else:
            eta = 0
        print("ETA: %6.2f [%3.2d%%][%s] %2d/%2d | Time elapsed : %.2f"
              % (eta, equal * 10, arrow, j, range_size,  loopend - elapsed))
        yield j


for i in ft_progress(lst):
    time.sleep(5)
