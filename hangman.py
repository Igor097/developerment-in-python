
def play_hangman():
    print('Hangman game')

    word_secret = 'Banana'

    hanged = False
    right = False

    while (not hanged and not right):

        kick = str(input('What letter ? ')).strip()
        # kick = kick.strip()

        index = 0
        for letter in word_secret:

            if (kick.upper() == letter.upper()):
                print('Letter {} in position {}'.format(letter, index))











