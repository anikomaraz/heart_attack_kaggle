This project was done for the [Heart Attack Risk Analysis](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview) challenge on Kaggle and the predictions were submitted to a live (active) competition. I prepared 2 versions: 
1. My [first attempt](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/heart_attack.ipynb) preprocessed the data, fitted an XGBoost and a SVM models in addition to the baseline, fine-tuned the XGBoost model hyperparameters and optimised feature selection. The accuracy got me to place 56 of the competition 
2. In the [second round](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/heart_attack_v2.ipynb) I used pipelines to preprocess the data, trimmed the features and tested the Logistic Regression, XGBoost, SVM and Decision Trees as competing models in the same pipeline. This approach (and the preceeding preprocessing) indicated that SVM fit the data the best, so I used this model to make predictions to the test data on Kaggle. This approach got me to place 46 (although places 9-46 have the same accuracy). 

Feedback is very welcome!


