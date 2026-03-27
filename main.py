import random
import time

level = 0

print('WELCOME TO SNAKE - GUN - WATER! \n'.center(500))
print('HOW TO PLAY: \n')
print(
    '- You will have to choose between snake, water & gun\n',
    '- The interpreter will choose one of them too.\n',
    '- Between snake & water: snake wins\n',
    '- Between snake & gun: gun wins\n',
    '- Between water & gun: water wins\n',
    '- I both choose the same, there will be a tie.\n'
)



names = {
    's' : 'snake',
    'w' : 'water',
    'g' : 'gun'
}
def decider(player_choice, computer_choice,names):
    time.sleep(1)
    wins = {
        's': 'w',
        'w': 'g',
        'g': 's'
    }

    if wins[player_choice] == computer_choice:
        return [True , f'The computer chose: {names[computer_choice]}']
    else:
        return [False , f'The computer chose: {names[computer_choice]}']


while True:
    play_game = input('Do you want to start Snake Water Gun? (type "Y" to play and "N" to not play) : ').lower().strip(' ')

    if play_game in ['y' , 'n']:
        break
    else:
        print('Invalid Input! ')

if play_game == 'y':
    print('\nLets Play Snake - Gun - Water! ')


    while True:
        with open('highscore.txt' , 'r') as f:
            scores = f.readlines()

            if scores:
                score_list = [int(x) for x in scores]
                highscore = max(score_list)
            else:
                highscore = 0

        
        
        print(f'\nHighscore : {highscore}\n')
       
        while True:
            player_choice = input('\nChoose between snake(S), water(W) & gun(G): ').lower().strip(' ')

            if player_choice in ['s' , 'w' , 'g']:
                break
            else:
                print('Invalid Input! ')

        computer_choice = random.choice(['s' , 'w' , 'g'])

        while True:

            if player_choice != computer_choice:
                
                break
            else:
                time.sleep(1)
                print(f'\nThe computer chose: {names[computer_choice]}')
                print('Tie! ')
                while True:
                    player_choice = input('\nChoose Again between snake(S), water(W) & gun(G): ').lower().strip(' ')

                    if player_choice in ['s' , 'w' , 'g']:
                        break
                    else:
                        print('Invalid Input! ')
                
                computer_choice = random.choice(['s' , 'w' , 'g'])

        
        if decider(player_choice, computer_choice,names)[0]:
            print(decider(player_choice, computer_choice,names)[1])
            time.sleep(1)
            print('\nYou Win! ')
            level += 1
            with open('highscore.txt' , 'a') as f:
                f.write(str(f'{level}\n'))
            print(f'Your score is {level} points! ')
            time.sleep(0.25)
            print('\nNext Round!\n')

        else:
            print(decider(player_choice, computer_choice,names)[1])
            time.sleep(1)
            print('\nYou Lose! ')
            print(f'Your score was {level} points! ')
            time.sleep(0.25)
            while True:
                play_again = input('\nDo you want to play again? (type "Y" to play and "N" to not play) : ').lower().strip(' ')

                if play_again in ['y' , 'n']:
                    break
                else:
                    print('Invalid Input! ')

            if play_again == 'y':
                print('\nLets Play Snake - Gun - Water! \n')
                with open('highscore.txt' , 'a') as f:
                    f.write(str(f'{level}\n'))
                level = 0
            else:
                print('\nThanks for playing! \n')
                with open('highscore.txt' , 'a') as f:
                    f.write(str(f'{level}\n'))
                break

else:
    print('\nThanks for playing!\n ')

