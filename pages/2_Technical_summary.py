import streamlit as st
from PIL import Image


st.set_page_config(page_title="Technical Summary", page_icon="📈")

st.sidebar.header("Technical Summary")

import streamlit as st

st.markdown("""
### :green[Foreword]

This project was inspired by a [Kaggle Competition](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview). 
The task was to predict heart attack risk (low/high) given 25 features of lifestyle and biometrics. 
Like at most Kaggle competitions, my model was evaluated for :blue-background[accuracy]: how well it predicts high vs. low risk of heart attack, and true vs. false cases ([preprocessing and Kaggle-optimized solution](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3_clean_KaggleV1.ipynb)). However, while accuracy is a good "general" metric, I argue that in this case :blue-background[precision] is a better metric for model performance given the high cost of missing true positive (high risk) cases (see my [Sensible approach](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v5_probability_xgboost_KaggleV2.ipynb). Therefore, I created my version to improve detection in production. After preprocessing and several training rounds, I settled for an XGBoost model with :blue-background[probability estimation], resulting in correctly detecting truly high-risk cases 43% of the time.

### :green[Task and Data]

The task was to train a model for predicting a binary target based on 25 features and 7010 cases. 
My submission was evaluated for accuracy on Kaggle given a set of test features (N=1753). There is no information about the source of data, but given that there are no missing values and that datapoints are uniformly distributed on most variables, I assume this is an artificial or upcycled database. Means and distributions appear to be representative of the general population.

### Preprocessing

Continuous features are typically close to a uniform distribution, and none of the categories are extremely underrepresented. There are no outliers or missing data. Mean values and distributions appear to reflect that of the normal population. I created the following <i>new features</i>: 
- blood pressure was split into Systolic and Diastolic values and their proportion calculated,
- cholesterol was split into low and high based on sample mean.

Given the lack of outliers and near-uniform distribution of data, I opted for the **Min Max Scaler** for the continuous variables to prepare them for gradient-based optimization algorithms and the **One Hot Encoder** for categorical features. There was no <i>multicollinearity</i> among features (all VIF < 4).

### Kaggle model performance

In order to obtain the highest accuracy, I tested 7 models in the pipeline:
![Models Accuracy](../plots/models_accuracy.png)

SVM and the Neural Network had the same accuracy, but **SVM** being a simpler model, I picked this for further processing. By fine-tuning with GridSearchCV, accuracy did not improve much (**0.6429**). The model was then trained on the entire train dataset, and predictions for the test data were made.

### All things strange

My best SVM-based model did not predict any positive case on the N=1753 unseen test data. Neither did any other model with similar accuracy. Given that there were 35% positive cases in the 7010 train data, 0% appears to be strange behavior. I [compared the train vs. test features](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/train_test_diff_plots.ipynb), but they did not seem to be very different from each other to account for a lack of positive cases. Submitting all zeros got me to place 46 on the competition, but places 5+ have the same or worse accuracy than an all-zero submission.

### Sensible Approach

It was not only the lack of positive cases but also the fact that risk prediction should be optimized for detecting positive cases that has led me to the decision of opting for **precision** as a measure of goodness of fit. Optimizing for precision will allow a more sensitive flagging of potentially high-risk cases in production. Missing a positive case (high risk for heart attack) would potentially be fatal, thus "expensive", whereas flagging a low-risk case results "only" in higher costs due to unnecessary secondary screening, thus it is "cheap". Consequently, the model should identify the true positive cases but avoid false positives as much as possible (so we disregard the identification of negative cases).

Mathematically speaking, precision is:

$$ \text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}} $$

Thus, the detection of negative cases will be ignored in this metric.

**Precision** scores for the models trained for the Kaggle competition in decreasing order were: **XGBoost: 0.388**, Decision Tree: 0.37, Gradient Boosting: 0.3609, Random Forest: 0.3553, SVM: 0.3454, Logistic Regression: 0.3376, Neural Network: 0.1778. Therefore, XGBoost was selected for further evaluation, because this model had the highest precision at baseline.

Additionally, in order to further increase sensitivity of detection, I used **probability estimation** instead of the binary approach. This approach predicts the <i>probability</i> of a case belonging to a certain label given the XGBoost model, not the actual state. After training, the best threshold was identified as 0.8505. This approach resulted in an improvement of **precision to 0.4286** and a similar **accuracy of 0.6400**.
![Model Metrics](../plots/model_xgb_proba_metrics.png)

### The Product

The model implemented in production demonstrates a high sensitivity in identifying positive cases, correctly flagging 43% of instances as high risk of heart attack. However, it also shows a notable bias towards positivity, resulting in 57% of cases being incorrectly classified as high risk. This approach has led to 27 cases being flagged as high risk that would have been missed by the baseline accuracy-optimized model.

Despite its efficacy in sensitivity, this bias towards positivity has impacted its performance on unseen Kaggle test data due to lower recall, resulting in a slightly lower accuracy of 0.63262 compared to 0.63776 achieved by the accuracy-optimized baseline model.

To gain insights into the model's decision-making process, here is the Feature Importance matrix highlighting the key factors influencing predictions:
![Feature Importance](../plots/model_xgb_feature_importance.png)
""",
    unsafe_allow_html=True
)
