print('Welcome to Rock Paper Scissor Gaming Console')
print('In order to quit the game at any time, please enter q or quit')

while True:
    inputofA = str(input("Enter User1 choice:"))
    inputofB = str(input("Enter User2 choice:"))

    if inputofA == 'q' or inputofA == 'quit':
        print("User1 quitting the game...")
        break
    elif inputofB == 'q' or inputofB == 'quit':
        print("User2 quitting the game...")
        break

    if inputofA=='rock' and inputofB=='rock':
        print('Game is tie..,')
    elif inputofA=='rock' and inputofB=='paper':
        print('User2 won the game..,')	
    elif inputofA=='rock' and inputofB=='scissor':
        print('User1 won the game..,')    
    elif inputofA=='paper' and inputofB=='rock':
        print('User1 won the game..,')
    elif inputofA=='paper' and inputofB=='paper':
        print('Game is tie..,')
    elif inputofA=='paper' and inputofB=='scissor':
        print('User2 won the game..,')
    elif inputofA=='scissor' and inputofB=='rock':
        print('User2 won the game..,')
    elif inputofA=='scissor' and inputofB=='paper':
        print('User1 won the game..,')
    elif inputofA=='scissor' and inputofB=='scissor':
        print('Game is tie..,')
    else:
        print('Invalid input ..!')

print("Thanks for taking part in RPS Gaming.")
	