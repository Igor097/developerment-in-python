
def play_hangman():
    print('Hangman game')

    word_secret = 'Banana'
    successful_letters = ['_', '_', '_', '_', '_', '_']

    hanged = False # Checks the player hanged
    right = False  # Check players' correctness

    print(successful_letters)

    while (not hanged and not right):

        kick = str(input('What letter ? ')).strip()
        # kick = kick.strip()

        index = 0
        for letter in word_secret:

            if (kick.upper() == letter.upper()):
                successful_letters[index] = letter
            index += 1

        print(successful_letters)
        print('playing ...')
    
    print('Game Over')


if (__name__ == '__main__'):
    play_hangman()









