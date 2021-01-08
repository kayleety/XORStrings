# Kaylee Yin - Cybersecurity, Period 5
# Lab #1 - Decode Monoalphabetic Cypher

# Test run:
# $ python3 frequency.py

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

    for i in percentages:
        print(i + ": " + str(percentages[i]))

letterFreq('sally likes seashells')
#letterFreq("WKLV PHVVDJH ZDV HQFUBSWHG XVLQJ D FDHVDU VKLIW FLSKHU.")
