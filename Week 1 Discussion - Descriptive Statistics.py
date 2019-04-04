#!/usr/bin/env python
# coding: utf-8

# # Week 1 Discussion - Descriptive Statistics
# ### Download the train.csv dataset and run some basic descriptive statistics and graphs for two or more variables of your choosing using Python.  Provide your Python code here, perhaps as a Jupyter notebook .html file on GitHub.  Embed at least one graph in your discussion by using the "Files" link in the upper right portion of Canvas.

# In[1]:


# Week 1 Discussion
# MSDS 422-DL-55
# Brandi Beals


# In[9]:


# Load packages
import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


# Read data
data = pd.read_csv('train.csv',sep=',')

# Show a sample of the first 10 rows of data
data.head(10)


# In[7]:


# Understand the data types of the data
data.info()


# In[8]:


# Summarize the numerical fields in the data
data.describe()


# In[48]:


# Exploratory data analysis
pd.plotting.scatter_matrix(data, diagonal='kde', color='black', alpha=0.3, figsize=(15,15))


# In[55]:


plt.figure(figsize=(10,10))
plt.hist(data['Pclass'], 3, color='black', alpha=0.3)
plt.xticks(data['Pclass'])
plt.title('Class Count')
plt.xlabel('Class')
plt.ylabel('Frequency')


# In[56]:


plt.figure(figsize=(10,10))
age = data['Age']
plt.hist(age.dropna(), 20, color='black', alpha=0.3)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')


# In[57]:


plt.figure(figsize=(10,10))
plt.scatter(data['SibSp'], data['Parch'], color='black', alpha=0.3)
plt.title('Scatterplot')
plt.xlabel('Number of Sibling/Spouse Aboard')
plt.ylabel('Number of Parent/Child Aboard')


# In[58]:


plt.figure(figsize=(10,10))
plt.boxplot(data['Fare'], vert=False)
plt.title('Boxplot of Fare')

