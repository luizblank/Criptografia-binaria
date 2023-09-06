alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 
            'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z']

def newbin(number):
    newnum = bin(int(number))
    newnum = newnum[2:]

    verifylen = 5 - len(newnum)
    if(verifylen > 0):
        newnum = '0' * verifylen + newnum
            
    return newnum
        
def criptografar(password):
    global alphabet
    newpassword = ""
    
    for i in password:
        if(i.isdigit()):
            newpassword += newbin(i) + '_'
        else:
            i = i.lower()
            if(i not in alphabet):
                newpassword += "00000_"
            else:
                newpassword += newbin(alphabet.index(i) + 1) + "_"
    
    return newpassword[:-1]
        
print("Insira a senha para ser codificada:")
password = input("> ")

print(criptografar(password))




