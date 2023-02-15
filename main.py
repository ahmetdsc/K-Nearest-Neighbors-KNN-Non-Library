import pandas as pd
from sklearn.model_selection import train_test_split

import KNN
import ConfusionMatrix as CM

df=pd.read_csv('IrısData.csv')#Example Data from https://archive.ics.uci.edu/ml/datasets/Iris
y=df["Species"]#Class Label
df.drop("Species",axis=1,inplace=True)

KNN.normalization(df)
x_train, x_test, y_train, y_test = train_test_split(df, y, test_size = 0.2, random_state = 0)


#print(KNN.neighbor(x_test.iloc[1],x_train,y_train,3)) #Finding neigboors of a selected data

predectidResult=KNN.predectidResult(x_train, x_test, y_train, 3)#The last parameter is the k value
print(predectidResult)
"""
#Compare Predectid Result and Result 
comparedf = pd.DataFrame(y_test.values.tolist(), columns=['Result'])
comparedf['Predectid']=predectidResult
print(comparedf.to_string())
"""

ConfusionMatrix=CM.Print(predectidResult,y_test.values.tolist())
print(ConfusionMatrix.view())
CM.Accuracy(ConfusionMatrix)
