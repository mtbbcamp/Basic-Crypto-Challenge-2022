# Basic Crypto Challenge 
Learn and build some basic cryptography ciphers with this challenge
![image](https://user-images.githubusercontent.com/109309034/179059146-0b968f1f-ff22-423e-9f16-f7d8f0dd7f9c.png)

As many of you know encryption and decryption is a huge part of keeping all our data safe in the bank.
From social security numbers to bank accounts all of our data is not stored in its raw data format.
In this challenge you will learn some basics of cryptography, including:
  - Caesar Cipher and Vignere Cipher (Very old and famous Cipher)
  - Using modern encyrption packages
  - How to brute force solve an encryption
  
  
No matter your understanding or skill level this challenge should take no more than 2-3 hours
**I built and provided stubs in python, feel free to complete this challenge in any language of your choosing!**
As always if you need help please reach out to the Coding Challenges committee or myself (bcamp@mtb.com)

# Building a Caesar Cipher and Vignere Cipher

You all probably know what a Caesar Cipher is, or at least you know the concept behind it.
A Caesar Cipher is when a letter is replaced by another letter in the alphabet, usually done by shifting letters down the alphabet a certain distance

![image](https://user-images.githubusercontent.com/109309034/179060326-89d8f1a1-d148-4884-a57a-480567f79452.png)

Implementing this in code is a very straight forward process, simply convert all the letters to their ascii number and subtract or add the distance
In this cipher the Key is the distance we are offsetting by

#### **Task: Build a Caesar Cipher encyrption and decryption**
- Encyrption function must take input (integer(key), message_to_encrypt) and output (encrypted_message)
- Decyrption function must output (encrypted_message, integer(key)) and output (message_to_encrypt)

Note- All messages are only ASCII letters A-Z https://www.asciitable.com/ (Dont forget to account for overflow -- Z + 1 offset becomes A)
Using the following keys and encrypted messages check to make sure your functions are working:
##### **Submit the following Caesar decrypted messages:**
  - ALZAPUN - key: 7
  - JXKAQYXKH - key: 23
  - BSUOHWJS - key: (-14)
  - HUQBBOBEDWJUNJMYJXRYWDKCRUH - key: 135762

**Bonus**
  - Encrypt a message using the Caesar Cipher and submit the encrypted message and key. The winner will get their message posted in the weekly newsletter!


Now that you have built a Caesar Cipher we are going to take it a step further and implement a Vignere Cipher.
A Vignere Cipher is a Caesar Cipher except the offset for each letter is based on a word and different for each letter, instead of the same offset for every letter.
Here is an example from GeeksForGeeks - https://www.geeksforgeeks.org/vigenere-cipher/?ref=lbp

Input : Plaintext :   GEEKSFORGEEKS
             Keyword :  AYUSH
Output : Ciphertext :  GCYCZFMLYLEIM
For generating key, the given keyword is repeated
in a circular manner until it matches the length of 
the plain text.
The keyword "AYUSH" generates the key "AYUSHAYUSHAYU"
The plain text is then encrypted using the process 
explained below.

#### **Task: Build a Vigenere Cipher encyrption and decryption**
- Encyrption function must take input (string(key), message_to_encrypt) and output (encrypted_message)
- Decyrption function must output (encrypted_message, string(key)) and output (message_to_encrypt)

Remember we are only usings character A-Z on the ascii table. Be sure to check for anything outside that range and wrap around if needed.
Using the following keys and encrypted messages check to make sure your functions are working:
##### **Submit the following Vigenere decrypted messages:**
  - CSWMUCWBYHLQXRCSYQQOFQWBPSM - key: INTERN
  - VVJHSMHDLHU - key: CAT
  - VQPUXBCLYCOHNXUIBNUBHITCJJAKHCQXSQCPHXYPDAGJZQCFKUSKIFQAR - key: BIGBOI

**Bonus**
  - Encrypt a message using the Vigenere Cipher and submit the encrypted message and key. The winner will get their message posted in the weekly newsletter!


### **Task: Applying this to real life**

While these ciphers are simple to build and in concept they still require decent computing power to brute force solve. (Nothing compared to modern ciphers but still surpisingly strong).
In your last task I want you to brute force find the keys to the following encryptions. I will provide all the details expect for the key itself.
For bonus points track how long each varation takes to solve!

##### **Find the keys to the following ciphers (Bonus: track the time it takes to brute force):**
  - Caesar - DTWVGHQTEG - BRUTEFORCE - key length (3)
  - Caesar - CSVUFGPSDF - BRUTEFORCE - key length (4)
  - Caesar - KADCNOXALN - BRUTEFORCE - key length (5)
  - Vigenere - NGRFTCAGZQ - BRUTEFORCE - key length (3)
  - Vigenere - JSGZMGAXKF - BRUTEFORCE - key length (4)
  - Vigenere - EGPHYIDMQY - BRUTEFORCE - key length (5)
  - Vigenere - QEBTEFDEJE - BRUTEFORCE - key length (6) -- Will take a long time (if this takes too long feel free to abort)

# Submit the following

  - Caesar Cipher Code
  - Answers to Caesar Cipher messages
  - **Bonus Points:** Caesar Cipher encrypted message with key
 
  - Vigenere Cipher Code
  - Answers to Vigenere Cipher messages
  - **Bonus Points:** Vigenere Cipher encrypted message with key
  
  - Brute Force Solutions
  - **Bonus Points:** How long it took to brute force each solution
