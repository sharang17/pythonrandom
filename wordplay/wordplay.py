fin=open('words.txt')

def genlist(fileobj):
    wordlist=[]
    for line in fileobj:
        word=line.strip()
        wordlist.append(word)
    #leng=len(wordlist)
    return wordlist

def gr20(wordlist):
    words=[]
    for word in wordlist:
        if len(word)>20:
            words.append(word)
        else:
            continue
    return words

def has_no_e(wordlist):
    words=[]
    for word in wordlist:
        if 'e' in word:
            continue
        else:
            words.append(word)
    return words

def printeperc(words,wordlist):
    return (float(len(words))/len(wordlist))*100


wordlist=genlist(fin)
#words=has_no_e(wordlist)
