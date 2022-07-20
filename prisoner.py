import random

# Simulates a run with the prisoners' strategy and returns True for a success
def prisonerTest(numOfPeople):

    checkLimit = numOfPeople // 2
    boxes = random.sample(range(1, numOfPeople + 1), numOfPeople)

    for prisonerNum in range(numOfPeople):

        box = boxes[prisonerNum]
        index = 0

        while index < checkLimit:
            if box - 1 == prisonerNum:
                break
            else:
                box = boxes[box - 1]
                index += 1
        else:
            return False
    return True

# Runs an infinite loop of tests approximating the success rate
def runPrisonerTest(numOfPeople):
    attempts = 0
    successCount = 0
    while True:
        attempts += 1
        if prisonerTest(numOfPeople):
            successCount += 1
        print("\tSuccess Rate: " + str(successCount / attempts * 100) + "%", end="\r")

# Script
NUM_OF_PEOPLE = 100
runPrisonerTest(NUM_OF_PEOPLE)
