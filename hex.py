'''
Kaylee Yin
Cybersecurity - Period 5
November 2, 2020

XOR Cipher
'''

import sys

def xor(mode, key, inp):

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
