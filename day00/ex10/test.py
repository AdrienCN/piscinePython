from loading import ft_progress
import time

ret = 0

listy = range(1)
start = time.time()
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.10)

print("end = ", time.time() - start)
print("\nret = ", ret)
