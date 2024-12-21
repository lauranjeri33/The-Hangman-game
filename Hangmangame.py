import random
# The list of words we will be using for the game
word_list = ["Data","Laura","Zindua","Camera"]
# Number of attempts
Runs = 5

word_chosen = random.choice(word_list)

print(word_chosen)
# Create a display list with underscores for each letter in the word
display= [] *len(word)

for letter in word_chosen:
    display +="_"
    print(display)

guessed_letter = input("Guess a letter")
if letter  == guessed_letter:
    print("It's a match!")

else: 
    print("wrong guess")
Runs -=1

if "_" not in display:
    print (f"Congratulations! You guessed the word")
else:
    print(f"Game over! The word was: {word_chosen}. Better luck next time!")
