
#simple gui
import tkinter as tk
from scipy.constants import lb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import sklearn

data = pd.read_csv("NEWDATA.csv")