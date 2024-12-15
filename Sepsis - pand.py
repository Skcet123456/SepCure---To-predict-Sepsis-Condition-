import random

Blood=[]
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



for x in range(30000):
      Blood.append(random.randint(60,160))
for x in range(30000):
      Urine.append(random.uniform(0,1.0))
for x in range(30000):
      Glucose.append(random.uniform(5.0,9.0))
for x in range(30000):
      Bilirubin.append(random.randint(50,90))
for x in range(30000):
      Inr.append(random.uniform(0.5,2))
for x in range(30000):
     Platelets.append(random.randint(80,120))
for x in range(30000):
      Spo.append(random.randint(70,110))
for x in range(30000):
     Heartrate.append(random.randint(90,180))
for x in range(30000):
     Respiratory.append(random.randint(10,90))
for x in range(30000):
      Wbc.append(random.randint(1,15))
for x in range(30000):
      Temp.append(random.uniform(34,40))
for x in range(30000):
     Lactate.append(random.randint(1,4))
for x in range(30000):
     Creatin.append(random.uniform(0.0,2.0))


import pandas as pd
#with open('E:/ML-Project/Sepsis/Sepsis.csv',newline='')as f:
          #w=csv.writer(f)
          #w.writrows(zip(Blood,Urine,Glucose,Bilirubin,Inr,Platelets,Spo,
                         #Heartrate,Respiratory,Wbc,Temp,Lactate,Creatin))
a=list(zip(Blood,Urine,Glucose,Bilirubin,Inr,Platelets,Spo,Heartrate,Respiratory,Wbc,Temp,Lactate,Creatin))

data=pd.DataFrame(a,columns=['Blood','Urine','Glucose','Bilirubin','Inr','Platelets','Spo','Heartrate','Respiratory','Wbc','Temp','Lactate','Creatin'])
data.to_csv('E:/ML-Project/Sepsis/Sepsis.csv',index=False)
