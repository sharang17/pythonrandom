"""
Exercise 2
In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e.” Since “e” is the most common letter in English, that’s not easy to do.
In fact, it is difficult to construct a solitary thought without using that most common symbol. It is slow going at first, but with caution and hours of training you can gradually gain facility.

All right, I’ll stop now.

Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.

Modify your program from the previous section to print only the words that have no “e” and compute the percentage of the words in the list have no “e.”

Exercise 3
Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesn’t use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the smallest number of words?

Exercise 4
Write a function named uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the list. Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa?”
Exercise 5
Write a function named uses_all that takes a word and a string of required letters, and that returns True if the word uses all the required letters at least once. How many words are there that use all the vowels aeiou? How about aeiouy?
Exercise 6
Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there?
"""




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

def avoids_word(word,forbidden):
    if forbidden in word:
        return -1
    else:
        return "True"


def avoids(wordlist):
    forbidden=raw_input("Enter forbidden string: ")
    wordlist=[]
    for word in wordlist:
        if forbidden in word:
            continue
        else:
            wordlist.append(word)
    return wordlist

wordlist=genlist(fin)
#words=has_no_e(wordlist)
def uses_only(word,uses):
    sorted_word=''.join(sorted(word))
    sorted_uses=''.join(sorted(uses))
    if sorted_word==sorted_uses:
        return True
    else:
        return false

def uses_all(word,uses):
    sorted_word=''.join(sorted(word))
    sorted_uses=''.join(sorted(uses))
    if sorted_uses in sorted_word:
        return "True"
    else:
        return "False"

def check_vowels(wordlist):
    vowels="aeiouy"
    vow=[]
    for word in worldlist:
        if vowels in word:
            vow.append(word)
        else:
            continue
    return vow

def is_abecedarian(word):
    for i in range(0,len(word)):
        if letter[i] < letter[i+1]:
            continue
        else:
            print "false"
