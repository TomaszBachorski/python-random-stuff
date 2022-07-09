from random import randint
from math import ceil


def generateRandomNumber(minRange, maxRange):
    number = randint(minRange, maxRange)
    return number


def binarySearch(minRange, maxRange, lookingFor):
    iterations = 0
    while maxRange != lookingFor and minRange != lookingFor:
        iterations += 1
        middle = maxRange-(maxRange-minRange)/2
        if lookingFor > middle:
            minRange = ceil(middle)
            continue
        if lookingFor < middle:
            maxRange = ceil(middle)
            continue
        if lookingFor == middle:
            break
    return iterations


def randomSearch(minRange, maxRange, lookingFor):
    iterations = 0
    while maxRange != lookingFor and minRange != lookingFor:
        iterations += 1
        split = randint(minRange, maxRange)
        if lookingFor > split:
            minRange = split
            continue
        if lookingFor < split:
            maxRange = split
            continue
        if lookingFor == split:
            break
    return iterations


minRange = 0
maxRange = 100

binaryWins, randomWins, draws = 0, 0, 0

for i in range(10000):
    lookingFor = generateRandomNumber(minRange, maxRange)
    iterationsOfBinarySearch = binarySearch(minRange, maxRange, lookingFor)
    iterationsOfRandomSearch = randomSearch(minRange, maxRange, lookingFor)
    if iterationsOfBinarySearch < iterationsOfRandomSearch:
        binaryWins += 1
    if iterationsOfBinarySearch > iterationsOfRandomSearch:
        randomWins += 1
    if iterationsOfBinarySearch == iterationsOfRandomSearch:
        draws += 1

print("Binary search wins: ", binaryWins)
print("Random search wins: ", randomWins)
print("Draws: ", draws)
