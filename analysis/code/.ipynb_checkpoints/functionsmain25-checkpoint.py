import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

def new_columns(newdf_cleaned):
    Avg_balance =( pd.cut(newdf_cleaned['Total_Revolving_Bal'] / newdf_cleaned['Months_on_book'], bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150], labels=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100','100-110','110-120','120-130','140-150','150+']).value_counts().plot(kind = "bar"))
    
    plt.figure(figsize=(10, 8))
    plt.title("Customer Average Balance")
    plt.xlabel("Balance")
    plt.ylabel("Count")
    plt.show()

def tenure(newdf_cleaned):
    
    bins = [0, 1, 2, 3, 4, 5, 6]
    labels = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6']

    customer_tenure = pd.cut(newdf_cleaned['Months_on_book'] / 12, bins=bins, labels=labels).value_counts().sort_index().plot(kind = "bar")
    
    plt.figure(figsize=(10, 8))
    plt.xlabel('Customer Tenure (years)')
    plt.ylabel('Count')
    plt.title('Histogram of Customer Tenure')
    plt.show()

def  categorize_transaction(newdf_cleaned):
    
    if trans_type in ['PURCHASE', 'RETAIL', 'ONLINE PURCHASE']:
        return 'Purchase'
    elif trans_type in ['BALANCE TRANSFER', 'BALANCE INQUIRY', 'QUASI CASH']:
        return 'Transfer'
    elif trans_type in ['CASH ADVANCE', 'ADVANCE']:
        return 'Cash Advance'
    else:
        return 'Other'

    newdf_cleaned['Transaction_Type'] = newdf_cleaned['Trans_Type'].apply(categorize_transaction)
    
    newdf_cleaned['Transaction_Type'].value_counts().plot(kind='bar')
    plt.title('Distribution of Transaction Types')
    plt.xlabel('Transaction Type')
    plt.ylabel('Count')
    plt.show()
    

    

    
