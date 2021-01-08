'''
Kaylee Yin
Cybersecurity - Period 5
November 2, 2020

XOR Cipher
'''
import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)


newWord = key
index = 0
while len(newWord) < len(inp): #method to make key as long as inp
    newWord += key[index]
    if (index == len(key) - 1): #if the index exceeds the length of original key
        index = 0
    else:
        index += 1

final = ""
for i in range(len(inp)): #XOR every pair of characters from key and inp
    if (mode == "human"):
        final = final + chr(ord(newWord[i]) ^ ord(inp[i]))
    else:
        final = final + (hex(ord(newWord[i]) ^ ord(inp[i])))[2:] + " "
print(final)
