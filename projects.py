words = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape"]
import random

word = random.choice(words)
underscores = ["_"] * len(word)
guesses = []
max_guesses = 7

while "_" in underscores and len(guesses) < max_guesses:
    print(" ".join(underscores))
    guess = input("Guess a letter: ")
    
    if guess in guesses:
        print("You already guessed that letter.")
        continue
    
    guesses.append(guess)
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                underscores[i] = guess
    else:
        print("Wrong!")
    if "_" not in underscores:
       print("Congratulations, you won!")
    else:
       print("Sorry, you lost. The word was:", word)
