# Data 301 Final Report Project Group 20A (Ajneya Lal)

## Introduction

As a mathematics major in data science and economics, I am particularly interested in exploring this dataset to understand consumer behaviour better and identify patterns and trends in credit card usage. I plan to use data visualisation and statistical analysis techniques to identify correlations between variables and to develop predictive models to identify customers who are most likely to accept new credit card offers or to default on their payments.This dataset piques my interest because credit card usage is critical to the modern economy. Therefore, knowing customer behaviour in this area is essential for businesses looking to design effective marketing tactics and analyse credit risk. I intend to obtain a deeper understanding of these challenges and help create more informed and successful business practices in the credit card sector by undertaking an analytics project on this dataset.
## Exploratory Data Analysis

EDA aims to provide a thorough understanding of the data and prepare for future data analysis tasks. This includes finding variable distributions, detecting missing or inconsistent data, analysing correlations between variables, and visualising the data using charts and graphs. In this section, you will find the exploratory data analysis for this dataset. I started with functions such as data set cleaning and later analysed the correlations between variables through various plots.

[If you would like to view  the full code of my EDA , please click here.](https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/analysis/analysis(Ajneya).ipynb)

After data processing and cleaning, we plotted the distribution of customers in the dataset based on existing and attrited customers. To see the trend of customer behaviour is this dataset.

![Churn Rates Plot](images/Churn_rates_plot.png)

![](/Users/poojalal/Desktop/DATA301/-project-group-group20A/images/Churn_rates_plot.png)


The graph above shows that the data consists mainly of existing customers. Thus the dataset is imbalanced as the dataset has more values for existing customers than churned customers. However, it does not affect our research question since there is still a churn rate of 16.07% present in the dataset. Therefore, we will identify the factors influencing customer behaviour and patterns of these 16.07% attrited customers.

From the graph above, the median age of customers who have churned is slightly higher than that of customers who have not churned. Thus, indicating a correlation between age and churn rate. However, the correlation requires further analysis for a concrete conclusion.

The third plot used to analyse correlations is a box plot to portray the relationship between the customer credit limit and churn rate. This graph helps analyse the relationship between the credit limit and customer churn rates.

![](/Users/poojalal/Desktop/DATA301/-project-group-group20A/images/Churn_rates_plot.png)

From the graph above, we can see that the attrited customers have significantly more outliers than existing customers. Thus, indicating high variability in the behaviour of attrited customers.

The plot below is a bar plot which displays the relationship between customer gender and churn rate.

The graph showcases the trend for customers based on their gender. It can be observed that the number of both attrited and existing customers is higher for female customers. However, it is important to consider that the dataset also contains more female customers. Thus, further analysis is required for a concrete conclusion.


## Question + Results

## Conclusion
