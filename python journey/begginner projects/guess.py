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
