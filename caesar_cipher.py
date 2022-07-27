import time
def cc_encrypt(message, key):
    encryption = ""
    for c in message:
        encryption = encryption + chr((ord(c) + key) % 26 + 65) 
    return encryption

def cc_bruteforce(ciphertext):
    key = 0
    plaintext = ''
    while plaintext != 'BRUTEFORCE':
        plaintext = cc_decrypt(ciphertext, key)
        key += 1
    return plaintext

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
    print(cc_decrypt("ALZAPUN", 7))
    print(cc_decrypt("JXKAQYXKH ", 23))
    print(cc_decrypt("BSUOHWJS", -14))
    print(cc_decrypt("HUQBBOBEDWJUNJMYJXRYWDKCRUH", 135762))

    print('+++++++++++++++')
    start = time.time()
    print(cc_bruteforce('DTWVGHQTEG'))
    end = time.time()
    print("Took " + str(end-start) + " seconds to decrypt DTWVGHQTEG")
    start = time.time()
    print(cc_bruteforce('CSVUFGPSDF'))
    end = time.time()
    print("Took " + str(end-start) + " seconds to decrypt CSVUFGPSDF")
    start = time.time()
    print(cc_bruteforce('KADCNOXALN'))
    end = time.time()
    print("Took " + str(end-start) + " seconds to decrypt KADCNOXALN")
if __name__ == '__main__':
    run_tests()
