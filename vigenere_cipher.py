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
    print(encryption)
    return encryption


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
    vc_decrypt("BRVLTBVAXGKPWQBRXPPNEPVAORL", "INTERN")
    vc_decrypt("UUIGRLGCKGT", "CAT")
    vc_decrypt("UPOTWABKXBNGMWTHAMTAGHSBIIZJGBPWRPBOGWXOCZFIYPBEJTRJHEPZQ", "BIGBOI")
    vc_encrypt('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG', 'SECRET')
    vc_decrypt('LLGHYBUODISPFJQONNETUFZXJXJVPTRCFFK', 'SECRET')

if __name__ == '__main__':
    run_tests()

