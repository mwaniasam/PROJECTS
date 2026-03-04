# Guessing game
# Two Players
# Display the dashes according to the number of letters in the guessed word
# Guess the letters, replace them in the word, if wrong, take one life away, if correct, let them keep
# guessing. After six wrong guesses, GAME OVER!
import random
import hangman_stages
import words
print("=" * 70)
print("Let's play hangman!")
print("You have 6 six attempts to guess the correct letter of the word")
print("=" * 70)

# hidden_word = ["Hobby", "Reckon", "Absolutely",
#                "Philanthropy", "Physics", "Affection"]
lives = 6
chosen_word = random.choice(words.words).lower()
print(chosen_word)
display = []
for i in chosen_word:
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guessed_letter == letter:
            display[position] = guessed_letter
            print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("An innocent man hanged! GAME OVER!")
    if "_" not in display:
        game_over = True
        print("You saved a man. YOU WIN!")
    print(hangman_stages.stages[lives])
