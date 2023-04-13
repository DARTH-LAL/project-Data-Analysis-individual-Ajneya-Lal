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
    
    bins = [0, 1, 2, 3, 4, 5, 6]
    labels = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6']

    customer_tenure = pd.cut(newdf_cleaned['Months_on_book'] / 12, bins=bins, labels=labels).value_counts().sort_index().plot(kind = "bar")
    
    plt.xlabel('Customer Tenure (years)')
    plt.ylabel('Count')
    plt.title('Histogram of Customer Tenure')
    

def  Monthly_Utilization(newdf_cleaned):
    
    monthly_utilization_rate = (newdf_cleaned['Total_Revolving_Bal'] / newdf_cleaned['Avg_Open_To_Buy']) * 100
    
    plt.hist(monthly_utilization_rate, bins=20, edgecolor='black')
    plt.xlabel('Monthly Utilization Rate (%)')
    plt.ylabel('Count')
    plt.title('Distribution of Monthly Utilization Rate')
    plt.show()

    

    
