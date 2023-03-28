#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
import numpy as np
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from lightgbm import LGBMClassifier
warnings.filterwarnings("ignore")
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import accuracy_score
warnings.filterwarnings("ignore")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


train = pd.read_parquet("train_nontemporal_classification.parquet.gz")
test =  pd.read_parquet("test_nontemporal_classification.parquet.gz")


# In[3]:


train.head()


# In[4]:


train.info()


# In[4]:


train.shape


# In[5]:


train.isnull().sum()


# In[6]:


train['CAQI_level'].value_counts()


# In[7]:


# combine high and vhigh to a single category, as we want to see how it will affect the accuracy of model
train['CAQI_level'] = train['CAQI_level'].replace({'vhigh':'high'})


# In[8]:


train['CAQI_level'].value_counts()


# In[9]:


# The ordered of mapping
mapping = {'vlow': 0, 'low': 1, 'medium': 2, 'high': 3}
train['CAQI_level'] = train['CAQI_level'].replace(mapping)


# In[10]:


train['CAQI_level'].value_counts()


# In[11]:


train.columns.to_list()


# In[12]:


from sklearn.preprocessing import LabelEncoder
# encoding the other categorical columns
cat_cols = ['powiat_voivod', 'voivodship', 'season','holiday_name']
for col in cat_cols:
    le = LabelEncoder()
    train['powiat_voivod_encoded'] = le.fit_transform(train['powiat_voivod'])
    train['voivodship_encoded'] =le.fit_transform(train['voivodship'])
    train['season_encoded'] =le.fit_transform(train['season'])
    train['holiday_name_encoded'] =le.fit_transform(train['holiday_name'])


# # TEST DATA

# In[13]:


test.head()


# In[14]:


test.info()


# In[15]:


test.shape


# In[16]:


test['CAQI_level'].value_counts()


# In[17]:


# combine high and vhigh to a single category, as we want to see how it will affect the accuracy of model
test['CAQI_level'] = test['CAQI_level'].replace({'vhigh':'high'})


# In[18]:


test['CAQI_level'].value_counts()


# In[20]:


# order of mapping
mapping = {'vlow':0,'low':1,"medium":2,"high":3}
test['CAQI_level'] = test['CAQI_level'].replace(mapping)


# In[21]:


test['CAQI_level'].value_counts()


# In[22]:


# encoding the other categorical columns
from sklearn.preprocessing import LabelEncoder
cat_cols = ['powiat_voivod', 'voivodship', 'season','holiday_name']
for col in cat_cols:
    le = LabelEncoder()
    test['powiat_voivod_encoded'] = le.fit_transform(test['powiat_voivod'])
    test['voivodship_encoded'] = le.fit_transform(test['voivodship'])
    test['season_encoded'] = le.fit_transform(test['season'])
    test['holiday_name_encoded'] = le.fit_transform(test['holiday_name'])


# In[23]:


# imputing train_test_split
X_train = train.drop(['CAQI_level','powiat_voivod', 'voivodship', 'season', 'holiday_name'], axis=1)
y_train = train['CAQI_level']
X_test = test.drop(['CAQI_level','powiat_voivod', 'voivodship', 'season', 'holiday_name'], axis=1)
y_test = test['CAQI_level']


# In[24]:


#import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier


# In[25]:


clf = RandomForestClassifier(max_depth=2, random_state=42)
clf.fit(X_train, y_train)


# In[26]:


# Predict on the test set
y_pred = clf.predict(X_test)

# Accuracy score:
model_accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", model_accuracy)


# In[27]:


# Evaluating the model performance
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


# # cross validation

# In[30]:


from sklearn.model_selection import cross_val_score, StratifiedKFold

kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


cv_scores = cross_val_score(clf, X_train, y_train, cv=kfold, scoring='accuracy')

# Cross-validation scores
print("Cross-validation scores:", cv_scores)
print("Mean CV accuracy:", cv_scores.mean())


# In[ ]:




