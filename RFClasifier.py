import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle
from sklearn.model_selection import train_test_split


data1=pd.read_csv('data/Sepsis.csv')
data2=pd.read_csv('data/SevereSepsis.csv')
data3=pd.read_csv('data/SepticShock.csv')

#Sepsis
X1=data1.drop(columns=['Class'])
Y1=data1['Class']


#SevereSepsis
X2=data2.drop(columns=['Class'])
Y2=data2['Class']

#SepticShock
X3=data3.drop(columns=['Class'])
Y3=data3['Class']


#Preprocessing
d={'Normal':0,'Severe Sepsis':2,'Septic Shock':3,'Sepsis':1}

Y1=Y1.map(d)
Y2=Y2.map(d)
Y3=Y3.map(d)

#Train_test_split
X1_train,X1_test,Y1_train,Y1_test=train_test_split(X1,Y1,test_size=.10)
X2_train,X2_test,Y2_train,Y2_test=train_test_split(X2,Y2,test_size=.10)
X3_train,X3_test,Y3_train,Y3_test=train_test_split(X3,Y3,test_size=.10)

#Classifier Sepsis_RF
cls1=RandomForestClassifier()
cls1.fit(X1_train,Y1_train)
acc1=cls1.score(X1_test,Y1_test)
print(acc1)
Filename = "model/SepsisRF.sav"
pickle.dump(cls1,open(Filename,'wb'))


#Classifier Sepsis_Severe_RF
cls2=RandomForestClassifier()
cls2.fit(X2_train,Y2_train)
acc2=cls2.score(X2_test,Y2_test)
print(acc2)
Filename = "model/SevereRF.sav"
pickle.dump(cls2,open(Filename,'wb'))

#Classifier Septic_shock
cls3=RandomForestClassifier()
cls3.fit(X3_train,Y3_train)
acc3=cls3.score(X3_test,Y3_test)
print(acc3)
Filename = "model/Shock.sav"
pickle.dump(cls3,open(Filename,'wb'))

