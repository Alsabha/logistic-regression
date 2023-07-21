#Importing required libraries
import numpy as np
import pandas as pd
import pylab as pl
import statsmodels.api as sm

#importing the dataset
df=pd.read_csv("binary.csv")
df.head()

#rename column names
df.columns=["admit","gre","gpa","prestige"]
df.head()



