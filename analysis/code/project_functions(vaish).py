import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import project functions
from .. import project_functions

def load_and_process(path_to_csv_file):

   df1 = (pd.read_csv('BankChurners.csv'))\
             .drop(columns = ['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'])\
             .drop(columns = ['Avg_Utilization_Ratio','Avg_Open_To_Buy', 'Total_Trans_Ct', 'Total_Amt_Chng_Q4_Q1','Total_Ct_Chng_Q4_Q1','Total_Trans_Amt'])\
             .dropna(subset = ['Months_on_book','Total_Revolving_Bal'])\
             .reset_index(drop=True)\
             .rename(columns={"Customer_Age": "Age"}
                    )
   df2 = (
       df1
       .dropna()\
       .sort_values('Total_Revolving_Bal', ascending = False)\
       .rename(columns={"CLIENTNUM": "Client"})
   )
       
   return df2

df = project_functions.load_and_process(url_or_path_to_csv_file)
df