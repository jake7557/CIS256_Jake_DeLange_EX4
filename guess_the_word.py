
import random
 
# Random word list
word_list = ["giraffe", "elephant", "dinosaur", "ostrich", "whale", "lizard"]
# Randomly chosen word from list

print("Please try to guess what letters are in the random word.")

# Initialized variables
guessed_letters = ""
turns = 8

# Main loop where player guesses the letters
while turns > 0:
    failed = 0
   
    # Current progress of word being guessed
    for letter in random_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("-", end=" ")
            failed += 1 # Increment count for failed letters

    if failed == 0:
        print("Congratulations! You guessed the word:", random_word)
        break # Loop breaks when all the letters are guessed

    guess = input("Try to guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters += guess

    if guess not in random_word:
        turns -= 1 # Number of turns is reduced for each attempt
        print("Wrong guess. Try another guess.")

    if turns == 0: # Once number of turns = 8, loop is ended
        print("You're out of turns! The word was:", random_word)

#Comment added to see if I'm able to add another commit correctly
