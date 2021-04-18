# References:
# 1. https://www.kaggle.com/dejavu23/titanic-eda-to-ml-beginner
# 2. https://seaborn.pydata.org/generated/seaborn.pointplot.html#seaborn.pointplot 
# 3. http://man.hubwiz.com/docset/Seaborn.docset/Contents/Resources/Documents/tutorial/categorical.html#categorical-tutorial

# imports
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
#import scipy.stats as iqr
import scipy.stats as stats


#  some pandas options controlling output format
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)

# read data into DataFrames
df_weatherAus = pd.read_csv("../dataset//weatherAUS.csv")



col = df_weatherAus.loc[:, "MinTemp":"MaxTemp"]
df_weatherAus['average_mean_temperature'] = col.mean(axis=1)
h1 = df_weatherAus['average_mean_temperature'].tolist()
h2 = df_weatherAus['Humidity9am'].tolist()
h3 = df_weatherAus['Humidity3pm'].tolist()
h1.sort()
pdf = stats.norm.pdf(h1,h2,h3)
plt.plot(h1, pdf) 
plt.show()








