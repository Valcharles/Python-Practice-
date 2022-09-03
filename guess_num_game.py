import random
counter=0 #tracks the number of guesses made.
win_ctr=0 #tracks the number of correct guesses made.
while True:
    comp_num=random.randint(1,9)
    print("The PC has picked a number between 1 & 9.\nCan you guess what number it is?")
    user_num=int(input())
    if (user_num>=1) and (user_num<=9):
        if comp_num<user_num:
            print('Your PC picked: {}'.format(comp_num))
            print('Your guess is higher')
            counter+=1
        elif comp_num>user_num:
            print('Your PC picked: {}'.format(comp_num))
            print('Your guess is lower')
            counter+=1
        elif comp_num==user_num:
            print('Your PC picked: {}'.format(comp_num))
            print('Congratulations! You guessed correctly.')
            counter+=1
            win_ctr +=1
    else:
        print('Your choice is out of range')
    print('Will you like to play again?')
    print("Type 'yes' to continue and 'exit' to quit")
    tryagain=str(input()).lower()
    if tryagain == 'exit':
        print('Your made {} guess(es)'.format(counter))
        print('You guessed correctly {} times.'.format(win_ctr))
        print('Thank you for Playing.Goodbye!')
        break
    elif tryagain =='yes':
        continue
