import sys

args = sys.argv
argLen = len(sys.argv)

assert argLen == 2, "Error usage: prog needs one argument"
assert sys.argv[1].isdigit(), "Error argument must be an int"
nb = int(sys.argv[1])

if nb == 0:
    print("I'm Zero")
else:
    print("I'm Even") if nb % 2 == 0 else print("I'm Odd")
