# Guessing game
# One Player
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

# Generate random words from the words list
chosen_word = random.choice(words.words).lower()
# print(chosen_word)
display = []
guessed_words = []
for i in chosen_word:
    display += '_'
print(" ".join(display))
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    
    # Let the user know that they already guessed that word
    if guessed_letter in guessed_words:
        print(f"You already guessed: {guessed_letter}")
        continue
    guessed_words.append(guessed_letter)
    
    # Input validation
    if len(guessed_letter) != 1 or not guessed_letter.isalpha():
        print("Please enter a single letter.")
        continue
        
    # Checking whether the letter matches any word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guessed_letter == letter:
            display[position] = guessed_letter
            print(" ".join(display))

    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("An innocent man hanged! GAME OVER!")
    if "_" not in display:
        game_over = True
        print("You saved a man. YOU WIN!")
    print(hangman_stages.stages[lives])



