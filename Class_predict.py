import pandas as pd
import numpy as np
import pickle


m1="SepsisRF.sav"
m2="SevereRF.sav"
m3="Shock.sav"

Sep1=pickle.load(open(m1,'rb'))
Sep2=pickle.load(open(m2,'rb'))
Sep3=pickle.load(open(m3,'rb'))

Res=int(input("Enter the Respiratory Rate : "))
Hrt=int(input("Enter the Heart Rate : "))
Wbc=float(input("Enter the WBC count : "))
Temp=float(input("Enter the Temp : "))
CRP=float(input("CRP : "))
CONCIOUS=float(input("CONCIOUS : "))

#Sepsis Prediction
s=Sep1.predict([[Res,Hrt,Wbc,Temp,CRP,CONCIOUS]])
if s[0]==1:
    print("Sepsis Symptomes detected")
    print("Let's Check the Stage")
    Urine=float(input("Enter the Urine Output : "))
    spo=int(input("Enter the SPO2 : "))
    #Sep2=pickle.load(open(m2,'rb'))
    d=Sep2.predict([[Urine,spo]])
    #Severe Sepsis Prediction
    if d[0]==2:
        print("------------------------")
        print("Severe Sepsis Symptomes detected")
        #Septic Shock Prediction

        print("Predicting chances for Septic shock ")
        BPSys=int(input("Enter the BP-Systolic : "))
        BPDia=int(input("Enter the Bp-Diastolic : "))
        Urine = float(input("Enter the Urine Output : "))
        Glucose=int(input("Enter the Glucose : "))
        Creatinine=float(input("Enter the Creatinine : "))
        Lactate=int(input("Enter the Lactate : "))
        Bilirubin = float(input("Enter the Bilirubin rate : "))
        Inr=float(input("Enter the Inr : "))
        Platelets=float(input("Enter the Platelets Rate : "))
        f=Sep3.predict([[BPSys,BPDia,Urine,Glucose,Creatinine,Lactate,Bilirubin,Inr,Platelets]])
        if f[0]==3:
            print("------------------------")
            print("Septic Shock may occur ")
        else:
            print("------------------------")
            print("Not having chances for septic shock ")
    else:
        print("------------------------")
        print("Sepsis Only detected")
else:
    print("------------------------")
    print("It's Normal !!!")
    
