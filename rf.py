import sys

class RailFence:

    def __init__(self):
        self.key = 0

    def setKey(self, key):
        self.key = int(key)

    def encrypt(self, plaintext):
        cipherText = ""

        #in case of capital letters, change all to upper
        plaintext = plaintext.upper()

        #eliminate spaces if found
        plaintext.replace(" ", "")

        #loop through plaintext incrementing by key
        i = 0 #iterator for outer loop
        k = 0 #index of char to add to ciphertext
        
        while i < self.key:
            while k < len(plaintext):
                if plaintext[k] != "\n":
                    cipherText = cipherText + plaintext[k]
                k = k + self.key
            i = i + 1
            k = i

        print(cipherText)
        return cipherText

    def decrypt(self, ciphertext):
        plainText = ""

        #in case of capital letters, change all to upper
        ciphertext = ciphertext.upper()
        
        #eliminate spaces if found
        ciphertext.replace(" ", "")

        i = 0 #iterator for outer loop
        lim = 0 #limit of outer loop
        k = 0 #index of char to add to plaintext
        cipherlen = len(ciphertext) #holds ciphertext length
        div = len(ciphertext)/self.key
        extraInc = 0 #in case of odd number
        decInc = 0 #used in inner loop to iterate to different places in string

        #establish bound of outer loop
        if cipherlen%self.key != 0:
            lim = div + 1
        else:
            lim = div

        #how many of odd numbers to add
        while cipherlen%div != 0:
            extraInc = extraInc + 1
            cipherlen = cipherlen - div - 1

        cipherlen = len(ciphertext) #set back to original value
        decInc = extraInc

        while i < lim:
            while k < cipherlen:
                if ciphertext[k] != "\n":
                    plainText = plainText + plainText[k]
                
                #break loop if ciphertext and plaintext are the same length
                if cipherlen == len(plainText):
                    break
        
                if decInc > 0:
                    k = k + div + 1
                    decInc = decInc - 1
                else:
                    k = k + div
            
            decInc = extraInc
            i = i + 1
            k = i

        print(plaintext)
        return plaintext







