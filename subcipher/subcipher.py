# Kaylee Yin - Cybersecurity, Period 5
# Lab #1 - Decode Monoalphabetic Cypher

# Test run - make sure to uncomment the test case:
# $ python3 subcipher.py < wordlist10000.txt

#1.1
def letterFreq(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0 #number of times a letter appears in the file
    letter = 0 #used to iterate through the alphabet
    percentages = {} #letter: % frequency

    string = string.lower() #make the entire string lowercase to account for uppercase letters
    strLen = 0
    for x in range(len(string)):
        for y in range(26):
            if string[x] == alphabet[y]: #ensure that punctuation and special letters are excluded
                strLen += 1

    while letter < 26: #iterate through the alphabet
        for i in range(len(string)):
            if string[i] == alphabet[letter]:
                count += 1
        percentages[alphabet[letter]] = count/strLen #add to percentages dictionary the letter and its % frequency
        count = 0
        letter += 1

    '''
    #print each letter and its frequency:
    for i in percentages:
        print(i + ": " + str(percentages[i]))
    '''
    return percentages

#letterFreq('sally likes seashells')
#letterFreq("WKLV PHVVDJH ZDV HQFUBSWHG XVLQJ D FDHVDU VKLIW FLSKHU.")

#1.2a
def shift(string):
    o = open("wordlist10000.txt", "r")
    if o.mode == "r":
        contents = o.read()
    wordFreq = letterFreq(contents) #% frequency of the alphabet from the English dictionary
    strFreq = letterFreq(string) #% frequency of string
    averages = {}
    total = 0

    for x in range(25): # shift 25 times
        for i in wordFreq: # abcdefghijklmnopqrstuvwxyz
            index = int(ord(i) + x)
            if index > 122: #circle back to the beginning of the alphabet
                index -= 26
            if wordFreq.get(i) < strFreq.get(chr(index)): #find the larger number of the two for % diff calculation
                big = strFreq.get(chr(index))
                small = wordFreq.get(i)
            else:
                big = wordFreq.get(i)
                small = strFreq.get(chr(index))
            if big != 0: #ensure no division by 0
                diff = (big - small) / big #find the percent difference
            total += diff #total every percent difference comparison
        averages[x] = total / 26
        total = 0

    lowestAvg = 1
    for i in averages: #find the lowest average of the % diff in order to find the shift
        if averages.get(i) < lowestAvg:
            lowestAvg = averages.get(i)
            shift = i

    x = 0
    string = string.lower()
    while x < len(string):
        if ord(string[x]) >= 97 and ord(string[x]) <= 122: #if the characters are lowercase letters
            shifted = ord(string[x]) - shift
            if shifted > 122: #circle back to the beginning of the alphabet
                shifted -= 26
            if shifted < 97: #circle to the end of the alphabet
                shifted = 123 - (97 - shifted)
            print(chr(shifted), end = "")
        else:
            print(string[x], end = "")
        x += 1
    print()

shift('JYFIRMFMVKJNNUBHCUSDMQMTAFWZZSFMVENTFFVGJYFIRMFM')
#shift('HVWG WG O GVCFH SBCIUV HSLH HVOH WG SBQFMDHSR KWHV O GWADZS GVWTH QWDVSF')

'''
#1.2b — i was completely stuck and this code does not work, so i commented it out
def substitute(string):
    words = string.split()
    o = open("wordlist10000.txt", "r")
    if o.mode == "r":
        contents = o.read()
    wordFreq = letterFreq(contents)
    strFreq = letterFreq(string)

    key = {} #{letter in encrypted code: correct letter}

    oneLetter = {}
    for i in words:
        if len(i) == 1:
            oneLetter[i] =
'''

testCase5 ='''xjiu cnpyypm, irh xgz uypxgw xbozu
      hph mwnz irh mpkcyz pr xgz jicz:
iyy kpkuw jznz xgz cbnbmbozu,
      irh xgz kbkz nixgu bexmnicz.
czjinz xgz qiccznjbla, kw ubr!
      xgz qiju xgix cpxz, xgz lyiju xgix lixlg!
czjinz xgz qecqec cpnh, irh uger
      xgz vnekpbeu cirhznurixlg!'''
#substitute(testCase5)
