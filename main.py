from random import randint
from math import ceil

def generateRandomNumber(minRange, maxRange):
    number = randint(minRange, maxRange)
    return number

def binarySearch(minRange, maxRange, lookingFor):
    iterations = 0
    while maxRange!=lookingFor and minRange!=lookingFor:
        iterations+=1
        middle = maxRange-((maxRange-minRange)/2)
        if lookingFor>middle:
            minRange = ceil(maxRange-(maxRange-minRange)/2)
            continue
        if lookingFor<middle:
            maxRange=ceil(maxRange-(maxRange-minRange)/2)
            continue
        if lookingFor==middle:
            break
    return iterations

minRange = 0
maxRange = 100

randomNumber = generateRandomNumber(minRange,maxRange)
print(randomNumber)

binarySearchIterations = binarySearch(minRange, maxRange, randomNumber)
print(binarySearchIterations)