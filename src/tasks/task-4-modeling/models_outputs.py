import fastparquet
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier



df = pd.read_parquet('train_temporal_classification.parquet.gz')
# print(df.columns.to_list())
'''
columns that have text data -> methods used to convert to numericals
powiat              ->One-Hot Encoding
voivodship         -> LabelEncoder
holiday_name       -> LabelEncoder
season             -> One-Hot Encoding
CAQI_level(target_value) -> label encoding
'''
df_textdata = pd.DataFrame(data=df[['holiday_name','season','CAQI_level']],columns=['holiday_name','season','CAQI_level'])
df_textdata[['powiat','voivodship']] = df['powiat_voivod'].str.split(',', expand=True)
# print(df_textdata.head())

# Apply Label Encoding to the voivodship name column
le = LabelEncoder()
df_textdata['voivodship_le'] = le.fit_transform(df_textdata['voivodship'])
df_textdata['CAQI_level_le'] = le.fit_transform(df_textdata['CAQI_level'])

# Apply One-Hot Encoding to the powiat,season name column
# powiat = pd.get_dummies(df_textdata['powiat'])
season = pd.get_dummies(df_textdata['season'])

# Concatenate the encoded columns with the original dataframe
# df_textdata = pd.concat([df_textdata, powiat], axis=1)
df_textdata = pd.concat([df_textdata, season], axis=1)

# Remove the original non-encoded columns
# df_textdata.drop(['voivodship', 'powiat'], axis=1, inplace=True)

df_textdata.drop(['holiday_name','season','CAQI_level','powiat','voivodship'],axis='columns',inplace=True)
df.drop(['powiat_voivod','voivodship','CAQI_level','season','holiday_name'],axis='columns',inplace=True)
df_final = pd.concat([df, df_textdata], axis=1)

##
df_test = pd.read_parquet('train_temporal_classification.parquet.gz')

'''
columns that have text data -> methods used to convert to numericals
powiat              ->One-Hot Encoding
voivodship         -> LabelEncoder
holiday_name       -> LabelEncoder
season             -> One-Hot Encoding
CAQI_level(target_value) -> label encoding
'''
df_test_textdata = pd.DataFrame(data=df_test[['holiday_name','season','CAQI_level']],columns=['holiday_name','season','CAQI_level'])
df_test_textdata[['powiat','voivodship']] = df_test['powiat_voivod'].str.split(',', expand=True)
# print(df_test_textdata.head())

# Apply Label Encoding to the voivodship name column
le = LabelEncoder()
df_test_textdata['voivodship_le'] = le.fit_transform(df_test_textdata['voivodship'])
df_test_textdata['CAQI_level_le'] = le.fit_transform(df_test_textdata['CAQI_level'])

# Apply One-Hot Encoding to the powiat,season name column
# powiat = pd.get_dummies(df_test_textdata['powiat'])
season = pd.get_dummies(df_test_textdata['season'])

# Concatenate the encoded columns with the original dataframe
# df_test_textdata = pd.concat([df_test_textdata, powiat], axis=1)
df_test_textdata = pd.concat([df_test_textdata, season], axis=1)

# Remove the original non-encoded columns
# df_test_textdata.drop(['voivodship', 'powiat'], axis=1, inplace=True)

df_test_textdata.drop(['holiday_name','season','CAQI_level','powiat','voivodship'],axis='columns',inplace=True)
df_test.drop(['powiat_voivod','voivodship','CAQI_level','season','holiday_name'],axis='columns',inplace=True)
df_test_final = pd.concat([df_test, df_test_textdata], axis=1)

x_train = df_final.drop('CAQI_level_le',axis='columns')
y_train = df_final['CAQI_level_le']
x_test = df_test_final.drop('CAQI_level_le',axis='columns')
y_test = df_test_final['CAQI_level_le']

#models and their corresponding results are given below

# model= SVC()
'''Taking lot of time'''
# model = MultinomialNB()
'''Taking lot of time'''

# model = RandomForestClassifier()
'''Score 
 0.9999966772993089
Mean squared error: 0.00
R-squared score: 1.00'''

model = DecisionTreeClassifier()
'''Score 
 1.0
Mean squared error: 0.00
R-squared score: 1.00'''
# model = GaussianNB()
'''Score 
 0.4787480063795853
Mean squared error: 3.63
R-squared score: -0.70'''

# model = LogisticRegression()
'''Score 
 0.5240497076023392
Mean squared error: 3.38
R-squared score: -0.58
'''
model.fit(x_train,y_train)
print('Score \n',model.score(x_test,y_test))
y_pred = model.predict(x_test)
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("R-squared score: %.2f" % r2_score(y_test, y_pred))