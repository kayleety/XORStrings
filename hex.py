'''
Kaylee Yin
Cybersecurity - Period 5
November 2, 2020

XOR Cipher
'''

import sys

def xor(mode, key, inp):
    key = word
    i = 0

    final = ""
    for i in range(len(inp)): #XOR every pair of characters from key and inp
        if (mode == "human"):
            final += chr(ord(inp[i]) ^ ord(key[i]))

#main method
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
