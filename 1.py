import pandas as pd
import numpy as np
import sklearn as sk

data= pd.read_csv('Sepsis.csv')

a=[]
for i in range(len(data)):
        if data['Blood'][i]<90 and data['Lactate'][i]>2 and data['Urine'][i]<0.5 and data['Glucose'][i]>7.7 and data['Creatin'][i]>177 and data['Bilirubin'][i]>70 and data['Inr'][i]>1.5 and data['Platelets']<100 :
                a.append('Sepsis Stock')
        elif data['Urine'][i]<0.5  and data['Spo'][i]<88 and data['Spo'][i]<92 and data['Spo'][i]>94 and data['Spo'][i]>98:
                a.append('Severe Sepsis')
        elif data['Respiratory'][i]>20 and data['Heartrate'][i]>90 and data['Wbc'][i]<4 and data['Wbc'][i]>14 and data['Temp'][i]<36 or data['Temp'][i]>38:
                a.append('Sepsis')
        else:
            a.append('Normal')

        
