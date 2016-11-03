def rot13(word,inc):
    rot=[]
    word=word.lower()
    for letter in word:
        num=ord(letter)+inc
        if num > 122:
            num=ord('a')+(num-122)
            rot.append(chr(num))
        elif num < ord('a'):
            num=122-(ord(letter)-ord('a'))-1
            rot.append(chr(num))
        else:
            rot.append(chr(num))
    rotpr=''.join(i for i in rot)
    print rotpr

rot13('melon',-10)
