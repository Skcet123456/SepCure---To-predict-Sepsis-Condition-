from sklearn.metrics import confusion_matrix
import pickle
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

cls1 = pickle.load(open('model/SepsisRF.sav', 'rb'))
cls2 = pickle.load(open('model/SevereRF.sav', 'rb'))
cls3 = pickle.load(open('model/Shock.sav', 'rb'))


################## Confusion Matrix calculation #################

# Predictions for Sepsis
Y1_pred = cls1.predict(X1_test)

# Predictions for SevereSepsis
Y2_pred = cls2.predict(X2_test)

# Predictions for SepticShock
Y3_pred = cls3.predict(X3_test)

# Confusion matrix for Sepsis
cm1 = confusion_matrix(Y1_test, Y1_pred)

# Confusion matrix for SevereSepsis
cm2 = confusion_matrix(Y2_test, Y2_pred)

# Confusion matrix for SepticShock
cm3 = confusion_matrix(Y3_test, Y3_pred)

print("Confusion Matrix for Sepsis:")
print(cm1)
print("\nConfusion Matrix for SevereSepsis:")
print(cm2)
print("\nConfusion Matrix for SepticShock:")
print(cm3)


################## Calssification report - precision, recall,F1-score #################

from sklearn.metrics import classification_report

# Define target names based on the mapping
target_names = ['Normal', 'Sepsis', 'Severe Sepsis', 'Septic Shock']

# Classification report for Sepsis
cr1 = classification_report(Y1_test, Y1_pred, target_names=target_names, labels=np.unique(Y1_test))

# Classification report for SevereSepsis
cr2 = classification_report(Y2_test, Y2_pred, target_names=target_names, labels=np.unique(Y2_test))

# Classification report for SepticShock
cr3 = classification_report(Y3_test, Y3_pred, target_names=target_names, labels=np.unique(Y3_test))

print("Classification Report for Sepsis:")
print(cr1)
print("\nClassification Report for SevereSepsis:")
print(cr2)
print("\nClassification Report for SepticShock:")
print(cr3)


from sklearn.metrics import accuracy_score

# Calculate accuracy for Sepsis
accuracy1 = accuracy_score(Y1_test, Y1_pred)
print(accuracy1)

# Calculate accuracy for SevereSepsis
accuracy2 = accuracy_score(Y2_test, Y2_pred)
print(accuracy2)

# Calculate accuracy for SepticShock
accuracy3 = accuracy_score(Y3_test, Y3_pred)
print(accuracy3)

# Calculate overall accuracy
overall_accuracy = (accuracy1 + accuracy2 + accuracy3) / 3

# Print accuracy in percentage
print("Overall Accuracy: {:.2f}%".format(overall_accuracy * 100))
          