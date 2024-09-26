import random
from word_file import all_the_words

def generate_random_word(all_the_words):
    word = random.choice(all_the_words)
    while "_" in word:
        word = random.choice(all_the_words)
    return word.upper()

print("Let's play hangman!")

word = generate_random_word(all_the_words)
display_word = [] # for the game when filled game over
word_array = list(word) # convert an iterable string into a list.

for each in word_array:
    display_word.append("_")

word_length = len(word)
user_letter = 0
guessed_list = [] #to keep tracking what we had guessed

while word_length != 0 and user_letter != "exit":
    print(" ".join(display_word))
    user_letter = input("Please guess a letter: ")

    if len(user_letter.upper())>1:
        print("You should only guess a single letter! Try again!")

    if user_letter.upper() in guessed_list:
        print("You had already guessed that letter! Try again!")
    else:
        for each_letter in range(0, len(word)): #iterate until guessed all length which means they spell the word.
            if user_letter.upper() == word[each_letter]:
                display_word[each_letter] = user_letter.upper()
                word_length -= 1
    guessed_list.append(user_letter.upper())

if user_letter == "exit":
    print("Thanks for playing! see you next time!")
else:
    print(" ".join(user_letter))
    print(f"Congratulations! You guessed the word! It was {word}")






