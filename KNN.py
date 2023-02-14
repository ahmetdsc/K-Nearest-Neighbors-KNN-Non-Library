def oneColumnNormalization(ColumnData):
    MaxValue=max(ColumnData)
    MinValue=min(ColumnData)
    NewColumnData=[]
    for i in ColumnData:
        Value=(i-MinValue)/(MaxValue-MinValue)
        NewColumnData.append(Value)
    return NewColumnData

def normalization(dataframe):
    for col in dataframe.columns:
        temp=dataframe[col]
        dataframe[col]=oneColumnNormalization(temp)
    return dataframe

def euclidean(FarPoint,TargetPoint):
    Distance=0
    for i in range(len(FarPoint)):
        x=FarPoint[i]-TargetPoint[i]
        Distance=Distance+(x*x)
    return Distance**0.5

def takeSecond(val):
    return val[1]

def neighborFind(example,xTrain,yTrain,k):
    neighbors = []
    boyut=xTrain.shape[0];
    for satırlar in range(boyut):
        uzaklık = euclidean(xTrain.iloc[satırlar], example)
        neighbors.append((satırlar,uzaklık,yTrain.iloc[satırlar]))
    neighbors.sort(key=takeSecond)
    neighbors=neighbors[0:k]
    return neighbors


def predectidResult(x_Train,x_Test,y_Train,kValue):
    knnPredectidResult= []
    for j in range(len(x_Test)):
        example = x_Test.iloc[j]
        neighbors = neighborFind(example,x_Train,y_Train,kValue)
        neighborTicket = []
        for neighbor in neighbors:
            neighborTicket.append(neighbor[2])
        knnPredectidResult.append(max(neighborTicket,key=neighborTicket.count))
    return knnPredectidResult
