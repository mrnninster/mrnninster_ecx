trip=3
import random as rand
hold=rand.randint(0,100)
def GUESS(trip,hold):
    guess=input('Guess my Value ')
    trip=int(trip)-1
    guess=int(guess)
    if(trip>0):
        if(guess>hold):
            print('Lower')
            GUESS(trip,hold)
        elif(guess<hold):
            print('Higher')
            GUESS(trip,hold)
        else:
            print('Correct')
    if(trip==0):
        print('Your final answer was off by '+str(guess-hold))
GUESS(trip,hold)