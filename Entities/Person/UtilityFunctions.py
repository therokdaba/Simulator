import random

def chooseRandomItemInArray(array):
    a = random.randint(0, len(array)-1)
    return array[a]  

def generateRandomIQ():
    #https://www.iq-brain.com/iq-test-scores/
    a = random.random()
    if a <= 0.021:
        return random.randint(0, 70)
    elif a <= 0.161:
        return random.randint(71, 85)
    elif a <= 0.5101:
        return random.randint(86, 100)
    elif a <= 0.841:
        return random.randint(101, 115)
    elif a <= 0.981:
        return random.randint(116, 145)
    elif a <= 1:
        return random.randint(146, 220)

def generateRandomStatValue(number):
    return random.randint(0, number)