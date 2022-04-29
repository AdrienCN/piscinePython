import sys


args = sys.argv
args.pop(0)
# Ponctuation restante

if len(args) != 2 or !args[1].isdigit():
    print("ERROR: usage <String To Filter> <Word Lenght Limit>")
    exit()

n = int(args[1])
res = [word for word in args[0].split() if len(word) > n]
print(res)
