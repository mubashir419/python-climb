import random
print("welcome to hangman game")
words=["rainbow","computer","science","programming","python"]
secret_word=random.choice(words)
display_word=[]
for letter in secret_word:
    display_word+="_"
print(display_word)
game_over=False
while not game_over:
    
    guess=input("Guess a character:")
    for positon in range(len(secret_word)):
        letter=secret_word[positon]
        if letter==guess:
            display_word[positon]=letter
    print(display_word)
    if "_" not in display_word:
        game_over=True
        print("You win")
