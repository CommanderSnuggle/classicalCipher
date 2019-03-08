import random


class MAC:

    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def setKey(self,key):
        self.key = list(key)
        if not(set(key) == set(self.alphabet)):
            print("Monoalphabetic cipher require all alphabet letters as a key. will replace the with random generated one")
            temp_key = list(self.alphabet)
            random.shuffle(temp_key)
            self.key = temp_key

    def encrypt(self, plaintext):

        plaintext = plaintext.replace(" ", "")
        plaintext = plaintext.upper()
        if not hasattr(self, 'key'):
            temp_key = list(self.alphabet)
            random.shuffle(temp_key)
            self.setKey(temp_key)

        ciphertext = []

        for letters in plaintext:
            ciphertext.append(self.key[self.alphabet.index(letters)])

        return ''.join(ciphertext)

    def decrypt(self, ciphertext):

        ciphertext = ciphertext.replace(" ","")
        ciphertext = ciphertext.upper()
        if not hasattr(self, 'key'):
            temp_key = list(self.alphabet)
            random.shuffle(temp_key)
            self.setKey(temp_key)

        plaintext = []
        for letters in ciphertext:
            plaintext.append(self.alphabet[self.key.index(letters)])

        return ''.join(plaintext)