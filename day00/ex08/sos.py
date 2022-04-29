import sys

args = sys.argv
args.pop(0)
code = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  ' ': ' / '
        }
i = 0
res = ""
for word in args:
    for letter in word:
        tmp = letter.upper()
        if tmp in code:
            res += code[tmp]
        elif tmp != ' ':
            print("Error %c is not alphanumeric" % tmp)
            exit()
    if i < len(args):
        res += " / "
    i += 1
print(res)
