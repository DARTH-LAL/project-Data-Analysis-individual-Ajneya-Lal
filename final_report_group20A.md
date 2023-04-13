# Data 301 Final Report Project Group 20A (Ajneya Lal)

## Introduction

As a mathematics major in data science and economics, I am particularly interested in exploring this dataset to understand consumer behaviour better and identify patterns and trends in credit card usage. I plan to use data visualisation and statistical analysis techniques to identify correlations between variables and to develop predictive models to identify customers who are most likely to accept new credit card offers or to default on their payments.This dataset piques my interest because credit card usage is critical to the modern economy. Therefore, knowing customer behaviour in this area is essential for businesses looking to design effective marketing tactics and analyse credit risk. I intend to obtain a deeper understanding of these challenges and help create more informed and successful business practices in the credit card sector by undertaking an analytics project on this dataset.

## Exploratory Data Analysis

EDA aims to provide a thorough understanding of the data and prepare for future data analysis tasks. This includes finding variable distributions, detecting missing or inconsistent data, analysing correlations between variables, and visualising the data using charts and graphs. In this section, you will find the exploratory data analysis for this dataset. I started with functions such as data set cleaning and later analysed the correlations between variables through various plots.

After data processing and cleaning, we plotted the distribution of customers in the dataset based on existing and attrited customers. To see the trend of customer behaviour is this dataset.

<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/Churn_rates_plot.png />

The graph above shows that the data consists mainly of existing customers. Thus the dataset is imbalanced as the dataset has more values for existing customers than churned customers. However, it does not affect our research question since there is still a churn rate of 16.07% present in the dataset. Therefore, we will identify the factors influencing customer behaviour and patterns of these 16.07% attrited customers.

<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/1.png />

From the graph above, the median age of customers who have churned is slightly higher than that of customers who have not churned. Thus, indicating a correlation between age and churn rate. However, the correlation requires further analysis for a concrete conclusion.

The third plot used to analyse correlations is a box plot to portray the relationship between the customer credit limit and churn rate. This graph helps analyse the relationship between the credit limit and customer churn rates.


<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/2.png />

From the graph above, we can see that the attrited customers have significantly more outliers than existing customers. Thus, indicating high variability in the behaviour of attrited customers.

The plot below is a bar plot which displays the relationship between customer gender and churn rate.

<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/3.png />

The graph showcases the trend for customers based on their gender. It can be observed that the number of both attrited and existing customers is higher for female customers. However, it is important to consider that the dataset also contains more female customers. Thus, further analysis is required for a concrete conclusion.

The following graph highlights the relationship between education level and churn rate, which is necessary for our research as it will tell us the distribution of the customers in the dataset based on their education level.

<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/4.png />

From the graph above, the churn rates for graduate education level customers are the highest. Still, it is also important to remember that the number of graduate customers is significantly higher. However, further analysis is required for a concrete conclusion.

The graph below shows the relationship between marital status and churn rates, which is essential as it aids in comprehending how marital status affects the churn rate for credit card firms.

<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/5.png />

The graph shows that the churn rate for married and single customers is the highest. Still, it is also essential to consider that the number of married and single customers is significantly higher. Therefore, further analysis is required for a concrete conclusion.

The following graph highlights the relationship between income category and churn rate, which can help understand the impact of income on customer churn for credit card companies.

<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/6.png />


From the above graph, we can conclude that the churn rates are the highest for customers in the less than 40k income category. Still, it is also essential to consider that the number of customers in the less than $40k income category is also significantly higher. Therefore, further analysis is required for a concrete conclusion.

The last graph used in this EDA is a count plot that showcases the correlation between the card category of customers and churn rate. The count plot shows the distribution of consumers among 
various Card Categories and the proportion of customers who churned or not in each category.

!<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/7.png />

From the graph above, it can be observed that the churn rates are the highest for customers in the blue card category. However, it is also essential to consider that the number of customers in the blue card category is significantly higher. Therefore, further analysis is required for a concrete conclusion.

[If you would like to view the full code of my EDA , please click here.](https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/analysis/analysis(Ajneya).ipynb)

## Research Question 1 :

How do demographics, such as age and income, affect credit card churn rates?

This question aims to understand how demographic factors may influence customer churn in credit card services. By analysing the relationship between demographic variables and churn rates, we can gain insight into which customer segments are most at risk of churn.

Analysis plan: I will begin by dividing the dataset into different demographic segments, such as age groups or income brackets, and comparing churn rates between these groups. Then  use regression analysis to model the relationship between demographic variables and churn rates, controlling for other factors that may also influence churn.


## Results for Research Question 1 :

For analysing my dataset based on the research question analysis, I  have performed a descriptive analysis of the demographic variables present in the dataset and their respective churn rates. By making histograms, box plots, or other visual representations of the distribution of the values, one can spot outliers or different odd patterns.

The demographic variables identified from the dataset and are used in this analysis are :

1.Customer Age 

2.Gender

3.Education Level

4.Income Category

5.Marital Status

6.Card Category

### Analysis for correlation between customer age and churn rates:

<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/9.png />

The graph above is a line plot showing the churn rate distribution for each group. For example, the chart above shows that the churn rates are the highest among the 65 to 70 age group.

Next, to understand the correlation between customer age and churn rates. I will be using the machine learning model of linear regression. Below is the output for a simple linear regression performed for this correlation.

<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/10.png />

From the linear regression it can be concluded that : 
1. For every one increase in customer age , we can expect an increase of 0.0008 in churn rate , as the coefficient of customer age is 0.0008. 
2. Since the R-squared value is very less , this means that customer age by itself is not a strong indicater of churn rates.
3. Since the p-valye is less than 0.05. , this means the relationship between age and churn is statistically significant.

Therefore, it is safe to conclude there is a positive correlation between customer age and churn rates and our guess about a significant correlation between them was true.

### Analysis for correlation between gender and churn rates:

During our EDA, we had already learnt that more female customers were present in the dataset than male customers. Therefore, taking churn rates based on this would not provide accurate patterns or trends. So, to overcome this challenge, the below graph showcases the churn rate for gender based on the ratio of each gender. By doing, this, we get a more accurate graph.


<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/11.png />

From the graph above, it can be observed that females still have higher churn rates than males based on the ratio. Therefore, we can conclude that females have higher churn rates than men.

We have not performed linear regression for this correlation, as only two variables exist. Also, gender is a categorical variable. Therefore, a linear regression analysis cannot use gender as an independent variable.

### Analysis for correlation between education level and churn rates:

 From our EDA, we already know that more customers are present in graduate-level education. Therefore, taking churn rates based on this would not provide accurate patterns or trends. So, to overcome a similar challenge, the graph below showcases the churn rate for education level based on the ratio of each education level. By doing, this, we get a more accurate graph.

 
<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/12.png />

 The graph above shows that the doctorate education level still has a Significantly higher ratio churn rate than the rest of the education levels. Therefore, the doctorate education level has the highest churn rates. The postgraduate education level has the second-highest churn rate. Thus, as the education level increases, the chances of churring also increase.

 We can also notice the churn rate is minimal for churn rates based on the education level of customers, thus indicating that there is not a strong correlation between education level and churn rates.

 ### Analysis for correlation between marital status and churn rates:

During our EDA, we had already discovered that the majority or 85%, of the customers in the dataset either belong to the married or single marital status. Therefore, taking churn rates based on this would not provide accurate patterns or trends. So, to overcome this challenge, the below graph showcases the churn rate for marital status based on the ratio of each marital status. By doing, this, we get a more accurate graph.


<img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/13.png />

 From the graph above, it can be observed that based on the ratio of each marital status, the married marital status has the highest churn rate ratio, with the single marital status being the second highest. The churn rates for marital status are significant, meaning there is a strong correlation between marital status and churn rates.

 Moreover, it is not ideal for performing a regression analysis for this correlation. The churn rate is the dependent variable, and marital status is the independent variable. Therefore, the direct application of linear regression analysis to the variable of married status is not appropriate because it is a categorical variable with numerous categories.

 ### Analysis for correlation between income category and churn rates:

 Our EDA shows that most customers are in the less than $ 40k income category. Therefore, taking churn rates based on this would not provide accurate patterns or trends. So, to overcome a similar challenge, the graph below showcases the churn rate for the income category based on the ratio of the income category. By doing, this, we get a more accurate graph.

 <img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/14.png />

  The graph above shows that the ratio churn rates are the highest for customers in the less than 40k category. Therefore, the churn rate is the highest for customers in the less than $ 40k income category.

 Thus, it is safe to conclude customers with a low income are more likely to churn. Also, the churn rates for the income category are significant. Therefore there is a strong correlation between the income category and churn rates.


 ### Analysis for correlation between card category and churn rates:

 From our EDA, we already know that most of the customers are in the blue card category, with 98% being in this category. Therefore, taking churn rates based on this would not provide accurate patterns or trends. So, to overcome a similar challenge, the graph below showcases the churn rate for card category based on the ratio of each card category. By doing, this, we get a more accurate graph.
 
 <img src=https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/images%20/15.png />

 Moreover, we can also see a significant relationship between card category and churn rates. Thus, both of them have a strong correlation.

 [If you would like more of my analysis , please click here.](https://github.com/ubco-W2022T2-data301/-project-group-group20A/blob/main/analysis/analysis(Ajneya).ipynb)


## Conclusion for Research Question:

The following conclusions can be drawn based on the dataset analysis and the research question of how demographics such as age and income affect credit card churn rates:

Firstly, the dataset analysis revealed that churn rates increase with customer age, indicating that older customers are more likely to churn. This could result from several factors, including shifting spending patterns, unstable finances, or a desire to consider different options. The retention of senior consumers should be a top priority for credit card businesses, and this may be done by offering them incentives and prizes to do so. For instance, they provide exclusive benefits and discounts to loyal clients, tailored financial advice, or superior customer support. Companies might also utilise data analytics to identify the reasons behind customer churn and address them proactively.

Secondly, Churn rates differ significantly by marital status, with married and single customers having the highest and Divorced customers having the lowest. This implies that to meet their particular wants and concerns more effectively, credit card firms should consider adjusting their marketing and retention methods to individual and marital status. For instance, they may provide single consumers with tailored budgeting tools or married couples with joint credit cards with attractive benefits. Additionally, banks might do surveys or focus groups to learn more about the elements that affect customer happiness and retention in each marital status category.

Furthermore, churn rates differ slightly by gender, as females have a slightly higher churn rate than male customers. Even though the difference is almost insignificant, credit card companies should still be aware of gender differences in financial behaviour and design their products and services accordingly. For instance, they may provide credit cards with features that appeal more to women, like rewards for shopping or vacation, or they could provide financial education and services that address issues that affect many female consumers, such as student loan debt or retirement planning.

Moreover, the dataset analysis showed that churn rates differ significantly by income categories, with customers earning less than 40k per year having the highest churn rates and those earning $120k+ having the lowest. This emphasises how crucial it is to customise marketing and retention plans for particular income brackets to better address their specific wants and concerns. For instance, credit card firms might provide low-income consumers with more flexible payment alternatives, such as reduced interest rates or longer repayment terms. For wealthy clients, they might give exclusive benefits or concierge services that fit their opulent way of life.

The dataset analysis revealed that churn rates differ significantly by education level, with the Doctorate education level having the highest churn rates. This proposes that credit card companies investigate the causes of this trend and develop plans to alleviate the worries of well-educated consumers. For instance, they can provide credit cards with rewards for continuing education or professional development or collaborate with educational organisations to provide cardholders with special perks. Additionally, they may carry out research to comprehend the financial priorities and aims of highly educated clients so that they can build goods and services that suit their requirements.

Finally, the dataset analysis showed that churn rates differ significantly by card categories, with blue card category customers having the highest and Platinum card category customers having the lowest churn rates. This implies that to serve each card category's specific wants and concerns more effectively, credit card providers should customise their marketing and retention efforts. They may, for instance, provide premium cardholders with more individualised customer support or create marketing campaigns highlighting the particular advantages and features of each card category. Additionally, they could use data analytics to identify factors contributing to customer loyalty in each card category and design retention strategies accordingly.

In conclusion, to answer my research question of how demographics affect credit card churn rates? All demographic variables present in this data(customer age, marital status, gender, income category, education level, card category) correlate either with the increase or decrease of churn risk. While some demographics, such as age, card category, income category and marital status, have a strong positive correlation with the increase in churn rates. Demographics such as gender and education level have a weak positive correlation with increased churn rates.
