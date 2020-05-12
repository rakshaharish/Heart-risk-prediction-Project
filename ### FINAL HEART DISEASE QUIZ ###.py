"""
Note : Close each window of the GUI after reading/form-filling to move to the next window.
"""
#simple gui
import tkinter as tk
from scipy.constants import lb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image  #PILL is the pillow package for image handling in python

finalrisk = 0
sum = 0

#create window1
root = tk.Tk()
root.title("About the Quiz")
heading = tk.Label(text = "      ABOUT THE QUIZ", font=("ariel", 40, "bold"), fg="red")
heading.grid()
desc1 = tk.Label(text = "Welcome To The Heart Disease Risk Quiz.")
desc = tk.Label(text = "Description: This quiz requires the user to answer about 15 questions.")
desc2 = tk.Label(text = "Here the user can select only one option out of the given options.")
desc3 = tk.Label(text = "The choices of the user will be compared with the statistical data of the general health of Indian population from 2005-2015.")
desc4 = tk.Label(text = "This data has been extracted from www.kaggle.com website, which gives an idea about the risk factors of heart disease.")
desc5 = tk.Label(text = "The quiz will evaluate this statistical data and predict how prone the quiz participant is to the heart disease.")
desc6 = tk.Label(text = "NOTE : CORRECT RESULTS WILL BE DISPLAYED CONSIDERING THE USER'S HEIGHT IS ABOVE 100cm AND WEIGHT IS ABOVE 30kg.")
load = Image.open('a1.jpg')
render = ImageTk.PhotoImage(load)
img = tk.Label(root, image=render)
img.image = render
img.place(x=200, y=250)
desc1.grid()
desc.grid()
desc2.grid()
desc3.grid()
desc4.grid()
desc5.grid()
desc6.grid()
root.mainloop()

def GRAPHS() :
    data = pd.read_csv("NEWDATA.csv")
    c = data["cholestrol"]
    #plt.yticks([2, 4, 6, 8, 10], [200, 300, 400, 500, 600])
    #plt.xticks([200, 300, 400, 500, 600], [2006, 2008, 2010, 2012, 2014])
    #plt.hist(c, bins=1000)
    #plt.ylabel("CHOLESTROL RATES")
    #plt.xlabel("YEAR")
    #plt.title("RISK OF HEART DISEASE IN INDIA BETWEEN 2005 AND 2014")
    #plt.grid(True)
    #plt.legend()
    #plt.show()

    Exercise = [1, 2, 3, 4]
    Body_Weight = [1, 2, 3, 4, 5, 6]
    Food = [1, 2, 3, 4]
    Stress = [1, 2, 3]
    Medications = [0, 1]
    Gender = [0, 1]
    Genetics = [0, 1]
    slices = [4, 6, 4, 3, 1, 1, 1]
    activities = ['Exercise', 'Body_Weight', 'Food', 'Stress', 'Medications', 'Genetics', 'Gender']
    cols = ['r', 'y', 'b', 'g', 'w', 'o', 'k', 'c', 'm']
    plt.pie(slices, labels=activities)
    plt.title("RISK FACTORS OF HEART DISEASE")
    plt.legend()
    plt.show()

    y = data["YEAR"]
    risk1 = data["FINAL RISK"]
    plt.hist2d(y, risk1)
    plt.title("INDUVIDUAL INCREASE IN HEART DISEASE RISK FROM 2006 TO 2015")
    plt.xlabel("YEAR")
    plt.ylabel("HEART DISEASE RISK SCORE")
    plt.show()

    w1 = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])
    ht = np.array([140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195])
    l1 = np.array([232.1, 244.6, 332.1, 340.2, 450.9, 480.4, 530.1, 556.6, 558.7, 584.6, 598, 606.5])
    w = data["WEIGHT(kg)"]
    deciht = ht / 100
    bmi = w1 / (deciht * deciht)
    plt.plot(bmi, l1)
    plt.grid(True)
    plt.xticks([25.5, 26.0, 26.5, 27.0, 27.5], [19.0, 19.5, 20.0, 20.5, 21])
    plt.yticks([250,300,350,400,450,500,550,600],[50,100,150,200,250,300,350,400])
    plt.xlabel("BODY MASS INDEX")
    plt.ylabel("CHOLESTROL(in mg/dl)")
    plt.title("GENERAL RELATION BETWEEN BMI AND HEART DISEASE")
    plt.legend()
    plt.show()


    plt.scatter(w, c)
    plt.xlabel("WEIGHT(in kg)")
    plt.ylabel("CHOLESTROL(in mg/dl)")
    plt.yticks([200, 300, 400, 500, 600], [100, 200, 300, 400, 500])
    plt.title("INDUVIDUAL RELATION BETWEEN BODY WEIGHT AND HEART DISEASE")
    plt.grid(True)
    plt.legend()
    plt.show()

    list = np.array(
        [np.mean(risk1[y == 2006]), np.mean(risk1[y == 2007]), np.mean(risk1[y == 2008]), np.mean(risk1[y == 2009]),
         np.mean(risk1[y == 2010]), np.mean(risk1[y == 2011]), np.mean(risk1[y == 2012]), np.mean(risk1[y == 2013]),
         np.mean(risk1[y == 2014]), np.mean(risk1[y == 2015])])
    # print(list)
    yr = np.array([2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])
    coll = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    plt.plot(coll, list)
    plt.scatter(coll,list)
    plt.fill_between(coll, list, 0, color="yellow")
    plt.xlabel("CHOLESTROL RATES (in mg/dl)")
    plt.ylabel("AVERAGE HEART DISEASE RISK SCORE PER YEAR")
    plt.grid(True)
    plt.xticks([200,400,600,800,1000],[100,300,500,700,900])
    plt.title("GENERAL INCREASE IN HEART DISEASE RISK FROM 2006 TO 2015")
    plt.show()


    # plt.scatter(bmi,l1)
    # plt.xlabel("BODY MASS INDEX")
    # plt.ylabel("CHOLESTROL(in mg/dl)")
    # plt.title("RELATION BETWEEN BODY MASS INDEX AND HEART DISEASE")
    # plt.legend()
    # plt.show()

    # food = data["OILY FOOD(1=regular, 2=week, 3=month, 4=rare)"]
    # l2 = data["cholestrol"]
    # exercise = data["EXERCISE(1,2,3,4)"]
    # stress = data["STRESS(1,2,3=High)"]
    # plt.xticks([1,2,3,4])
    # plt.plot(food,l2)
    # plt.scatter(exercise,l2)
    # plt.scatter(stress,l2)
    # plt.show()

    # l3 = data["MEDICATION(1=Yes, 0=No)"]
    # plt.xticks([0,1])
    # plt.hist(l3,bins=2)
    # plt.show()





#create the window2
window = tk.Tk()

#modify root window
window.title("Heart Disease Risk Quiz")
#window.geometry("30000x30000")
#window.configure(background = "black")

#label
title = tk.Label(text = "                    HEART DISEASE RISK QUIZ", font=("ariel", 34,"bold"), fg="red")
title.grid()
#title = tk.Label(text = "\nHEALTHY LIFE QUIZ \n \n Welcome To The Healthy Life Quiz. \nDescription:This quiz requires the user to answer 15 multiple choice questions.Here the user can select only one option out of the given four options.The choices of the user will be compared with the statistical data of the general health of Indian population from 2005-2015.This data has been extracted from XYZ website, which gives an idea about the approximate number of people who are prone to heart disease. The quiz will evaluate this statistical data and predict how prone the quiz participant is to the heart disease")
#title.grid()

#yscroll = tk.Scrollbar(window)
#how to scroll through the form????

lab = tk.Label(text = " ")
name1 = tk.Label(text = "Enter your first name")
lab.grid()
name1.grid()
#Entry field
fname = tk.StringVar()#storing first name var
field1 = tk.Entry(window, textvariable=fname)
field1.grid(column=1, row=2)

lab1 = tk.Label(text = " ")
name2 = tk.Label(text = "Enter your last name")
lab1.grid()
name2.grid()
lname = tk.StringVar() #storing last name var
field2 = tk.Entry(window, textvariable=lname)
field2.grid(column=1, row=4)


lab3 = tk.Label(text = " ")
age = tk.Label(text = "Enter your age(in years)")
lab3.grid()
age.grid()
age1 = tk.IntVar()
field4 = tk.Entry(window, textvariable=age1)
field4.grid(column=1, row=6)

lab2 = tk.Label(text=" ")
gender = tk.Label(text = "What is your gender?")
lab2.grid()
gender.grid()
v = tk.IntVar()
male = tk.Radiobutton(window, text = "Male", variable=v, value=1)
female = tk.Radiobutton(window, text = "Female", variable=v, value=2)
#write provision to accept radio input
male.grid(column=1, row=8)
female.grid(column=2, row=8)

lab4 = tk.Label(text = " ")
weight = tk.Label(text = "Enter your weight(in kilograms)")
lab4.grid()
weight.grid()
weight1 = tk.DoubleVar()
field3 = tk.Entry(window, textvariable=weight1)
field3.grid(column=1, row=10)

lab5 = tk.Label(text = " ")
height = tk.Label(text = "Enter your height(in centimeters)")
lab5.grid()
height.grid()
height1 = tk.DoubleVar()
field5 = tk.Entry(window, textvariable=height1)
field5.grid(column=1, row=12)

lab6 = tk.Label(text = " ")
smoke = tk.Label(text = "Do you smoke?")
lab6.grid()
smoke.grid()
a = tk.IntVar()
yes1 = tk.Radiobutton(window, text="Yes", variable=a, value=1)
no1 = tk.Radiobutton(window, text="No", variable=a, value=2)
#write provision to accept radio input
yes1.grid(column=1, row=14)
no1.grid(column=2, row=14)

lab7 = tk.Label(text = " ")
cholestrol = tk.Label(text = "Do you have a history of high cholestrol?")
lab7.grid()
cholestrol.grid()
b = tk.IntVar()
yes2 = tk.Radiobutton(window, text="Yes", variable=b, value=1)
no2 = tk.Radiobutton(window, text="No", variable=b, value=2)
#write provision to accept radio input
yes2.grid(column=1, row=16)
no2.grid(column=2, row=16)

lab8 = tk.Label(text = " ")
diabetes = tk.Label(text = "Do you have a history of diabetes?")
lab8.grid()
diabetes.grid()
c = tk.IntVar()
yes3 = tk.Radiobutton(window, text="Yes", variable=c, value=1)
no3 = tk.Radiobutton(window, text="No", variable=c, value=2)
#write provision to accept radio input
yes3.grid(column=1, row=18)
no3.grid(column=2, row=18)

lab9 = tk.Label(text = " ")
stress = tk.Label(text = "How would you rate your stress/anger levels?")
lab9.grid()
stress.grid()
d = tk.IntVar()
low = tk.Radiobutton(window, text="Low", variable=d, value=1)
mid = tk.Radiobutton(window, text="Moderate", variable=d, value=2)
high = tk.Radiobutton(window, text="High", variable=d, value=3)
low.grid(column=1, row=20)
mid.grid(column=2, row=20)
high.grid(column=3, row=20)

lab10 = tk.Label(text = " ")
burn = tk.Label(text = "Have you previously experienced heart burn or nausea or fatigue?")
lab10.grid()
burn.grid()
e = tk.IntVar()
yes4 = tk.Radiobutton(window, text="Yes", variable=e, value=1)
no4 = tk.Radiobutton(window, text="No", variable=e, value=2)
yes4.grid(column=1, row=22)
no4.grid(column=2, row=22)

lab11 = tk.Label(text = " ")
family = tk.Label(text = "Do you have a family history of diabetes or hypertension or high cholestrol?")
lab11.grid()
family.grid()
f1 = tk.IntVar()
f2 = tk.IntVar()
f3 = tk.IntVar()
dia = tk.Checkbutton(window, state=tk.ACTIVE, text="Diabetes", variable=f1)
hyper = tk.Checkbutton(window, state=tk.ACTIVE, text="Hypertension", variable=f2)
highc = tk.Checkbutton(window, state=tk.ACTIVE, text="High Cholestrol", variable=f3)
dia.grid(column=1, row=24)
hyper.grid(column=2, row=24)
highc.grid(column=3, row=24)

lab12 = tk.Label(text = " ")
meds = tk.Label(text = "Do you take medications regularly?")
lab12.grid()
meds.grid()
g = tk.IntVar()
yes6 = tk.Radiobutton(window, text="Yes", variable=g, value=1)
no6 = tk.Radiobutton(window, text="No", variable=g, value=2)
yes6.grid(column=1, row=26)
no6.grid(column=2, row=26)

lab13 = tk.Label(text = " ")
diet = tk.Label(text = "Are you on a special diet or a high protein diet?")
lab13.grid()
diet.grid()
h = tk.IntVar()
yes7 = tk.Radiobutton(window, text="Yes", variable=h, value=1)
no7 = tk.Radiobutton(window, text="No", variable=h, value=2)
yes7.grid(column=1, row=28)
no7.grid(column=2, row=28)

lab14 = tk.Label(text = " ")
oil = tk.Label(text = "How often do you consume oily food or junk food?")
lab14.grid()
oil.grid()
i = tk.IntVar()
reg = tk.Radiobutton(window, text="Regularly", variable=i, value=1)
wk = tk.Radiobutton(window, text="Once a week", variable=i, value=2)
mn = tk.Radiobutton(window, text="Once a month", variable=i, value=3)
rar = tk.Radiobutton(window, text="Rarely", variable=i, value=4)
reg.grid(column=1, row=30)
wk.grid(column=2, row=30)
mn.grid(column=3, row=30)
rar.grid(column=4, row=30)
#for listbox
# oil1 = tk.Listbox(window)
#oil1.insert(1, "Regularly")
#oil1.insert(2, "Once a week")
#oil1.insert(3, "Once a month")
#oil1.insert(4, "Rarely")
#oil1.grid(column=1, row=30)

lab15 = tk.Label(text = " ")
exercise = tk.Label(text = "How often do you exercise per week?")
lab15.grid()
exercise.grid()
j = tk.IntVar()
less = tk.Radiobutton(window, text="Less than 1hr", variable=j, value=1)
mode = tk.Radiobutton(window, text="1 to 2 hrs", variable=j, value=2)
med = tk.Radiobutton(window, text="2 to 4 hrs", variable=j, value=3)
more = tk.Radiobutton(window, text="More than 4hrss", variable=j, value=4)
less.grid(column=1, row=32)
mode.grid(column=2, row=32)
med.grid(column=3, row=32)
more.grid(column=4, row=32)



def END() :


    if (age1.get() <= 0):
        print("WARNING : Age cannot be 0 or negative")
        print("\n ########## YOU HAVE NOT FILLED THE FORM CORRECTLY ##########")
        exit()

    if(age1.get()>=100):
        print("WARNING : Age only upto 100yrs is considered")
        print("\n ########## YOU HAVE NOT FILLED THE FORM CORRECTLY ##########")
        exit()

    if ((weight1.get()<=30.00)or(weight1.get()>=120)):
        print("WARNING : Considering weights above 30kg and below 120kg only")
        print("\n ########## YOU HAVE NOT FILLED THE FORM CORRECTLY ##########")
        exit()

    if ((height1.get()<=100.00)or(height1.get()>=200)):
        print("WARNING : Considering heights above 100cm and below 200cm only")
        print("\n ########## YOU HAVE NOT FILLED THE FORM CORRECTLY ##########")
        exit()


    if ((v.get())and(fname.get())and(age1.get())and(weight1.get())and(height1.get())and(a.get())and(b.get())and(c.get())and(d.get())and(e.get())and(g.get())and(h.get())and(i.get())and(j.get()))  :
        print("\n ##########  YOU HAVE SUCCESSFULLY COMPLETED THE QUIZ ##########")
        #call a defined funtion here : function implements scikit-learn and plots the  graph
        #exit()

    #window2 = tk.Tk()
    #window2.title("QUIZ FORM RESULT")
    #FORMULA of bmi = weight/(height*height)
    w = weight1.get()
    ht1 = height1.get()
    h1 = ht1/100 #height in meters
    bmi = w / (h1*h1)
    print("Hello "+str(fname.get())+" "+str(lname.get()))
    #print("YOU HAVE SUCCESSFULLY FILLED THE QUIZ FORM!!!")
    print("RESULT OF THE QUIZ : \n")
    print("User name : "+str(fname.get())+" "+str(lname.get()))
    print("User age : "+str(age1.get()))
    print("User weight : "+str(weight1.get())+"kg")
    print("User height : "+str(height1.get())+"cm")

    AGE = age1.get()
    Gender = v.get()

    if v.get()==1:
        print("Gender : MALE")
    elif v.get()==2 :
        print("Gender : FEMALE")
    else :
        print("\n WARNING : Gender Radiobutton not selected")

    if a.get()==1 :
         finalrisk = sum + 4
         print("STATUS : Smoker")
    elif a.get()==2 :
         finalrisk = sum + 0
         print("STATUS : Non-Smoker")
    else :
         finalrisk = sum + 0
         print("\n WARNING : Smoking Radiobutton not selected")

    print("FAMILY HISTORY OF HEART RELATED DISEASES : ")
    if ((f1.get() == True) and (f2.get() == True) and (f3.get() == True)):
        print("Diabetes, Hypertension and High Cholestrol")
        finalrisk = finalrisk + 1 + 2 + 3
    elif ((f2.get() == True) and (f3.get() == True)):
        print(" Hypertension and High Cholestrol")
        finalrisk = finalrisk + 2 + 3
    elif ((f1.get() == True) and (f3.get() == True)):
        print(" Diabetes and High Cholestrol")
        finalrisk = finalrisk + 1 + 3
    elif ((f1.get() == True) and (f2.get() == True)):
        print(" Diabetes and Hypertension")
        finalrisk = finalrisk + 1 + 2
    elif f1.get() == True:
        print(" Diabetes")
        finalrisk = finalrisk + 1
    elif f2.get() == True:
        print(" Hypertension")
        finalrisk = finalrisk + 2
    elif f3.get() == True:
        print(" High Cholestrol")
        finalrisk = finalrisk + 3
    else:
        print("No family history of any disease")



    print("User BMI(Body Mass Index) : " + str(bmi) + "\n     {NOTE : BMI between 18.5 and 22.9 is said to be normal.}")


    if b.get()==1 :
        finalrisk = finalrisk + 2   #yes -> history of high cholestrol
    elif b.get()==2 :
        finalrisk = finalrisk + 0   #no -> no history of high cholestrol
    else :
        print("\n WARNING : Cholestrol Radiobutton not selected")


    if c.get()==1 :
        finalrisk = finalrisk + 1    #yes -> history of diabetes
    elif c.get()==2 :
        finalrisk = finalrisk + 0     #no -> no history of diabetes
    else :
        print("\n WARNING : Diabetes Radiobutton not selected")


    if d.get()==1 :
        finalrisk = finalrisk + 1#Low Stress
    elif d.get()==2 :
        finalrisk = finalrisk + 2#Moderate Stress
    elif d.get()==3 :
        finalrisk = finalrisk + 3#High Stress
    else :
        print("\n WARNING : Stress Radiobutton not selected")


    if e.get()==1 :
         finalrisk = finalrisk + 1#Yes -> previous attacks
    elif e.get()==2 :
         finalrisk = finalrisk + 0#No -> no previous attacks
    else :
        print("\n WARNING : Previous Attacks RadioButton not selected")


    if g.get()==1 : #Yes -> Regular medications
        finalrisk = finalrisk + 1
    elif g.get()==2 : #No -> No regular medications
        finalrisk = finalrisk + 0
    else :
        print("\n WARNING : Medications Radiobutton not selected")


    if h.get()==1 :#Yes -> On a special diet
        finalrisk = finalrisk + 0
    elif  h.get()==2 : #NO -> Not on a special  diet
        finalrisk = finalrisk + 1
    else :
        print("\n WARNING : Special Diet Radiobutton not selected")


    if i.get()==1 :#Regular oily food consumption
        finalrisk = finalrisk + 3
    elif i.get()==2 :#Once a week oily food consumption
        finalrisk = finalrisk + 2
    elif i.get()==3 :#Once a month oily food consumption
        finalrisk = finalrisk + 1
    elif i.get()==4 :#Rare oily food conssumption
        finalrisk = finalrisk + 0
    else :
        print("\n WARNING : Oily Food Radiobutton not selected")


    if j.get()==1 :#Exercise < 1hr per week
        finalrisk = finalrisk + 3
    elif j.get()==2 :# 1-2hrs exercise per week
        finalrisk = finalrisk + 2
    elif j.get()==3 :# 2-4hrs exercise per week
        finalrisk = finalrisk + 1
    elif j.get()==4 :#Exercise >4hrs per week
        finalrisk = finalrisk + 0
    else :
        print("\n WARNING : Exercise Radiobutton not selected")

    if (Gender == 1):
        if (AGE < 55):
            finalrisk = finalrisk + 2
        elif ((AGE >= 55) and (AGE <= 65)):
            finalrisk = finalrisk + 3
        elif ((AGE > 65) and (AGE < 75)):
            finalrisk = finalrisk + 4
        else:
            finalrisk = finalrisk + 5

    if(Gender==2):
        if (AGE < 55):
            finalrisk = finalrisk + 1
        elif ((AGE >= 55) and (AGE <= 65)):
            finalrisk = finalrisk + 2
        elif ((AGE > 65) and (AGE < 75)):
            finalrisk = finalrisk + 3
        else:
            finalrisk = finalrisk + 5


    if ((v.get())and(fname.get())and(age1.get())and(weight1.get())and(height1.get())and(a.get())and(b.get())and(c.get())and(d.get())and(e.get())and(g.get())and(h.get())and(i.get())and(j.get()))  :
        print()
        print()
        print("FORMULA CALCULATED VALUES : ")
        print()
        print("FINAL CALCULATED HEART DISEASE RISK SCORE [Min=2, Max=30] : " + str(finalrisk))

        if (finalrisk <= 4):
            print("PERCENTAGE OF HEART DISEASE RISK : Less than 3%")
            print("PREDICTION FOR NEXT 10 YEARS: Very low risk. Heart attack is extremely unlikely.")
        elif ((finalrisk >= 5) and (finalrisk <= 9)):
            print("PERCENTAGE OF HEART DISEASE RISK : 3-8%")
            print(
                "PREDICTION FOR NEXT 10 YEARS : Low risk. You are doing most things right, but you can probably do some fine-tuning. If you pay attention, you will live a long, healthy, active, and productive life.")
        elif ((finalrisk >= 10) and (finalrisk <= 13)):
            print("PERCENTAGE OF HEART DISEASE RISK : 9-14%")
            print(
                "PREDICTION FOR NEXT 10 YEARS: Moderate risk. You do some things right, but you have work to do. Identify your risk factors and take corrective action.")
        elif ((finalrisk >= 14) and (finalrisk <= 16)):
            print("PERCENTAGE OF HEART DISEASE RISK : 15-19%")
            print(
                "PREDICTION FOR NEXT 10 YEARS: High risk. You stand a good chance of having a first heart attack before you are 55, if male, and 65, if female.  If you have already had a heart attack, you are at high risk for a repeat performance.")
        else:
            print("PERCENTAGE OF HEART DISEASE RISK : More than 20%")
            print(
                "PREDICTION FOR THE NEXT 10 YEARS :  Extreme risk. Unless you have a death wish, you have work to do. It will take time and effort to move to the lower risk categories. The process of change should be slow, committed, persistent, and permanent. ")

        print()
        print()

        accuracy = finalrisk
        err = 0

        print("DATA ANALYSIS PREDICTION VALUES : ")
        print()
        if(weight1.get()<=40) :
            print("PREDICTED CHOLESTROL RATE : Less than 100mg/dl")
            print("PREDICTED HEART DISEASE RISK SCORE : 0 - 5")
            err = (1/4)*((5-accuracy)*(5-accuracy))
            print("Percentage Error in risk score prediction = ",err)
        elif(weight1.get()>40 and weight1.get()<=60) :
            print("PREDICTED CHOLESTROL LEVEL : 100mg/dl - 200mg/dl")
            print("PREDICTED HEART DISEASE RISK SCORE : 5 - 10")
            err = (1 / 4) * ((10 - accuracy) *(10-accuracy))
            print("Percentage Error in risk score prediction = ", err)
        elif(weight1.get()>60 and weight1.get()<=70) :
            print("PREDICTED CHOLESTROL RATE : 200mg/dl - 300mg/dl")
            print("PREDICTED HEART DISEASE RISK SCORE : 7 - 12")
            err = (1 / 4) * ((12 - accuracy) *(12-accuracy))
            print("Percentage Error in risk score prediction = ", err)
        elif(weight1.get()>70 and weight1.get()<=80) :
            print("PREDICTED CHOLESTROL RATE : 300mg/dl - 400mg/dl")
            print("PREDICTED HEART DISEASE RISK SCORE : 9 - 14")
            err = (1 / 4) * ((14 - accuracy)*(14-accuracy))
            print("Percentage Error in risk score prediction = ", err)
        elif(weight1.get()>80 and weight1.get()<=90) :
            print("PREDICTED CHOLESTROL RATE : 400mg/dl - 450mg/dl")
            print("PREDICTED HEART DISEASE RISK SCORE : 10 - 15")
            err = (1 / 4) * ((15 - accuracy) *(15-accuracy))
            print("Percentage Error in risk score prediction = ", err)
        elif(weight1.get()>90 and weight1.get()<=100) :
            print("PREDICTED CHOLESTROL RATE : 450mg/dl - 500mg/dl")
            print("PREDICTED HEART DISEASE RISK SCORE : 13 - 18")
            err = (1 / 4) * ((18 - accuracy) *(18-accuracy))
            print("Percentage Error in risk score prediction = ", err)
        elif(weight1.get()>100 and weight1.get()<=110) :
            print("PREDICTED CHOLESTROL RATE : 500mg/dl - 600mg/dl")
            print("WARNING : Risk of Hyperglycemia disease, ie, excessive cholestrol rates. ")
            print("PREDICTED HEART DISEASE RISK SCORE : 15 - 22")
            err = (1 / 4) * ((22 - accuracy) *(22-accuracy))
            print("Percentage Error in risk score prediction = ",err)
        elif(weight1.get()>110 and weight1.get()<=120) :
            print("PREDICTED CHOLESTROL RATE : More than 600mg/dl")
            print("WARNING : Risk of Hyperglycemia disease, ie, excessive cholestrol rates.")
            print("PREDICTED HEART DISEASE RISK SCORE : More than 25")
        else :
            print()


        GRAPHS()
        #call a defined funtion here : function implements scikit-learn and plots the  graph
        #exit()
    else :
        print("\n ########## YOU HAVE NOT FILLED THE FORM CORRECTLY ##########")
        exit()

    #window2.mainloop()

button1 = tk.Button(text = "SUBMIT", bg="yellow", command=END)
button1.grid(column=0, row=33)


#to create text field
##text1 = tk.Text(master=window, height=10, width=30)
##text1.grid()

#start the eventloop
window.mainloop()

#Creating the final last window
#Thank You window
window2 = tk.Tk()
window2.title("RESULT")
header1 = tk.Label(text = "THANK YOU", font=("ariel", 100, "bold"), fg="red")
header1.grid()
window2.mainloop()


#NOTE:
#PENDING :
#Final comparision between formula(calculated) value and graph predicte value using "scikit-learn"
#EXTRA :
#Write a note on the comparitive analysis b/w calculated value and predictive value
#CURRENT PROCESS : Compare bmi->cholestrol, Compare Weight->cholestrol
#Finally,
#Compare the AVG CHOLESTROL -> HEART RISK SCORE in graph
#A little difference is observed b/w calculated value and graph value of HEART DISEASE RISK SCORE
