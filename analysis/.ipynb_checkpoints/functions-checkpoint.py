import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

def new_columns(newdf_cleaned):
    Avg_balance =( pd.cut(newdf_cleaned['Total_Revolving_Bal'] / newdf_cleaned['Months_on_book'], bins=[0 , 50 , 150 ,250 ,300 ,500 ,1000], labels=['0-50','50-150' , '250-300','300-500', '500-1000', '1000+']).value_counts().plot(kind = "bar"))
    
    return Avg_balance
    

    
