
#---------- Q1 ----------#
# Write a program in python to generate md5 of the string data

import hashlib

text = input("Enter a string : ")
h = hashlib.md5(text.encode())

print("Original string : ",text)
print("MD5 hashed string : ",end="")
print(h.hexdigest())


#%%

#---------- Q2 ----------#
# Write a program in python to generate hashes of string data using 3 algorithms from hashlib

import hashlib
import os

text = input("Enter a string : ")

print("Choose a hashing algorithms from the below list...")
print("1. sha256")
print("2. sha512")
print("3. sha224")
ch = int(input("Enter your choice : "))

if ch == 1:
    h = hashlib.sha256(text.encode())
    print("SHA256 hashed string : ",end="")
    print(h.hexdigest())
    salt = os.urandom(16) 
    key = hashlib.pbkdf2_hmac('sha256', text.encode(),salt,100).hex()
    print("Salting and Iteration string : ",key)
    
elif ch == 2:
    h = hashlib.sha512(text.encode())
    print("SHA512 hashed string : ",end="")
    print(h.hexdigest())
    salt = os.urandom(16) 
    key = hashlib.pbkdf2_hmac('sha512', text.encode(),salt,100).hex()
    print("Salting and Iteration string : ",key)
    
elif ch == 3:
    h = hashlib.sha224(text.encode())
    print("SHA224 hashed string : ",end="")
    print(h.hexdigest())
    salt = os.urandom(16) 
    key = hashlib.pbkdf2_hmac('sha224', text.encode(),salt,100).hex()
    print("Salting and Iteration string : ",key)
    
else:
    print("Enter a valid choice....")
    
    
#%%

#---------- Q3 ---------#
#Add salting and iterations to your hashes

import hashlib
import os

text = input("Enter a string : ")
t = int(input("Enter number of iterations : "))

salt = os.urandom(16) 
key = hashlib.pbkdf2_hmac('md5', text.encode(),salt,t).hex()

print("Salting and Iteration string : ",key)



