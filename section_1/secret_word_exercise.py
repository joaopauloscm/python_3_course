import os

secret_word = 'love'
correct_letters = ''
number_of_attempts = 0

while True:
    typed_letter = input('Type a letter: ')
    number_of_attempts += 1

    if len(typed_letter) > 1:
        print('Type only one letter.')
        continue

    if typed_letter in secret_word:
        correct_letters += typed_letter

    formed_word = ''
    for secret_letter in secret_word:
        if secret_letter in correct_letters:
            formed_word += secret_letter
        else:
            formed_word += '*'

    print('Formed word:', formed_word)

    if formed_word == secret_word:
        os.system('clear')
        print('YOU WON!! CONGRATULATIONS!')
        print('The word was', secret_word)
        print('Attempts:', number_of_attempts)
        correct_letters = ''
        number_of_attempts = 0
        exit()

