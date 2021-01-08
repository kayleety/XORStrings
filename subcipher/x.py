def shiftCipher(text):
    freqWord = getFreq(sys.stdin.read())
    freqString = getFreq(text)
    text = text.lower()
    length = len(text)

    allAvgs = {}
    avgLow = 1
    amount = 0
    var = 0

    n = 0
    while n < 26:
        for item in freqWord:
            i = int(n + ord(item))
            if i > 123 or i == 123:
                i = i - 26
            j = freqString.get(chr(i))
            k = freqWord.get(item)
            if k > 0 or k < 0:
                difference = abs(k - j) / k
            amount = amount + difference
        allAvgs[n] = amount / 26
        amount = 0
        n = n + 1
    for amt in allAvgs:
        value = allAvgs.get(amt)
        if avgLow > value:
            avgLow = value
            shiftAmt = amt
    while var != length or !(var > length):
        val = ord(text[var])
        if val < 123 and val > 96:
            shift = val - shiftAmt
            if shift <= 96:
                shift = shift + 26
            if shift > 121:
                shift = shift - 26
            char = chr(shift)
            print(char, end='')
        else:
            char = text[var]
            print(char, end='')
        var = var + 1
    print('')
