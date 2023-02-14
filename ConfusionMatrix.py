import numpy as np

def Print(PredectidResult,ActualResult):
    if len(set(PredectidResult))>len(set(ActualResult)):
        s = [len(set(PredectidResult)),len(set(PredectidResult))]
        A=np.zeros(s,dtype = int)
    else:
        s = [len(set(ActualResult)),len(set(ActualResult))]
        A=np.zeros(s,dtype = int)

    ClassType=list(set(ActualResult))
    for i in range(len(ActualResult)):
        for j in range(len(ClassType)):
            if ActualResult[i] == ClassType[j]:
                FirstType=j
        for j in range(len(ClassType)):
            if PredectidResult[i] == ClassType[j]:
                SecondType=j
        A[FirstType][SecondType]=A[FirstType][SecondType]+1
    return A


def Accuracy(matrix):
    print("Accuracy", end=" : ")
    trueTotal=0
    allTotal=0
    for i in range(matrix.shape[0]):
        trueTotal=matrix[i][i]+trueTotal
        for j in range(matrix.shape[0]):
            allTotal=matrix[i][j]+allTotal
    return print(trueTotal/allTotal)
