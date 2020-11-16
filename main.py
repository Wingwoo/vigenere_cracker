#Define variables
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

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
        if i != " ":
            count = count + 1
        if count > keylen - 1:
            count = 0
        currentkey = key[count]           
    return output

#Main
print("Vigenere Cipher Cracker | V0.2 | Made By WingwooGaming")
string = input("What is the string to cipher? ")
key = input("What is the key? ")
print (vcipher(string, key))
