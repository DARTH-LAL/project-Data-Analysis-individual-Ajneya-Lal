import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

def new_columns(newdf_cleaned):
    Avg_balance =( pd.cut(newdf_cleaned['Total_Revolving_Bal'] / newdf_cleaned['Months_on_book'], bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150], labels=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100','100-110','110-120','120-130','140-150','150+']).value_counts().plot(kind = "bar"))
    
    plt.title("Customer Average Balance")
    plt.xlabel("Balance")
    plt.ylabel("Count")
    plt.show()

def tenure(newdf_cleaned):
    
    bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    labels = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12']

    customer_tenure = pd.cut(newdf_cleaned['Months_on_book'] / 12, bins=bins, labels=labels).value_counts().sort_index().plot(kind = "bar"))

    plt.xlabel('Customer Tenure (years)')
    plt.ylabel('Count')
    plt.title('Histogram of Customer Tenure')
    plt.show()

def Credit_Limit_Utilization(newdf_cleaned):
    
     Limit_Utilization = (pd.cut(newdf_cleaned['Total_Revolving_Bal'] / newdf_cleaned['Credit_Limit'], bins=[0 ,1 , 2 ,3 ,4 ,5 ,6,7,8,9,10,11,12], labels=['0-50','50-60','60-70','70-80','90-100','100-110','110-120','50-150' , '250-300','300-500', '500-1000', '1000+']).value_counts().plot(kind = "bar"))
     return Credit_Limit_Utilization
    

    

    
