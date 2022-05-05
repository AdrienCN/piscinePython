from generator import generator

text = "1 2 3 4 5 6 7 8 9 10 1 2"
for i in generator(text, " ", "ordered"):
    print(i)
