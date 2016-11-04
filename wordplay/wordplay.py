fin=open('words.txt')

def gen_list(fin):
    wordlist=[]
    for line in fin:
        word=line.strip()
        print word
        wordlist.append(word)
    return(wordlist)
#print words with length greater than 20
def listlen(wordfile):
    wordlist=[]
    for line in fin:
        word=line.strip()
        wordlist.append(word)
    return(len(wordlist))

def gr20(wordfile):
    wordlist=[]
    for line in fin:
        word=line.strip()
        if (len(word)>20):
            print word
        else:
            wordlist.append(word)
    return wordlist

#print no e
def has_no_e(wordfile):
    e_list=[]
    for line in fin:
        word=line.strip()
        #print(type(word))
        if 'e' in word:
            continue
        else:
            e_list.append(word)
    return e_list

def printeperc(elist=has_no_e,len=listlen(fin)):
    perc=float((len(elist)/len)*100)
    return perc


def avoids(forbidden,word="Monty Python"):
    print("Foribidden: " +forbidden)
    print("Word: "+word)
    if(avoid_check(word,forbidden)):
        print "True"


def avoid_check(word,forbidden):
    for letter in word:
        if letter in forbidden:
            print "Forbidden"
            return False
    return True

##User Segment
#inp=str(raw_input("Enter forbidden string: "))
#res=avoids("MontyPython",inp)

def avoids_count(wordlist):
    forbidden=raw_input("Enter forbidden string: ")
    count=0
    for word in wordlist:
        if(avoid_check(word,forbidden)):
            count+=1
        else:
            continue
    return float((count/len(wordlist))*100)

#print(avoids_count(gen_list(fin)))
