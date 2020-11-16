#Imports required tools
from itertools import product

#Define variables
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter = 'abcdefghijklmnopqrstuvwxyz'

#Functions
def vcipher(string, key):
    string = string.lower()
    output = ""
    key = list(key)
    keylen = len(key)
    currentkey = key[0]
    count = 0
    for i in string:
        if i == " ":
            output = output + " "
        elif i == ".":
            output = output + "."
        elif i == ",":
            output = output + ","
        elif i in letters:
            shift = letters.index(currentkey)
            if letters.index(i) + shift >= 25:
                shift = shift - 26
            index = letters.index(i)
            shiftedletter = letters[index + shift]
            output = output + shiftedletter
        else:
            output = output + "#"
        if i != " ":
            count = count + 1
        if count > keylen - 1:
            count = 0
        currentkey = key[count]
    return output

def dvcipher(string, key):
    string = string.lower()
    output = ""
    key = list(key)
    keylen = len(key)
    currentkey = key[0]
    count = 0
    for i in string:
        if i == " ":
            output = output + " "
        elif i == ".":
            output = output + "."
        elif i == ",":
            output = output + ","
        elif i in letters:
            if letters.index(currentkey) != 0:
                shift = letters.index(currentkey)
                shift = shift - shift - shift
            else:
                shift = 0
            if letters.index(i) + shift >= 25:
                shift = shift - 26
            index = letters.index(i)
            shiftedletter = letters[index + shift]
            output = output + shiftedletter
        else:
            output = output + "#"
        if i != " " and i != "," and i != ".":
            count = count + 1
        if count > keylen - 1:
            count = 0
        currentkey = key[count]           
    return output

def vciphercracker(string, known):
    for length in range(1, 30):
        to_attempt = product(letter, repeat=length)
        print("Trying length " + str(length))
        for attempt in to_attempt:
            dc = dvcipher(string, attempt)
            if known in dc:
                print("Possible value is: " + dc)
                print("The key was " + str(attempt))
        

#Main
print("Vigenere Cipher Cracker | V0.3 | Made By WingwooGaming")
#string = input("What is the string to cipher? ")
#key = input("What is the key? ")
print(dvcipher("Kw fg yyf rlakfkee eflhzbgerkrj vf qcp, fg npqkc kk gp tgryct, kfck gu, sw uf ajrlizli kfg fpfvp qw rjv jgkrgiq qw rjv yngfcscv, kfck lqk y yfpf tmwcb dv kcuc qlr.", "cry"))
print (vciphercracker("Kw fg yyf rlakfkee eflhzbgerkrj vf qcp, fg npqkc kk gp tgryct, kfck gu, sw uf ajrlizli kfg fpfvp qw rjv jgkrgiq qw rjv yngfcscv, kfck lqk y yfpf tmwcb dv kcuc qlr.", "anything"))
