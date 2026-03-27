import random
import time
print('WELCOME TO SNAKE - GUN - WATER! \n'.center(500))
print('HOW TO PLAY: \n')
print(
    '- You will have to choose between snake, water & gun\n',
    '- Te interpreter will choose one of them too.\n',
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
    if player_choice == 's' and computer_choice == 'w':
        return [True , f'The computer chose: {names[computer_choice]}']
    if player_choice == 'g' and computer_choice == 's':
        return [True , f'The computer chose: {names[computer_choice]}']
    if player_choice == 'w' and computer_choice == 'g':
        return [True , f'The computer chose: {names[computer_choice]}']
    if player_choice == 'g' and computer_choice == 'w':
        return [False , f'The computer chose: {names[computer_choice]}']
    if player_choice == 'w' and computer_choice == 's':
        return [False , f'The computer chose: {names[computer_choice]}']
    if player_choice == 's' and computer_choice == 'g':
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
            time.sleep(0.25)
            print('\nNext Round!\n')

        else:
            print(decider(player_choice, computer_choice,names)[1])
            time.sleep(1)
            print('\nYou Lose! ')
            time.sleep(0.25)
            while True:
                play_again = input('\nDo you want to play again? (type "Y" to play and "N" to not play) : ').lower().strip(' ')

                if play_again in ['y' , 'n']:
                    break
                else:
                    print('Invalid Input! ')

            if play_again == 'y':
                print('\nLets Play Snake - Gun - Water! \n')
            else:
                print('\nThanks for playing! \n')
                break

else:
    print('\nThanks for playing!\n ')