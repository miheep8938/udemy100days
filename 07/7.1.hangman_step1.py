#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random 

chosen_word = random.choice(word_list)
# chosen_word.split()
#chosen_word = list(chosen_word)

#print(chosen_word)

#print(random_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter? ").lower()

#print(guess) 

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
