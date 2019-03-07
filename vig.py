class VIG:

    def setKey(self, key):
        self.key=key
        keys = []
        self.final_key = []
        self.key = self.key.replace(" ", "")

        for i in range(len(self.key)):
                keys.append(ord(self.key[i].upper()))
                self.final_key.append(keys[i] - 65)

    def encrypt(self, plaintext):
        enciphered = ""
        plaintext=plaintext.upper()
        i = 0
        for letter in plaintext:
            if ord(letter) + self.final_key[i] > 90:
                new_key = ord(letter) + self.final_key[i] - 90
                new_letter = chr(64 + new_key)
                enciphered += new_letter
                i += 1
                if len(self.final_key) == i:
                    i = 0
            else:
                enciphered += (chr(ord(letter) + self.final_key[i]))
                i += 1
                if len(self.final_key) == i:
                    i = 0
        return enciphered

    def decrypt(self, ciphertext):
        plaintext = ""
        i = 0
        for letter in ciphertext:
            if ord(letter) - self.final_key[i] < 65:
                new_key = 65 - (ord(letter) - self.final_key[i])
                new_letter = chr(91 - new_key)
                plaintext += new_letter
                i += 1
                if len(self.key) == i:
                    i = 0
            else:
                plaintext += chr(ord(letter) - self.final_key[i])
                i += 1
                if len(self.final_key) == i:
                    i = 0
        return plaintext