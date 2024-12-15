import random

Blood1=[]
Blood2=[]
Urine=[]
Glucose=[]
Bilirubin=[]
Inr=[]
Platelets=[]
Spo=[]
Heartrate=[]
Respiratory=[]
Wbc=[]
Temp=[]
Lactate=[]
Creatin=[]
crp=[]
Con=[]


for x in range(100000):
      Blood1.append(random.randint(50,120))
for x in range(100000):
      Blood2.append(random.randint(20,85))
for x in range(100000):
      Urine.append(random.uniform(0,1.0))
for x in range(100000):
      Glucose.append(random.randint(20,60))
for x in range(100000):
      Bilirubin.append(random.uniform(1,3))
for x in range(100000):
      Inr.append(random.uniform(.9,2.3))
for x in range(100000):
     Platelets.append(random.uniform(0,7.5))
for x in range(100000):
      Spo.append(random.randint(80,100))
for x in range(100000):
     Heartrate.append(random.randint(70,120))
for x in range(100000):
     Respiratory.append(random.randint(10,30))
for x in range(100000):
      Wbc.append(random.uniform(1,15))
for x in range(100000):
      Temp.append(random.uniform(33,42))
for x in range(100000):
     Lactate.append(random.randint(1,3))
for x in range(100000):
     Creatin.append(random.uniform(0.5,2.0))
for x in range(100000):
      crp.append(random.randint(-3,3))
for x in range(100000):
      Con.append(random.randint(0,1))


import pandas as pd

a=list(zip(Blood1,Blood2,Urine,Glucose,Bilirubin,Inr,Platelets,Spo,Heartrate,Respiratory,Wbc,Temp,Lactate,Creatin,crp,Con))

data=pd.DataFrame(a,columns=['BP-systolic','BP-diastolic','Urine','Glucose','Bilirubin','Inr','Platelets(10^4)','Spo','Heartrate','Respiratory','WBC','Temp','Lactate','Creatinine','CRP','Consious'])
data.to_csv('E:/ML-Project/Sepsis/Sepsis2.csv',index=False)
