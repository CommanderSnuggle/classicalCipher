import math


class RowTrans:

    def __init__(self):
        self.key = ""
        self.keyLen = 0

    def setKey(self, key):
        self.key = str(key)
        self.keyLen = len(self.key)

    def encrypt(self, plaintext):
        # Remove spaces and convert plaintext to uppercase
        plaintext = plaintext.replace(" ", "").upper()
        cipherText = ""

        # Number of Columns is the length of the key
        # Number of Rows is the length of the plaintext divided by the length of the key
        cols = self.keyLen
        rows = int(math.ceil(len(plaintext) / self.keyLen))

        # Initialise Array, add X's to empty spaces
        cipherArr = [['X'] * cols for i in range(rows)]

        # Put plaintext into array, writing left to right
        temp = 0
        for i in range(rows):
            for j in range(cols):
                if temp >= len(plaintext):
                    break
                cipherArr[i][j] = plaintext[temp]
                temp += 1

        # Pull ciphertext out of array by reading top to bottom based on key
        for i in range(self.keyLen):
                for j in range(rows):
                    cipherText += cipherArr[j][int(self.key[i])-1]

        print(cipherText)
        return cipherText

    def decrypt(self, ciphertext):

        plaintext = ""

        # Calculate row and column numbers then initialise array
        cols = self.keyLen
        rows = int(math.ceil(len(ciphertext) / self.keyLen))
        cipherArr = [['X'] * cols for i in range(rows)]

        # Populate array with ciphertext by writing top to bottom
        temp = 0
        for i in range(cols):
            for j in range(rows):
                cipherArr[j][i] = ciphertext[temp]
                temp += 1

        # Read from array by selecting column by key
        for i in range(rows):
            for j in range(self.keyLen):
                col = self.key.find(str(j+1))
                plaintext += cipherArr[i][col]

        print(plaintext)
        return plaintext