import random

game_terms=['r','p','s']
running=True
while running:
    computer_choice=random.choice(game_terms)
    user_input=input('''enter 'r' for ROCK |'p' for paper |'s' for scisso: ''').lower()  
    if user_input not in game_terms:
        user_input=input('''please enter 'r' for ROCK |'p' for paper |'s' for scissor: ''').lower()  
    print(f'your choice is {user_input}')
    print(f'''computer's choice is {computer_choice}''')
    if user_input==computer_choice:
        print('its a tie!')
    elif user_input=='s' and computer_choice=='p':
        print('you won!')
    elif user_input=='r' and computer_choice=='s':
        print('you won!')
    elif user_input=='p' and computer_choice=='r':
        print('you won!')
    else:
        print('oops! computer won')
    again=input('''do you want to play again enter 'y' for yes | 'n' for no''').lower()
    if not again=='y':
        running=False
print('thankyou')
    
  

