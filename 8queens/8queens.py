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

#review the arrays of queens and return the amount of not threats of each array
def reviewArraysOfArraysOfQueens(arraysOfArraysOfQueens):
    amountThreatsOfEveryArray = []
    for arrayOfQueens in arraysOfArraysOfQueens:                
        amountThreats = reviewArrayOfQueenInTheSameRow(arrayOfQueens)
        amountThreats += reviewArrayOfQueenInDiagonal(arrayOfQueens)
        amountThreatsOfEveryArray.append(amountThreats)
    return amountThreatsOfEveryArray
    

quantityOfArraysOfQueens = 1
arraysOfQueens = generateQuantityOfArraysOfQueens(quantityOfArraysOfQueens)
valTest = [[1,2,3,4,5,6,7,8]]
print(arraysOfQueens)
print(reviewArraysOfArraysOfQueens(arraysOfQueens))




