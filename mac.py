import random


class MAC:

    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def setKey(self,key):
        self.key = list(key.upper())
        self.error = False
        if not(set(self.key) == set(self.alphabet)):
            print("Monoalphabetic cipher require 26 unique letters for the key, Please try again. Sample key: "+ self.alphabet)
            self.error = True

    def encrypt(self, plaintext):
        if not(self.error):
            plaintext = plaintext.replace(" ", "")
            plaintext = plaintext.upper()
            ciphertext = []
            for letters in plaintext:
                 ciphertext.append(self.key[self.alphabet.index(letters)])
            return ''.join(ciphertext)
        else:
            return "Monoalphabetic encryption key error."
        
    def decrypt(self, ciphertext):
        if not(self.error):
            ciphertext = ciphertext.replace(" ", "")
            ciphertext = ciphertext.upper()
            plaintext = []
            for letters in ciphertext:
                plaintext.append(self.alphabet[self.key.index(letters)])
            return ''.join(plaintext)
        else:
            return "Monoalphabetic decryption key error."
        
        
