import sys

args = sys.argv
args.pop(0)
argCount = len(args)
usageMsg = """Usage: python operations.py <number1> <number2>
                Example:
                python operations.py 10 3"""

#Check arg count
if argCount != 2 :
    if argCount > 2:
        print("InputError: too many arguments\n")
    print(usageMsg)
    exit()

#Check arg format
for item in args:
        if item.isdigit() == False:
            print("InputError: only numbers\n")
            print(usageMsg)
            exit()

#Print results
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
