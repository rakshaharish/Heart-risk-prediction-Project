#import matplotlib.pyplot as plt
#x = [1,2,3,4]
#y = [1,2,3,4]
#plt.hist(x,y)
#plt.xlabel('X Axis')
#plt.ylabel('Y Axis')
#plt.show()

import time
from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=500, height=400)
canvas.pack()
canvas.create_oval(60,40,90,90)
for i in range(90):
    for x in range(0, 70):
        canvas.move(1, 5, 0)
        tk.update()
        time.sleep(0.05)
    for x in range(0, 70):
        canvas.move(1, -5, 0)
        tk.update()
        time.sleep(0.05)


tk.mainloop()