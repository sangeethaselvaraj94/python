print('Welcome to COW & BULL Game\nRules : \n\t Input - 3 digit number\n\t COW - Correct Number and Correct Position\n\t BULL - Correct Numbber and Wrong position\n ')
import random as r

secret = r.randint(100,999)
print('Secret Number',secret)

attempts = 0

indexlist = [i for i in str(secret)]

while True:
    try:
        guess = input("Enter your guess:")
        attempts = attempts+1 
        if guess.isdigit():  
            if len(guess)!=3:
                raise ValueError("Guess should be equal to 3 digits\n")
        else:
            raise ValueError("Guess should be a number\n") 
    except ValueError as e:
        print('Invalid input..,')       
        print(e) 
        continue

    if guess!=str(secret):
        cow = 0
        bull = 0        

        for i,j in enumerate(guess):    
            try:
                if j in indexlist:                
                    if indexlist[i]==j:
                        cow=cow+1                    
                    else:
                        bull=bull+1
                    continue
            except:
                continue

        print('Your guess isn\'t right..,')
        print('You have {} cow and {} bull'.format(cow,bull))
        continue
    else:
        break
        

print('\nYou won after',attempts,'attempts.., Thanks for participating')
