
#NOTE:
#PENDING :
#Final comparision between formula(calculated) value and graph predicte value using "scikit-learn"
#EXTRA :
#Write a note on the comparitive analysis b/w calculated value and predictive value
#CURRENT PROCESS : Compare bmi->cholestrol, Compare Weight->cholestrol
#Finally,
#Compare the AVG CHOLESTROL -> HEART RISK SCORE in graph
#A little difference is observed b/w calculated value and graph value of HEART DISEASE RISK SCORE

import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt


data = pd.read_csv("NEWDATA.csv")
c = data["cholestrol"]
y = data["YEAR"]
r = data["FINAL RISK"]
coll = np.array([100,200,300,400,500,600,700,800,900,1000])
list = np.array([np.mean(r[y==2006]), np.mean(r[y==2007]), np.mean(r[y==2008]),np.mean(r[y==2009]),np.mean(r[y==2010]),np.mean(r[y==2011]),np.mean(r[y==2012]),np.mean(r[y==2013]),np.mean(r[y==2014]),np.mean(r[y==2015])])
print(list)
yr = np.array([2006,2007,2008,2009,2010,2011,2012,2013,2014,2015])
plt.plot(coll,list)
plt.xticks([200,400,600,800,1000],[100,200,300,400,500])
plt.xlabel("Cholestrol Rates")
plt.ylabel("Heart Disease risk score")
plt.show()



print(c.describe())
plt.yticks([2,4,6,8,10],[200,300,400,500,600])
plt.xticks([200,300,400,500,600],[2006,2008,2010,2012,2014])
plt.hist(c,bins=1000)
plt.ylabel("CHOLESTROL RATES")
plt.xlabel("YEAR")
plt.title("RISK OF HEART DISEASE IN INDIA BETWEEN 2005 AND 2014")
plt.legend()
plt.show()

Exercise = [1,2,3,4]
Body_Weight = [1,2,3,4,5,6]
Food = [1,2,3,4]
Stress = [1,2,3]
Medications = [0,1]
Gender = [0,1]
Genetics = [0,1]
slices = [4,6,4,3,1,1,1]
activities = ['Exercise','Body_Weight','Food','Stress','Medications','Genetics','Gender']
cols = ['r', 'y', 'b', 'g', 'w', 'o', 'k', 'c', 'm']
plt.pie(slices, labels=activities)
plt.title("RISK FACTORS OF HEART DISEASE")
plt.legend()
plt.show()

w1 = np.array([50,55,60,65,70,75,80,85,90,95,100,105])
ht = np.array([140,145,150,155,160,165,170,175,180,185,190,195])
l1 = np.array([232.1,244.6,332.1,340.2,450.9,480.4,530.1,556.6,558.7,584.6,598,606.5])
w = data["WEIGHT(kg)"]
print(w.describe())
deciht = ht/100
bmi = w1 / (deciht*deciht)

plt.plot(bmi,l1)
plt.xticks([25.5,26.0,26.5,27.0,27.5],[19.0,19.5,20.0,20.5,21])
plt.xlabel("BODY MASS INDEX")
plt.ylabel("CHOLESTROL(in mg/dl)")
plt.title("GENERAL RELATION BETWEEN BMI AND HEART DISEASE")
plt.legend()
plt.show()

plt.scatter(w,c)
plt.xlabel("WEIGHT(in kg)")
plt.ylabel("CHOLESTROL(in mg/dl)")
plt.title("INDUVIDUAL RELATION BETWEEN BODY WEIGHT AND HEART DISEASE")
plt.legend()
plt.show()


#NOTE:
#PENDING :
#Final comparision between formula(calculated) value and graph predicte value using "scikit-learn"
#EXTRA :
#Write a note on the comparitive analysis b/w calculated value and predictive value
#CURRENT PROCESS : Compare bmi->cholestrol, Compare Weight->cholestrol
#Finally,
#Compare the AVG CHOLESTROL -> HEART RISK SCORE in graph
#A little difference is observed b/w calculated value and graph value of HEART DISEASE RISK SCORE