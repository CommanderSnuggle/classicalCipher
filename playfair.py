class playfair:
    matrix = [['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T', 'U'], ['V', 'W', 'X', 'Y', 'Z']] # placeholder and default matrix
    message = []
    cipher = []
    key = []
    lookup = {} #using a dictionary to store positions of letters to use to index into the matrix
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #this is the base that get's converted to the matrix
    def setKey(self, string):
        self.key = string
    def build_matrix(self, string=''): #build matrix from given key
        for i in range(0, len(string)):
            if string[i].upper() not in self.key and not string[i].isspace(): #if lettter isn't used, add it
                if string[i] == 'J':
                    self.key.append('I')    #replace J's with I's
                else:
                    self.key.append(string[i].upper())      #all to upper
                self.alphabet.remove(string[i].upper())     #remove existing from alphabet to prevent duplicates
        for i in range(len(self.key) - 1, -1, -1):  #insert key from back to front to maintain order
            self.alphabet.insert(0, self.key[i])
        for i in range(len(self.alphabet)):     #convert to matrix and generate lookup dictionary
            self.matrix[i/5][i%5] = self.alphabet[i]
            self.lookup[self.alphabet[i]] = [i/5, i%5]

    def setM(self, string): #set the message to encrypt
        for i in range(len(string)):
            if not string[i].isspace(): #strip spaces
                self.message.append(string[i].upper())
        for i in range(0, len(self.message)-1, 2):
            if self.message[i] == self.message[i+1]:
                self.message.insert(i+1, 'X')   #break up doubles
        if (len(self.message) % 2) == 1:
            self.message.append('X') #pad with trailing 'X' if not even length


    def setC(self, string):     #same as set message but sets the ciphertext you want to decode
        for i in range(len(string)):
            if not string[i].isspace():
                self.cipher.append(string[i].upper())
        for i in range(0, len(self.cipher)-1, 2):
            if self.cipher[i] == self.cipher[i+1]:
                self.cipher.insert(i+1, 'X')
        if (len(self.cipher) % 2) == 1:
            self.cipher.append('X')

    #the following functions wrap around the matrix
    def addr(self, char):   #returns position in the matrix of the given char
        return [self.lookup[char][1], self.lookup[char][0]]
    def rs(self, char): #returns character one space to the right
        return self.matrix[self.addr(char)[1]][((self.addr(char)[0] + 1)%5)]
    def ds(self, char): #returns character one space below
        return self.matrix[((self.addr(char)[1]+1) % 5)][self.addr(char)[0]]
    def ls(self, char): #returns character one space left
        if self.addr(char)[0] == 0:
            return self.matrix[self.addr(char)[1]][4]
        return self.matrix[self.addr(char)[1]][(self.addr(char)[0] - 1)]
    def us(self, char): #returns character one space above
        if self.addr(char)[1] == 0:
            return self.matrix[4][self.addr(char)[0]]
        return self.matrix[((self.addr(char)[1]-1))][self.addr(char)[0]]

    def box(self, chara, charb): #returns the horizontal corners of the given characters
        ra = [self.addr(charb)[1], self.addr(chara)[0]]
        rb = [self.addr(chara)[1], self.addr(charb)[0]]
        return self.matrix[rb[0]][rb[1]], self.matrix[ra[0]][ra[1]]

    def tostring(self): #
        print("KEY")
        print(self.key)
        print("MESSAGE")
        print(self.message)
        print("CIPHER")
        print(self.cipher)
    
    def encrypt(self): #encrypt message to ciphertext
        self.cipher = []
        for i in range(0, len(self.message)-1, 2):
            if self.addr(self.message[i])[1] == self.addr(self.message[i+1])[1]:
                self.cipher.append(self.rs(self.message[i]))
                self.cipher.append(self.rs(self.message[i+1]))
            elif self.addr(self.message[i])[0] == self.addr(self.message[i+1])[0]:
                self.cipher.append(self.ds(self.message[i]))
                self.cipher.append(self.ds(self.message[i+1]))
            else:
                self.cipher.append(self.box(self.message[i], self.message[i+1])[0])
                self.cipher.append(self.box(self.message[i], self.message[i+1])[1])
        print(self.cipher)

    def decrypt(self): #decrypt ciphertext to plaintext message
        self.message = []
        for i in range(0, len(self.cipher)-1, 2):
            if self.addr(self.cipher[i])[1] == self.addr(self.cipher[i+1])[1]:
                self.message.append(self.ls(self.cipher[i]))
                self.message.append(self.ls(self.cipher[i+1]))
            elif self.addr(self.cipher[i])[0] == self.addr(self.cipher[i+1])[0]:
                self.message.append(self.us(self.cipher[i]))
                self.message.append(self.us(self.cipher[i+1]))
            else:
                self.message.append(self.box(self.cipher[i], self.cipher[i+1])[0])
                self.message.append(self.box(self.cipher[i], self.cipher[i+1])[1])
        print(self.message)
    def clear(self): #clear message and cipher to make sure encrypt and decrypt are working
        self.message = []
        self.cipher = []
