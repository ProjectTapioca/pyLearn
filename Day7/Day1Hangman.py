#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

#Take a random word via index and set that to a variable as a string
word_index = random.randint(0, len(word_list)-1)
random_word = word_list[word_index]

#Assigning user character guess to a variable and force lowercase
guess = str(input("Guess a letter: "))
guess.lower()

for characters in random_word:
    if guess == characters:
        print("Right")
    else:
        print("Wrong")
        
        
        
#Dr. Angela Solution
#chosedn_word = random.choice(word_index)
#guess = input("Guess a letter: ").lower()
#pretty much the same loop aside from different variable names