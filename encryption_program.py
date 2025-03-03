import random
import string

chr=" "+string.punctuation+string.ascii_letters+string.digits
chr=list(chr)
key=chr.copy()
random.shuffle(key)
print(f"characters---> {chr}")
print(f"key---> {key}")


plain_text=input("enter a message:")
cypher=""

for letter in plain_text:
    index=chr.index(letter)
    cypher+=key[index]

print(f"the orignal message: {plain_text}")
print(f"the encrypted message: {cypher}")
