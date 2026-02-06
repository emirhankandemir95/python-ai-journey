# # # def donate_hesapla(miktar, birim):
# # #     print(f"Wooow! Chysro'ya {miktar} {birim} bağış geldi! Teşekkürler!")
# # # donate_hesapla(50,'TL')
# # # def dolar_cevir(dolar_miktari):
# # #     kur = 34
# # #     tl_karsiligi = dolar_miktari * kur
# # #     return tl_karsiligi
# # # gelen_para = dolar_cevir(34)
# # # print(f'Hesabına {gelen_para}TL yattı.')



# # def kare_al(sayi):
# #     result = sayi * sayi
# #     return result
# # gelencevap = kare_al(5)
# # print(gelencevap)


# def yas_hesapla(dogum_yili):
#     sum = 2025 - dogum_yili
#     return sum
# summy = yas_hesapla(2000)
# print(summy)

import random

# Hangman visuals (ASCII Art)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 / |  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
   |  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
game_over = False

# STEP 1: Initialize the display with underscores
display = []
for _ in range(word_length):
    display.append("_")

# STEP 2: Main Game Loop
while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check if the user has already guessed this letter
    if guess in display:
        print(f"You've already guessed {guess}")

    # STEP 3: Check the guessed letter against the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # STEP 4: Handle wrong guesses
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        
        # Check if the user has run out of lives
        if lives == 0:
            game_over = True
            print(stages[0])
            print(f"You lose! The word was: {chosen_word}")

    # Show the current state of the game
    if not game_over:
        print(stages[lives])
        print(f"{' '.join(display)}")

    # STEP 5: Check if the user has won
    if "_" not in display:
        game_over = True
        print("You win!")