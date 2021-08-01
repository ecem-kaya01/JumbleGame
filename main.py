import words
import random

get_word = random.choice(words.wordList)
word = get_word["word"]
mix = " "
correct = word
name = input("Enter your name: ")

while word:
    position = random.randrange(len(word))
    mix += word[position]
    word = word[:position] + word[(position + 1):]

print(
    f"""
      HELLO  {name} !
      Welcome to WORD JUMBLE!!!
      YOU SHOULD GET MEANINGFUL WORDS BY ARRANGING THE WORDS !
      (press the enter key at prompt to quit)
    """
)

print( "The meaning of word: ", get_word["meaning"], " \n  The jumble is: ", mix)
guess = input("Your guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not true, try again ! ")
    guess = input("Your guess: ")

if guess == correct:
    print("That's true, you guessed it! Congratulations !!! \n")

print("Thanks for playing! ")
input("Press the enter key to exit")
