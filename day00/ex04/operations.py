import sys

args = sys.argv
args.pop(0)
argCount = len(args)
usageMsg = "Usage: python operations.py <number1> <number2> " +\
           "\nExample: " +\
           "python operations.py 10 3"

# Check arg count
if argCount != 2:
    if argCount > 2:
        print("InputError: too many arguments")
    else:
        print("InputError: Not enough arguments")
    print(usageMsg)
    exit()

# Check arg format
for item in args:
    if item[0] == '-' or item[0] == '+':
        item_tocheck = item[1:]
    else:
        item_tocheck = item
    if not item_tocheck.isdigit():
        print("InputError: only numbers\n")
        print(usageMsg)
        exit()

# Print results
a = int(args[0])
b = int(args[1])
if b == 0:
    quotient = "ERROR (div by zero)"
    remainder = "ERROR (modulo by zero)"
else:
    quotient = str(a / b)
    remainder = str(a % b)

print("Sum:\t\t", str(a + b))
print("Difference:\t", str(a - b))
print("Product:\t", str(a * b))
print("Quotient:\t", quotient)
print("Remainder:\t", remainder)
