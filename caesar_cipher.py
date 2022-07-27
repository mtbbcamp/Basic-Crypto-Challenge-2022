import time
def cc_encrypt(message, key):
    encryption = ""
    for c in message:
        encryption = encryption + chr((((ord(c)-65) + key) % 26) + 65)
    return encryption

def cc_bruteforce(ciphertext):
    key = 0
    plaintext = ''
    while plaintext != 'BRUTEFORCE':
        plaintext = cc_decrypt(ciphertext, key)
        key += 1
    key -= 1
    print("KEY: " + str(key))
    print("PLAINTEXT: " + cc_decrypt(ciphertext, key))

def cc_decrypt(encrypted_message, key):
    decryption = ""
    if key < 0:
        key *= -1
    for c in encrypted_message:
        #Convert to ASCII code
        #Convert to position in the alphabet
        #Apply decrpytion
        #Back to ASCII code
        #Back to character
        d = chr((((ord(c)-65) - key) % 26) + 65)
        decryption += d
         

    return decryption


def run_tests():
    print("=====KNOWN KEY=====")
    print(cc_decrypt("ALZAPUN", 7))
    print(cc_decrypt("JXKAQYXKH", 23))
    print(cc_decrypt("BSUOHWJS", -14))
    print(cc_decrypt("HUQBBOBEDWJUNJMYJXRYWDKCRUH", 135762))

    print('=====BRUTE FORCE=====')
    start = time.time()
    cc_bruteforce('DTWVGHQTEG')
    end = time.time()
    print("Took " + str(end-start) + " seconds to decrypt DTWVGHQTEG")
    start = time.time()
    cc_bruteforce('CSVUFGPSDF')
    end = time.time()
    print("Took " + str(end-start) + " seconds to decrypt CSVUFGPSDF")
    start = time.time()
    cc_bruteforce('KADCNOXALN')
    end = time.time()
    print("Took " + str(end-start) + " seconds to decrypt KADCNOXALN")

    print('=====ENCRYPT=====')
    print(cc_encrypt('THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG', 13) + ' 13')
if __name__ == '__main__':
    run_tests()
