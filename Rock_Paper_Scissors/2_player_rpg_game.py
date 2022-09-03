while True:
    p1=str(input('Player 1 please pick between rock, paper or scissors')).lower()
    p2=str(input('Player 2 please pick between rock, paper or scissors')).lower()
    if p1 == p2:
        print('This is a tie')
    elif (p1 == 'rock') and (p2== 'paper'):
        print('Congratulations Player2 you win!')
    elif (p1 == 'rock') and (p2== 'scissors'):
        print('Congratulations Player1 you win!')
    elif (p1 == 'paper') and (p2== 'rock'):
        print('Congratulations Player1 you win!')     
    elif (p1 == 'paper') and (p2== 'scissors'):
        print('Congratulations Player2 you win!')  
    elif (p1 == 'scissors') and (p2== 'rock'):
        print('Congratulations Player2 you win!')  
    elif (p1 == 'scissors') and (p2== 'paper'):
        print('Congratulations Player1 you win!')
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
