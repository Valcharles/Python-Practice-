import random
game_option=['rock','paper','scissors']
while True:
    p1=str(input('Player 1 please pick between rock, paper or scissors')).lower()
    p2=str(random.choice(game_option))
    print('System choice is ' + p2 )
    if p1 == p2:
        print('This is a tie')
    elif (p1 == 'rock') and (p2== 'paper'):
        print('Sorry you lost')
    elif (p1 == 'rock') and (p2== 'scissors'):
        print('Congratulations you won!')
    elif (p1 == 'paper') and (p2== 'rock'):
        print('Congratulations you won!')     
    elif (p1 == 'paper') and (p2== 'scissors'):
        print('Sorry you lost!')  
    elif (p1 == 'scissors') and (p2== 'rock'):
        print('Sorry you lost!')  
    elif (p1 == 'scissors') and (p2== 'paper'):
        print('Congratulations you won!')
    else:
        print('Invalid entry')
    print('Will you like to play again?')
    print("Type 'yes' to continue and 'no' to exit")
    tryagain=str(input()).lower()
    if tryagain == 'no':
        print('Thank you for Playing.Goodbye!')
        break
    elif tryagain =='yes':
        continue
