import sys

t = (19, 42, 21)
print('The {} numbers are: '.format(len(t)), end="")

j = 1
for i in t:
    print("{}".format(i), end="")
    if j < len(t):
        print(", ", end="")
    j += 1
