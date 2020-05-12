
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

data12 = pd.read_csv("NEWDATA.csv")
plt.plotfile('Heart_Disease_Data.csv')
plt.xticks([0,50,100,150,200,250,300],[2008,2009,2010,2011,2012,2013,2014])
plt.yticks([2006,2008,2010,2012,2014],[200,300,400,500,600])
plt.xlabel("Year")
plt.ylabel("cholestrol")
plt.grid(True)
plt.legend()
plt.show()

y = data12["YEAR"]
risk1 = data12["FINAL RISK"]
plt.hist2d(y,risk1)
plt.title("INCREASE IN HEART DISEASE RISK FROM 2006 TO 2015")
plt.xlabel("YEAR")
plt.ylabel("HEART DISEASE RISK SCORE")
plt.show()

year = np.array([2006,2007,2008,2009,2010,2011,2012,2013,2014,2015])
wts = np.array([70.11,66.8,72.25,75.667,77.83,80.433,79.63,74.32,77.23,89.67])
plt.plot(year,wts)
plt.xlabel("YEAR")
plt.ylabel("MEAN WEIGHTS")
plt.title("")
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