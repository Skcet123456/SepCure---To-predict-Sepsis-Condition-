import pandas as pd
import warnings

data=pd.read_csv('Sepsis2.csv')


X1=data[['Respiratory','Heartrate', 'WBC','Temp','CRP','Consious']]

X2=data[['Urine','Spo']]

X3=data[['BP-systolic','BP-diastolic','Urine','Glucose','Creatinine','Lactate','Bilirubin','Inr','Platelets(10^4)']]

a=[]
b=[]
c=[]

warnings.filterwarnings('ignore')
for i in range(len(X1)):
    if X1['Respiratory'][i]>20 and X1['Heartrate'][i]>90 and X1['WBC'][i]<4.5 or X1['WBC'][i]>11 and  X1['Temp'][i]<36 or X1['Temp'][i]>38 or X1['Consious'][i]==1   :
        if X1['CRP'][i]>=0:
            a.append('Sepsis')
        else:
            a.append('Normal')
    elif X1['Respiratory'][i]<20 and X1['CRP'][i]<0 and X1['Heartrate'][i]<=90 and X1['WBC'][i]>=4.5 and X1['WBC'][i]<11 and  X1['Temp'][i]>=36 and X1['Temp'][i]<=38 or X1['Consious'][i]==0:
        a.append('Normal')
    else:
        if X1['CRP'][i]>=0:
            a.append('Sepsis')
        else:
            a.append('Normal')
for j in range(len(X2)):
    if X2['Urine'][j]<0.5 and X2['Spo'][j]<93:
        b.append('Severe Sepsis')
    else:
        b.append('Sepsis')
for k in range(len(X3)):
    if X3['BP-systolic'][k]<70 or X3['BP-systolic'][k]>110 and X3['BP-diastolic'][k]<40 or X3['BP-diastolic'][k]>70 or X3['Lactate'][k]>=2 and X3['Urine'][k]<0.5 or X3['Glucose'][k]<40 or X3['Creatinine'][k]>1.3 and X3['Bilirubin'][k]>=2.0 and X3['Inr'][k]>1.5 and X3['Platelets(10^4)'][k]<=1.5 or X3['Platelets(10^4)'][k]>5.0 :
        c.append('Septic Shock')
    else:
        c.append('Severe Sepsis')

X1['Class']=a
X2['Class']=b
X3['Class']=c


X1.to_csv('E:/ML-Project/Sepsis/data/Sepsis.csv',index=False)
X2.to_csv('E:/ML-Project/Sepsis/data/SevereSepsis.csv',index=False)
X3.to_csv('E:/ML-Project/Sepsis/data/SepticShock.csv',index=False)
