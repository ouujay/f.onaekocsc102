import random 

def guess(x):    
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}'))
        print(guess)
        if guess > random_number:
            print('Sorry,guess again. too high')
        elif guess < random_number:
            print('sorry too low')
    print('fuck you im sure you think youre smart')
guess(40)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'is{guess} too high(H), too low (L), or corret (C)')
        if feedback == 'h':
            high = guess - 1
        elif feedback  == 'l':
            low = guess + 1
            
    

