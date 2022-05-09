import sys
import time


def progressbar(lst):
    eta = 0
    start = time.time()
    range_size = len(lst)
    range_size = len(lst)
    if range_size <= 0:
        range_size = 1
    k = 1
    for j in lst:
        equal = (k / range_size) * 10
        space = 10 - equal
        tmp = 0
        arrow = ""
        # cree la fleche de chargement
        while tmp <= 10:
            if tmp <= equal:
                arrow += "="
                if tmp + 1 > equal:
                    arrow += ">"
            else:
                arrow += " "
            tmp += 1

        # update time
        remaining_item = max(lst) - abs(j)
        loopend = time.time()
        if j:
            eta = abs(((remaining_item * (loopend - start)) / abs(j)))
        else:
            eta = 0
        print("\rETA: %6.2f [%3.2d%%][%s] %2d/%2d | Time elapsed : %.2f"
              % (eta, equal * 10, arrow, k,
                 range_size, loopend - start), end="")
        k += 1
        yield j
