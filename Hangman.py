import random

print('H A N G M A N')

game_list = ['python', 'java', 'kotlin', 'javascript']


attempt = 8
tried_letters = []


correct_input = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r',
  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main_menu():
    global tried_letters, attempt
    user_input = str(input('Type "play" to play the game, "exit" to quit: '))
    print()
    print()
    while True:
        if user_input == 'play':
            attempt = 8
            tried_letters.clear()
            act_guess()
        elif user_input == 'exit':
            exit()
        else:
            user_input = input('Type "play" to play the game, "exit" to quit: ')


def act_guess():
    global choice, hint, attempt, tried_letters, correct_input, user_input
    choice = random.choice(game_list)
    hint = ('-' * (len(choice))) 
    print(hint)
    while True:
        if hint != choice:
            guess_letter = str(input('Input a letter: '))
        if guess_letter in choice and hint == choice:
            print('''You guessed the word!
You survived!''')
            print()
            main_menu()
        elif guess_letter not in choice and guess_letter not in tried_letters and guess_letter in correct_input and hint != choice and attempt == 1:
            attempt-=1 
            print('''That letter doesn't appear in the word!
You lost!''')
            print()
            main_menu()
        elif guess_letter not in correct_input and len(guess_letter) > 1 and attempt >= 1 or guess_letter == '' and attempt >= 1:
            print('You should input a single letter')
            print()
            print()
            print(hint)         
        elif guess_letter not in correct_input and len(guess_letter) == 1 and attempt >= 1 or guess_letter == int and attempt >= 1:
            print('Please enter a lowercase English letter')
            print()
            print()
            print(hint)
        elif guess_letter in tried_letters and hint != choice and attempt >= 1:
            print("You've already guessed this letter")
            print()
            print()
            print(hint)     
        else:
            if guess_letter in choice and guess_letter in correct_input and guess_letter not in tried_letters and hint != choice and attempt >= 1:
                tried_letters.append(guess_letter)
                new = ''         
                for x in range(len(choice)):
                    if guess_letter == choice[x]:
                        new += guess_letter
                    else:
                        new += hint[x]
                hint = new
                print()
                print()        
                print(hint)   
            elif guess_letter not in choice and guess_letter not in tried_letters and guess_letter in correct_input and hint != choice and attempt >= 1:
                attempt -= 1
                tried_letters.append(guess_letter)
                print("That letter doesn't appear in the word")
                print()
                print()
                print(hint)
            
           
main_menu()        
