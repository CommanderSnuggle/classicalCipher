TO EXECUTE THE CIPHERS
Run the cipher.py file followed by the arguments

The arguments are

root@name:~# python cipher.py <cipher_name> <cipher_key> <ENC/DEC> <input_file> <output_file>

<cipher_name> : 
                PLS - Playfair
                MAC - monoalphabetic
                CES - Caesar
                RFC - Railfence
                VIG - Vigenre
                RTS - Row Transposition

<cipher_key> : The key to be used

<ENC/DEC> : ENC - Encryption
            DEC - Decryption

<input_file> : The file to be ENC/DEC

<output_file> : The output of the cipher function

An example would be

root@name:~# python cipher.py CES 3 ENC small.txt smallout.txt