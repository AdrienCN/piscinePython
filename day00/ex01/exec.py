import sys

# Count arg numbers
argc = len(sys.argv)
argv = str(sys.argv)
# Exit if empty
if argc == 1:
    exit()

# Concat if multiple arguments
res = sys.argv[1]
if argc >= 2:
    for i in range(argc):
        if i > 1:
            res += " " + sys.argv[i]
rev = res[::-1]
rev = rev.swapcase()
print(rev)

# Reverse string letters
