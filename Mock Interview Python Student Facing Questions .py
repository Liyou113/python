#!/usr/bin/env python
# coding: utf-8

# <h3> Mock Interview Python Screening test </h3>
# 

# In[1]:


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
dataframe = pd.read_csv("adult_census_data.csv")


# In[2]:


#Reading the censua Dataset
dataframe


# In[3]:


dataframe.shape


# In[4]:


# Checking if my dataset is consistent with the same data type in every column
dataframe.info()


# In[5]:


# Describing the numerical value only
dataframe.describe()


# <b> Q1. After importing the adult_census_data.csv file, please filter this to include only the following criteria: </b>
# <p>
# 
# <li> State-Gov</li>
# <li> Bachelors </li>
# <li> Never-Married </li>
# <li> Adm-Clerical </li> 
# <li> Not-in-familiy </li>
# <li> White </li>
# <li> Male </li> 
# <li> United States </li>
# <li> <=50K </li> 
# 
# <b> Feel free to any method to complete this tasks. However, we recommend you use either list filtering [], or .loc to complete this task.</b>

# <b> Put your code below </b>

# In[6]:


columns=[1,3,5,6,7,8,13,14]
census_df=dataframe.iloc[:,columns]
census_df.head()


# In[9]:


# Checking the shape of the filtered dataframe
census_df.shape


# In[10]:


# Checking the columns name 
census_df.columns


# <b> Currently, the dataframe you are using has the following column names: </b>
# 
# [' State-gov', ' Bachelors', ' Never-married',
#        ' Adm-clerical', ' Not-in-family', ' White', ' Male', ' United-States', ' <=50K']
#        
#      
# <b> Q2. Please re-name all the newly filtered columns in the pandas DataFrame to the following: </b>
# 
# Employment Type, Degree Status, Marriage-Status, Job-Role, Family-Role, Ethnicity, Gender, Country, Earnings
# 
# E.g. State-Gov becomes Employment Type, Bachelors becomes Degree Status, etc.

# <b> Put your code below </b>

# In[16]:


# Renaming columns in the new dataframe
new_names=['Employment Type','Degree Status','Job-Role', 'Family-Role', 'Ethnicity', 'Gender', 'Country', 'Earnings']


# In[17]:


census_df.columns=new_names
census_df.head()


# In[18]:


# checking census_df dataframe
census_df . info ()


# <b> Q3. The Job Role Columns holds the job information for each individual in this census snapshot. Using this column, create a Bar Chart that shows the count of 'Unique' Jobs per Job Group in the "Job-Role" Column in ascending order, as per the provided image below </b>
# 

# <b> Put your code below </b>

# In[21]:


# checking the unique values of job role
census_df['Job-Role'].nunique()


# In[22]:


# Using value_counts to get a Series containing counts of unique values
census_df['Job-Role'].value_counts()


# In[23]:


# Plotting the bar chart for unique job groups in the job role column
plt.figure(figsize=(10,5))
census_df['Job-Role'].value_counts(ascending=True).plot(kind='bar')
plt.xlabel('Job Group',color='blue',fontsize=15)
plt.ylabel('Count of Unique Values',color='blue',fontsize=15)
plt.title('Unique Jobs Per Job Group in Job Role',color='blue',fontsize=20)
plt.show()


# <b> Q4. Please create two bar plots as per below that show:
#     
#     1) The number of individuals who have a High School Graduate Diploma AND earn <=50K in the United States
#     2) The number of individuals who have a High School Graduate Diploma AND earn >50K in the United States 
# 
# Please note you will be looking specifically at the *Job Role* column

# <b> Put Your Code Below </b>

# In[24]:


# Created DF1 and DF2 to help to plot the two conditions of earning
plt.figure(figsize=(10,5))
df1 = (census_df[(census_df['Degree Status']==' HS-grad')&(census_df['Earnings']==" <=50K")&(census_df['Country']==" United-States")])
df1.iloc[:,3].value_counts().plot(kind='bar')
plt.title('Individuals who have a High School Graduate Diploma AND earn <=50K in the United States')
plt.show()

plt.figure(figsize=(10,5))
df2 = (census_df[(census_df['Degree Status']==' HS-grad')&(census_df['Earnings']==" >50K")&(census_df['Country']==" United-States")])
df2.iloc[:,3].value_counts().plot(kind='bar')
plt.title('Individuals who have a High School Graduate Diploma AND earn >50K in the United States')
plt.show()


# In[ ]:





# 
# 

# <H2> Challenge Question </H2>
# 
# <b> Q5. Which Job Role has the highest <i> proportion </i> of individuals who earn >50K? </b>

# <b> Put your code below </b>

# In[ ]:




