import random

def play_hangman():

    print_opening_message()

    word_secret = word_generator()

    successful_letters = letter_generator(word_secret) 

    print(successful_letters)

    hanged = False # Checks the player hanged
    right = False  # Check players' correctness
    error = 0

    while (not hanged and not right):

        kick = report_a_kick()
        # kick = kick.strip()

        if (kick in word_secret):
            checks_a_right_kick(kick, successful_letters, word_secret)
        else:
            error += 1
            draw_hangman(error)

        hanged = error == 7
        right = '_' not in successful_letters
        print(successful_letters)

    if (right):
        print_winning_message()
    else:
        print_losing_message(word_secret)
    print('Game Over')

def draw_hangman(error):
    print("  _______     ")
    print(" |/      |    ")

    if(error == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(error == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(error == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(error == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(error == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(error == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (error == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def print_losing_message(word_secret):
    print('You lose!!')
    print('Word secret : {}'.format(word_secret))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_winning_message():
    print('You win!! ')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def checks_a_right_kick(kick, successful_letters, word_secret):

    index = 0
    for letter in word_secret:
        if (kick == letter):
            successful_letters[index] = letter
        index += 1

def word_generator():

    file = open('words.txt', 'r')
    words = []

    for row in file:
        row = row.strip()
        words.append(row)

    file.close()

    number = random.randrange(0, len(words))
    word_secret = words[number].upper()

    return word_secret

def print_opening_message():
    
    print('Hangman game')

def letter_generator(word):

    return ['_' for letter in word]

def report_a_kick():
    
    kick = str(input('What letter ? ')).strip().upper()
    return kick

if (__name__ == '__main__'):
    play_hangman()





