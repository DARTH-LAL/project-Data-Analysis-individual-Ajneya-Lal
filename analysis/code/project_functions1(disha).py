import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import project functions
from .. import project_functions

def load_and_process(path_to_csv_file):
    df1=(
        pd.read_csv(path_to_csv_file)
        .drop(columns=['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'])\
        .drop(columns=['Total_Relationship_Count','Months_Inactive_12_mon','Contacts_Count_12_mon','Total_Revolving_Bal','Avg_Open_To_Buy','Total_Amt_Chng_Q4_Q1','Total_Trans_Amt','Total_Trans_Ct','Total_Ct_Chng_Q4_Q1','Avg_Utilization_Ratio'])\
        .rename(columns={"% of cell phone users who do mobile banking": "% mobile banking"})
    )
    df2=(
        df1
        .query('Income_Category != "Unknown"')\
        .dropna()\
        .reset_index(drop=True)\
        .sort_values('Credit_Limit', ascending=False)
    )
    return df2   

df = project_functions.load_and_process(url_or_path_to_csv_file)
df
