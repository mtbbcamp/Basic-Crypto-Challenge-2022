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
As always if you need help please reach out to the Coding Challenges committee or myself (bcamp@mtb.com)

# Building a Caesar Cipher and Vignere Cipher

You all probably know what a Caesar Cipher is, or at least you know the concept behind it.
A Caesar Cipher is when a letter is replaced by another letter in the alphabet, usually done by shifting letters down the alphabet a certain distance

![image](https://user-images.githubusercontent.com/109309034/179060326-89d8f1a1-d148-4884-a57a-480567f79452.png)

Implementing this in code is a very straight forward process, simply convert all the letters to their ascii number and subtract or add the distance
In this cipher the Key is the distance we are offsetting by

#### **Task: Build a Caesar Cipher encyrption and decryption**
- Encyrption function must take input (key, message_to_encrypt) and output (encrypted_message)
- Decyrption function must output (encrypted_message, key) and output (message_to_encrypt)

Using your new functions check against the following encrypted messages (Dont forget to account for overflow)
Note- All messages are only ASCII letters A-Z (https://www.asciitable.com/)
Using the following keys and encrypted messages check to make sure your functions are working:
##### **Submit the following decrypted messages:**
  - ALZAPUN - key: 7
  - JXKAQYXKH - key: 23
  - BSUOHWJS - key: (-14)
  - HUQBBOBEDWJUNJMYJXRYWDKCRUH - key: 135762


Now that you have built a Caesar Cipher we are going to take it a step further and implement a Vignere Cipher.
A Vignere Cipher is a Caesar Cipher except the offset for each letter is based on a word and different for each letter, instead of the same offset for every letter.
For example, if we have a key of "DOG", when we encrypt a message "PUPPY" it will update
