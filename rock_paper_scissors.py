from random import randint
from colorama import Fore, Back, Style
again = ''
while True:
    rock = 'Rock'
    paper = "Paper"
    scissors = 'Scissors'
    player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')
    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid input. Try again...')
    computer_ramdom_number = randint(1, 3)
    computer_move = ''
    if computer_ramdom_number == 1:
        computer_move = rock
    elif computer_ramdom_number == 2:
        computer_move = paper
    else:
        computer_move = scissors
    win = 0
    lost = 0
    draw = 0
    if (player_move == rock  and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
        win += 1
        print(f'{Fore.BLUE} The computer chose {Fore.BLUE + computer_move}\n{Fore.GREEN} You win!')
    elif (player_move == rock  and computer_move == rock) or \
        (player_move == paper and computer_move == paper) or \
        (player_move == scissors and computer_move == scissors):
        draw += 1
        print(f'{Fore.BLUE} The computer chose {Fore.BLUE + computer_move}\n{Fore.YELLOW} Draw!')
    elif (player_move == rock  and computer_move == paper) or \
        (player_move == paper and computer_move == scissors) or \
        (player_move == scissors and computer_move == rock):
        lost += 1
        print(f'{Fore.BLUE} The computer chose {Fore.BLUE + computer_move}\n{Fore.RED} You lost!')
    print(f'Your score is {win} win {lost} lost {draw} draw games')
    again = input(f'{Fore.WHITE} Type [any key] for YES to Play Again or [n] NO to quit: ')
    if again == 'n':
        break