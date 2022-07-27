from caesar_cipher import cc_decrypt
import time
def vc_encrypt(message, key):
    encryption = ""
    #Expand key to have same length as message
    orig_key = key
    key_idx = 0
    while len(key) < len(message):
        key = key + orig_key[key_idx]
        key_idx = (key_idx+1) % len(orig_key)
    for i in range(0, len(key)):
        encryption += chr(((ord(message[i]) + ord(key[i])) % 26) + 65)        
    return encryption


def vc_brute(cipher, plain, keylen):
    out = ''
    for i in range(0, len(cipher)):
        k = 0
        c = cipher[i]
        p = plain[i]
        d = ''
        while d != p:
            d = cc_decrypt(c, k)
            #print(c + ' -> ' + p)
            k += 1
        #print()
        k -= 1
        out = out + chr(k + 65)
    out = out[:keylen]
    print("KEY: " + out)
    print("PLAINTEXT: ", end='')
    vc_decrypt(cipher, out)
    return out

def vc_decrypt(encrypted_message, key):
    #Expand key to have same length as message
    orig_key = key
    key_idx = 0
    while len(key) < len(encrypted_message):
        key = key + orig_key[key_idx]
        key_idx = (key_idx+1) % len(orig_key)
    
    decryption = ""
    for i in range(0, len(key)):
        #Convert key and ciphertext to ASCII code, apply decryption, convert back to ASCII, and then to string
        decryption += chr(((ord(encrypted_message[i]) - ord(key[i])) % 26) + 65)        
    print(decryption)
    return decryption


def run_tests():
    print("======KNOWN KEY======")
    vc_decrypt("BRVLTBVAXGKPWQBRXPPNEPVAORL", "INTERN")
    vc_decrypt("UUIGRLGCKGT", "CAT")
    vc_decrypt("UPOTWABKXBNGMWTHAMTAGHSBIIZJGBPWRPBOGWXOCZFIYPBEJTRJHEPZQ", "BIGBOI")
    
    print("======BRUTE FORCE=====")
    start = time.time()
    vc_brute('EFAWSLRFIH', 'BRUTEFORCE', 3)
    end = time.time()
    print("Took " + str(end-start) + " seconds to decrypt EFAWSLRFIH")

    start = time.time()
    vc_brute('UNCZXBWXVA', 'BRUTEFORCE', 4)
    end = time.time()
    print("Took " + str(end-start) + " seconds to decrypt UNCZXBWXVA")

    start = time.time()
    vc_brute('URHZSYOEIS', 'BRUTEFORCE', 5)
    end = time.time()
    print("Took " + str(end-start) + " seconds to decrypt URHZSYOEIS")

    start = time.time()
    vc_brute('MFHZIWZFPK', 'BRUTEFORCE', 6)
    end = time.time()
    print("Took " + str(end-start) + " seconds to decrypt MFHZIWZFPK")

    print("=====ENCRYPT=====")
    print(vc_encrypt('THISMESSAGEWILLSELFDESTRUCT', 'SECURE') + ', SECURE')
if __name__ == '__main__':
    run_tests()

