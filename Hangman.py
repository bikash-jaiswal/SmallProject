# Write your code here
'''
 A simple hangman program 
'''
import random
from string import ascii_lowercase
print(f"H A N G M A N")
mode = ""
while(mode != "exit"):
    mode = input('Type "play" to play the game, "exit" to quit: ')
    if mode == "play":
        words = list(['python', 'java', 'kotlin', 'javascript'])
        random_word = random.choice(words)
        guess = "-"*(len(random_word))
        already_used = set()
        life = 8
        while life > 0:
            print()
            print(guess)
            letter = input(f"Input a letter: ") 
            if letter in already_used:
                print("You already typed this letter")    
                already_used.update(letter)
                continue
            elif len(letter) != 1:
                print("You should input a single letter") 
                continue
            elif letter not in ascii_lowercase:
                print("It is not an ASCII lowercase letter")
                already_used.update(letter)
                continue
            elif letter not in random_word:
                print(f"No such letter in the word")
                already_used.update(letter)
                life -= 1          
            else:
                 already_used.update(letter)
                 for i in range(len(guess)):
                     if letter == random_word[i]:
                         guess = guess[:i] + letter + guess[i+1:]  
                     
        if guess == random_word:
           print(f"You guessed the word {random_word}!")
           print("You survived!")             
        else:
            print("You are hanged!")                              
    if mode == "exit":
        break
    
    print()

    
