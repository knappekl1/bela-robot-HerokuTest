import numpy as np
import pandas as pd
import sys

def calculateMatrix(input_all, total_sum, row_info):
    """
    input_all: List of String; includes all components of the input field, items to calculate are left blank
    total_sum: Int; target sum of all numbers in the input field
    row_info: List of Int; 2 item list, item[0] = digit count to be added, item[1] = target sum for the rows
    Returns string of all items for the input field separated by double space or Cannot calculate if there is no solution
    """
    #Get inputs, needs to get connected to front end
    rawInput = input_all
    targetSumAllRows = [len(rawInput),total_sum]
    targetSumRow = row_info
    InputRow = []
    num = int()
    idxPop = int()
    count = 0
    #tryparse
    for i in rawInput:
        try:
            num = int(i)
            InputRow.append(num)
            idxPop = count
        except:
            InputRow.append(i)
        count += 1

    # print("input row ", InputRow)

    #Slice parts
    sliceList = []
    for i in range(len(rawInput)-targetSumRow[0]+1):
        sliceList.append(InputRow[i:i+targetSumRow[0]])

    # fill in slices with Zeroes
    for s in enumerate(sliceList):
        #Insert before items
        for i in range(0,s[0]):
            s[1].insert(i,0)

        #Insert after items
        for i in range(len(s)+ s[0],len(rawInput)-1):
            s[1].append(0)   

    sliceList.insert(0,InputRow) # Add first row
    # print("Slices ",sliceList)

    #Create vector
    vector = []
    for l in sliceList:
        flag = False
        for i in l:
            if isinstance(i,int):
                if i> 0:
                    vector.append(i)
                    flag = True
        if flag==False:
            vector.append(0)

    #remove the constant at idxPop
    for s in sliceList:
        s.pop(idxPop)

    # print("\n", vector)
    #Create result vector
    resVector = []

    for i in enumerate(vector):
        if i[0] == 0:
            resVector.append(targetSumAllRows[1])
        else:
            resVector.append(targetSumRow[1])

    # print("\n", resVector)

    #Create numpy
    vectorArr = np.array(vector)
    reVecArr = np.array(resVector)
    resArr = reVecArr - vectorArr
    resArr = np.reshape(resArr,(len(vectorArr),1)) #final result vector
    # print(resArr) #TESTING
    #create matrix
    matrixArr = np.array(sliceList)

    matrixArr[matrixArr == ""]=1 #replace empty string by 1
    matrixArr = matrixArr.astype(int)
    # print(matrixArr) #TESTING

    #Calculate
    try:
        invMatrix = np.linalg.inv(matrixArr) #inverse matrix
        result = invMatrix.dot(resArr) #matrix multiplication (inverse vs resVector)
    except:
        outputString = "Příklad nemá řešení"
        return outputString
        
    #get results into original list
    #get index of all empty strings
    indexList = []
    for i in enumerate(rawInput):
        if i[1]== "":
            indexList.append(i[0])

    for i in range(len(indexList)):
        rawInput[indexList[i]] = result[i][0].astype(int).astype(str)

    outputString = " | ".join(rawInput)
    # print(outputString)
    return outputString
    
    # print(matrixArr)
    # print(invMatrix)
    # print(resArr)
    # print(result)
    #print(rawInput)

    # ConstRow = [i for i in inputRow if i > 0] # list comprehension

# result = calculateMatrix(["2","","","",""], 16, [3,11])
