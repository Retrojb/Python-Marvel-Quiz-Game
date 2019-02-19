import random

lives = 9;

word_bank = ['pizza', 'otter', 'jerks', 'boobs', 'poops', 'nuggy', 'growl']

secert_word = random.choice(word_bank)
clue = list('?????')
hearts = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secert_word, clue):
    index = 0;
    while index < len(secert_word):
        if guessed_letter == secert_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print(f'Lives left {hearts * lives}')
    guess = input('Guess a letter or the whole word: ')

    if guess == secert_word:
        guessed_word_correctly == True
        print('Congraulations you got the word')
        break

    if guess in secert_word:
        update_clue(guess, secert_word, clue)
    else:
        lives = lives - 1
        print(f'incorrect answer')