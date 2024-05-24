# This is an active Kaggle competition for Kudos.
# Details: https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview

###### IMPORTS ######
from matplotlib import pyplot as plt
import pandas as pd
import ydata_profiling
import statistics


###### GET DATA ######
df_heart_risk_train = pd.read_csv('data/train.csv')
df_heart_risk_test = pd.read_csv('data/test.csv')

###### EXPLORE DATA ######
# df_heart_risk_train.profile_report()
print(df_heart_risk_test.columns)
columns = ['Patient ID', 'Age', 'Sex', 'Cholesterol', 'Blood Pressure',
       'Heart Rate', 'Diabetes', 'Family History', 'Smoking', 'Obesity',
       'Alcohol Consumption', 'Exercise Hours Per Week', 'Diet',
       'Previous Heart Problems', 'Medication Use', 'Stress Level',
       'Sedentary Hours Per Day', 'Income', 'BMI', 'Triglycerides',
       'Physical Activity Days Per Week', 'Sleep Hours Per Day', 'Country',
       'Continent', 'Hemisphere']
print(df_heart_risk_train[['Diabetes']].describe()['mean'])
columns_mean = df_heart_risk_train['Age', 'Cholesterol']

mean(df_heart_risk_train['Age'])

# for column in columns_mean:
#        mean = statistics.mean(columns_mean[[column]])
#        std = statistics.stdev(columns_mean[[column]])
#        f"For {column} the mean is {mean} and the std is {std}."


# print(df_heart_risk_test.describe())
# train data contains 7010 entries and 26 columns (25+1)
# there is no missing data!
# mean age is 54 years, 18-90 years, 70% men. The sample has high cholesterol levels (mean = 260, above 240 is considered high).
# Heart rate is around 75 (normal: 60-100).


# .shape, .columns, .dtypes
# .info(), .describe(), nunique(), .isna().sum()


# import ydata_profiling
# mpg.profile_report()


###### IMPUTE ######


###### MODELING ######
#pip install -U scikit-learn
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import cross_validate

# Ready X and y
# X = livecode_data[['GrLivArea']]
# y = livecode_data['SalePrice']
#
# # Split into Train/Test
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
#
#
#
# # Instantiate model
# model = LinearRegression()
#
# # 5-Fold Cross validate model
# cv_results = cross_validate(model, X, y, cv=5)
# # Rule of thumb:  K = 5   or 10
# # Scores
# print(cv_results['test_score'])
# # Mean of scores
# cv_results['test_score'].mean()
#
# # check model learning curves
# import numpy as np
# from sklearn.model_selection import learning_curve
#
# train_sizes = [25,50,75,100,250,500,750,1000,1150]
#
# # Get train scores (R2), train sizes, and validation scores using `learning_curve`
# train_sizes, train_scores, test_scores = learning_curve(
#     estimator=LinearRegression(), X=X, y=y, train_sizes=train_sizes, cv=5)
#
# # Take the mean of cross-validated train scores and validation scores
# train_scores_mean = np.mean(train_scores, axis=1)
# test_scores_mean = np.mean(test_scores, axis=1)
#
# # plt.plot(train_sizes, train_scores_mean, label = 'Training score')
# # plt.plot(train_sizes, test_scores_mean, label = 'Test score')
# # plt.ylabel('r2 score', fontsize = 14)
# # plt.xlabel('Training set size', fontsize = 14)
# # plt.title('Learning curves', fontsize = 18, y = 1.03)
# # plt.legend()
