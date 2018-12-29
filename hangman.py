
def play_hangman():
    print('Hangman game')

    word_secret = 'Banana'.upper()
    successful_letters = ['_' for letter in word_secret]

    hanged = False # Checks the player hanged
    right = False  # Check players' correctness
    error = 0

    print(successful_letters)

    while (not hanged and not right):

        kick = str(input('What letter ? ')).strip().upper()
        # kick = kick.strip()

        if (kick in word_secret):

            index = 0
            for letter in word_secret:

                if (kick == letter):
                    successful_letters[index] = letter
                index += 1
        
        else:
            error += 1

        hanged = error == 6
        right = '_' not in successful_letters
        print(successful_letters)

    if (right):
        print('You win!!')
    else:
        print('You lose!! ')
    print('Game Over')


if (__name__ == '__main__'):
    play_hangman()









