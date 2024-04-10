import random


#Generate the first random position of the array of the queens 
def generateArray8Queens():
    queensArray = []
    for _ in range(8):
        queensArray.append(random.randint(1,8))
    return queensArray

#Generate an amount of arrays of arrays of queens 
def generateQuantityOfArraysOfQueens(quantityOfArrays):
    arraysOfArraysOfQueens = []
    for _ in range(quantityOfArrays):
        arraysOfArraysOfQueens.append(generateArray8Queens())
    return arraysOfArraysOfQueens
    
#review and return the amount of queens are threaten each other in the same row
def reviewArrayOfQueenInTheSameRow(arrayOfQueens):
    amountOfThreats = 0
    for i in range(len(arrayOfQueens)):        
        for j in range(i + 1, len(arrayOfQueens)):
            if(arrayOfQueens[i] == arrayOfQueens[j]):
                amountOfThreats += 1
    return amountOfThreats
                
#review and return the amount of queens are threaten each other in diagonal
def reviewArrayOfQueenInDiagonal(arrayOfQueens):
    amountOfThreats = 0
    for i in range(len(arrayOfQueens)):
        for j in range(i + 1, len(arrayOfQueens)):
            if(i != j):
                distanceDifference = j - i
                if(arrayOfQueens[i] == (arrayOfQueens[j] - distanceDifference)):
                    amountOfThreats +=1
    return amountOfThreats

#review the arrays of queens and return the amount of threats of each array
#Return aptitude value of every array
def reviewArraysOfArraysOfQueens(arraysOfArraysOfQueens):
    amountThreatsOfEveryArray = []
    for arrayOfQueens in arraysOfArraysOfQueens:                
        amountThreats = reviewArrayOfQueenInTheSameRow(arrayOfQueens)
        amountThreats += reviewArrayOfQueenInDiagonal(arrayOfQueens)
        amountThreatsOfEveryArray.append(amountThreats)
    return amountThreatsOfEveryArray

#TEST
valTest = [[1,2,3,4,5,6,7,8]]

#Values 
objectiveFunction = 0
quantityOfArraysOfQueens = 1

#Generate init pob
arraysOfQueens = generateQuantityOfArraysOfQueens(quantityOfArraysOfQueens)

#Generate all aptitude of all arrays
allaptitudes = reviewArraysOfArraysOfQueens(arraysOfQueens)

print(arraysOfQueens)
print(allaptitudes)

