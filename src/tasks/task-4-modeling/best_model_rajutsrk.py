'''
Final_df_regression.csv - The target column for this dataset is the CAQI_idx column. There is no CAQI_level column.
Final_df_classification.csv - The target column for this dataset is the CAQI_level column. There is no CAQI_idx column.
data of 2021 used to test

'''
import fastparquet
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier



df = pd.read_parquet('train_temporal_classification.parquet.gz')
print(df.columns.to_list())
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
powiat = pd.get_dummies(df_textdata['powiat'])
season = pd.get_dummies(df_textdata['season'])

# Concatenate the encoded columns with the original dataframe
df_textdata = pd.concat([df_textdata, powiat], axis=1)
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
powiat = pd.get_dummies(df_test_textdata['powiat'])
season = pd.get_dummies(df_test_textdata['season'])

# Concatenate the encoded columns with the original dataframe
df_test_textdata = pd.concat([df_test_textdata, powiat], axis=1)
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

model_params = {
    'svm': {
        'model': svm.SVC(gamma='auto'),
        'params': {
            'C': [1, 10, 20],
            'kernel': ['rbf', 'linear']
        }
    },
    'random_forest': {
        'model': RandomForestClassifier(),
        'params': {
            'n_estimators': [1, 5, 10]
        }
    },
    'logistic_regression': {
        'model': LogisticRegression(solver='liblinear', multi_class='auto'),
        'params': {
            'C': [1, 5, 10]
        }
    },
    'naive_bayes_gaussian': {
        'model': GaussianNB(),
        'params': {}
    },
    'naive_bayes_multinomial': {
        'model': MultinomialNB(),
        'params': {}
    },
    'decision_tree': {
        'model': DecisionTreeClassifier(),
        'params': {
            'criterion': ['gini', 'entropy'],

        }
    }
}

scores = []

for model_name, mp in model_params.items():
    clf = GridSearchCV(mp['model'], mp['params'], cv=5, return_train_score=False)
    clf.fit(x_train, y_train)
    scores.append({
        'model': model_name,
        'best_score': clf.best_score_,
        'best_params': clf.best_params_
    })

best_model = pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])
print(best_model)
