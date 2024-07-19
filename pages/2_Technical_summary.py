import streamlit as st
from PIL import Image

st.set_page_config(page_title="Technical Summary", page_icon="📈")

st.sidebar.header("📈 Technical Summary")

st.markdown("""
### :green[Foreword]

This project was inspired by a [Kaggle Competition](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview). 
The task was to predict heart attack risk (low/high) given 25 features of lifestyle and biometrics. 
Like most Kaggle competitions, my model was evaluated based on :blue-background[accuracy]: how well it predicts high vs. low risk of heart attack, and true vs. false cases ([Version 1: preprocessing and Kaggle-optimized solution](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3_clean_KaggleV1.ipynb)). 
However, while accuracy is a good general metric, I argue that in this case :blue-background[**precision**] is a better metric for model performance given the high cost of missing true positive (high risk) cases (see [Version 2, the precision-focused approach](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v5_probability_xgboost_KaggleV2.ipynb)). Therefore, I created my version to improve detection in production. 
After preprocessing and several training rounds, I settled on an _**:blue-background[XGBoost] model with :blue-background[probability estimation], resulting in correctly detecting high-risk cases :blue-background[43%] of the time.**_

### :green[Task and Data]

The task was to train a model to predict a binary target based on 25 features from 7010 cases. My submission was evaluated for accuracy on Kaggle using a test set of 1753 cases. 
There is no information about the data source, but given the lack of missing values and uniform distribution across most variables, I assume this is an artificial or upcycled database. The means and distributions appear to be representative of the general population.

### :green[Preprocessing]

Continuous features are typically close to a uniform distribution, and none of the categories are extremely underrepresented. 
There are no outliers or missing data. Mean values and distributions reflect those of the general population. I created the following :blue-background[new features]: 
- Blood pressure was split into Systolic and Diastolic values, and their proportion calculated.
- Cholesterol was split into low and high based on the sample mean.

Given the lack of outliers and near-uniform distribution of data, I opted for the :blue-background[Min Max Scaler] for continuous variables to prepare them for gradient-based optimization algorithms and the :blue-background[One Hot Encoder] for categorical features. There was :blue-background[no multicollinearity] among features (all VIF < 4).

### :green[**Version 1:** Kaggle Model Performance]

To achieve the highest accuracy, I tested seven models in the pipeline:
""", unsafe_allow_html=True)


models_accuracy = Image.open('plots/models_accuracy.png')
st.image(models_accuracy)


st.markdown("""
SVM and the Neural Network had the same accuracy, but :blue-background[SVM], being a simpler model, was chosen for further processing. 
By :blue-background[fine-tuning with GridSearchCV], the accuracy did not improve much (0.6429). The model was then trained on the entire training dataset, and predictions for the test data were made.

### :green[Unexpected Results]

_My best SVM-based model did not predict any positive cases in the 1753 unseen test data._ 
Neither did any other model with similar accuracy. Given that there were 35% positive cases in the 7010 training data, 0% positive cases in the test data seemed unusual. 
Submitting all zeros :blue-background[placed me 46th in the competition], but positions 5 and above had the same or worse accuracy than an all-zero submission.
I [compared the train vs. test features](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/train_test_diff_plots.ipynb), but they did not appear significantly different to account for the lack of positive cases. 
Additionally, even though the competition was scored on accuracy, I questioned whether this metric is the best measure for this model's performance. 
Therefore I decided to follow my own approach. 

### :green[**Version 2:** Precision-based Approach]

Accuracy is a good "general" metric for model classification performance because it reflects the model's ability to correctly label both true and false cases. 
However, in this particular case, missing a high-risk (positive) case of heart attack could be fatal. 
To mitigate this risk and ensure high-risk cases are captured as diligently as possible, I prioritized :blue-background[**precision** as a measure of goodness of fit].
Optimizing for precision allows for more sensitive detection of high-risk cases in production, potentially saving lives.


Mathematically:
<br> <br>

$$\\text{Precision} = \\frac{\\text{True Positives}}{\\text{True Positives} + \\text{False Positives}} $$
<br> <br>

:blue-background[Precision scores] for the models trained for the Kaggle competition in decreasing order were: :blue-background[XGBoost: 0.388], Decision Tree: 0.37, Gradient Boosting: 0.3609, Random Forest: 0.3553, SVM: 0.3454, Logistic Regression: 0.3376, Neural Network: 0.1778. 
Therefore, XGBoost was selected for further evaluation, as this model had the highest precision at baseline.

Additionally, to account for the all-zero predictions on the test set, I decided to further increase the model's sensitivity. 
Thus, I opted for using :blue-background[probability estimation] instead of a binary approach. 
This approach predicts the *probability* of a case belonging to a certain label using the XGBoost model, not the actual state, making it a more sensitive and flexible approach. 
After training, the best threshold was identified as 0.8505. This approach :blue-background[improved precision to **0.4286**] and resulted in a :blue-background[similar accuracy of 0.6400].

The model metrics as a function of threshold (including the optimal threshold) are as follows:
""", unsafe_allow_html=True)


xgboost_metrics = Image.open('plots/model_xgb_proba_metrics.png')
st.image(xgboost_metrics)


st.markdown("""
### :green[The Product]

The model implemented in production demonstrates high sensitivity in identifying positive cases, correctly flagging 43% of instances as high risk of heart attack. 
However, it also shows a notable bias towards positivity, resulting in 57% of cases being incorrectly classified as high risk. 
*This approach has led to 27 cases being flagged as high risk that would have been missed by the baseline accuracy-optimized (Version 1) model.*

Despite its efficacy in sensitivity, this bias towards positivity has impacted its performance on unseen Kaggle test data due to lower recall, resulting in a slightly lower accuracy of 0.63262 compared to the 0.63776 achieved by the accuracy-optimized baseline model.

To gain insights into the model's decision-making process, here is the :blue-background[Feature Importance plot], highlighting the key factors influencing predictions. 
Keep in mind that this plot represents the relative importance of features in making predictions but does not indicate whether the correlation is positive or negative.


""", unsafe_allow_html=True)


feature_importance = Image.open('plots/model_xgb_feature_importance.png')
st.image(feature_importance)

st.markdown("""
It appears that based on this (fake-data-)model that there might be significant differences in heart attack risk based on :blue-background[geographic location]. 
This could be due to various factors like climate, lifestyle, healthcare access, or even genetic predispositions prevalent in different hemispheres.
However, :blue-background[diet] also plays a role in heart attack risk: unhealthy diet is strongly associated with increased heart attack risk. This aligns with medical research that poor dietary habits contribute significantly to heart disease.

""")

st.markdown("""
    <br> <br>
    Further details: [GitHub Repository](https://github.com/anikomaraz/heart_attack_kaggle)
    """, unsafe_allow_html=True)
