import sys

try:
    filename = sys.argv[1]
except:
    print("Requires a filename")
    filename = "freq.py"
try:
    fileText = open(filename, encoding="utf8").read();
except Exception as e:
    print(e)
    exit()

def freq(text):
    text = text.lower();
    total = 0
    counts= []
    for letter in "abcdefghijklmnopqrstuvqxyz":
        counts.append(text.count(letter))
    total = sum(counts)


    for i in range(len(counts)):
        c = counts[i]
        f = (int)(c / total * 10000)/100
        letter = chr(ord('a')+i)
        perc = str( f)+"%"
        print(letter + " :"+ perc +(6-len(perc))*" "+"|"+(int)(4*f)*"*")

#you can manually call freq if you want and not use the arguments.
freq(fileText)
