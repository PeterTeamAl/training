from getpass import getpass
import pyAesCrypt

password = input("Enter password to be cyphered or decyphered: ")
cond = int(input("1 to crypt, 0 to decrypt."))
if cond == 1:
     #encrypt
     pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

elif cond == 0:
    #decrypt
    pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)

print("File was created in parent directory. ")

