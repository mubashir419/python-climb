import random
characters='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
lenght=int(input("Enter the lenght of password:"))
password=""
for i in range(lenght):
    password += random.choice(characters)
print(password)    
