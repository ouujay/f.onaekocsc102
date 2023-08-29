import random
def computerguess():
    low = 1
    high = x
    feedback = ''

    while guess != 'c':
        guess = random.randint(low, high)
        feedback = input(f'is {guess} too high(H) or too low(L)').lowercase
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1


