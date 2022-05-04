import sys

args = sys.argv
argLen = len(sys.argv)

assert argLen == 2, "Error usage: prog needs one argument"
nb = sys.argv[1]
if nb[0] == '-' or nb[0] == '+':
    nb_check = nb[1:]
else:
    nb_check = nb
assert nb_check.isdigit(), "Error argument must be an int"
nb = int(nb)

if nb == 0:
    print("I'm Zero")
else:
    print("I'm Even") if nb % 2 == 0 else print("I'm Odd")
