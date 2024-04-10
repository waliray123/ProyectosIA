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
                elif(arrayOfQueens[i] == (arrayOfQueens[j] + distanceDifference)):
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


#If aptitude is 0 then is resolved, if dont is not resolved
def reviewIfIsResolved(allaptitudes):
    for indexAptitude in range(len(allaptitudes)):
        if(allaptitudes[indexAptitude] == 0):
            return indexAptitude
    return -1

#return the index of the parent to select
def selecctionOfParent(totalAptitudes,allAptitudes):
    #Generate the random number of the selection
    numberToExceed = random.randint(0,totalAptitudes)
    newTotalAptitudes = 0
    for indexAptitude in range(len(allaptitudes)):
        newTotalAptitudes += allaptitudes[indexAptitude]
        if(newTotalAptitudes >= numberToExceed):
            return indexAptitude

#Realize the selection of the n parents
def selecctionOfParentsToMix(allAptitudes,arrayOfQueens,nParents):
    arrayOfQueensParents = []
    totalAptitudes = 0
    for aptitude in allAptitudes:
        totalAptitudes += aptitude
    
    for n in range(nParents):
        parentArrayOfQueens = selecctionOfParent(totalAptitudes,allAptitudes)
        arrayOfQueensParents.append(parentArrayOfQueens)

    return arrayOfQueensParents

#Merge the parents
#Get the index
#Return the sons
def mergeParentsOfArraysOfQueens(indexOfParents, arrayOfQueens):
    print("The parents are: ")
    print(arrayOfQueens[indexOfParents[0]])
    print(arrayOfQueens[indexOfParents[1]])
    
    sonsToReturn = []
    pointToMerge = random.randint(0,7)
    print("The point is")
    print(pointToMerge)
    newSon = []
    newSon2 = []
    for indexGen in range(8):
        if(pointToMerge < indexGen):
            newSon.append(arrayOfQueens[indexOfParents[0]][indexGen])
            newSon2.append(arrayOfQueens[indexOfParents[1]][indexGen])
        else:
            newSon2.append(arrayOfQueens[indexOfParents[0]][indexGen])
            newSon.append(arrayOfQueens[indexOfParents[1]][indexGen])
    sonsToReturn.append(newSon)
    sonsToReturn.append(newSon2)
        
    return sonsToReturn
    





#TEST
valTest = [[1,2,3,4,5,6,7,8]]
valTest2 = [[8,7,6,5,4,3,2,1]]

#Values 
objectiveFunction = 0
quantityOfArraysOfQueens = 10
nParents = 2
nSons = 1 # n Sons is nSons * 2

#Generate init pob
arraysOfQueens = generateQuantityOfArraysOfQueens(quantityOfArraysOfQueens)

#Generate all aptitude of all arrays
allaptitudes = reviewArraysOfArraysOfQueens(arraysOfQueens)


#Review if is resolved
isResolved = reviewIfIsResolved(allaptitudes)
if(isResolved != -1):
    print(f"The array {allaptitudes[isResolved]}")
else:
    for i in range(nSons):
        parentsOfArraysOfQueens = selecctionOfParentsToMix(allaptitudes,arraysOfQueens,nParents)                
        #Merge the parents
        sonOfArrayOfQueen = mergeParentsOfArraysOfQueens(parentsOfArraysOfQueens,arraysOfQueens)
        print("The son are:")
        print(sonOfArrayOfQueen)





print(arraysOfQueens)
print(allaptitudes)




