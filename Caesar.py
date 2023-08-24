alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
txt = input("Insert text to encode: ").lower()
n = int(input("Insert shift number: "))
def chiper(txt,n):
    nt = ""
    for letter in txt:
        pos = alphabet.index(letter) #For know in what position of alphabet is the letter
        npos = pos+ n
        nlett = alphabet[npos]
        nt += nlett
        print(pos)
    print(nt)
chiper(txt,n)

txt = input("Insert text to decode: ")
n= int(input("Insert  shift number: "))
def dechiper(txt,n):
    nt = ""
    for letter in txt:
        pos = alphabet.index(letter)
        npos= pos - n
        nlett = alphabet[npos]
        nt += nlett
    print(nt)
dechiper(txt,n)
        