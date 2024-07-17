import streamlit as st
from PIL import Image


st.set_page_config(page_title="Technical Summary", page_icon="📈")

st.sidebar.header("Technical Summary")

st.markdown(
    """
    <h2 style="color:#228B22;">Foreword</h2>

    <p>This project was inspired by a <a href="https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview">Kaggle Competition</a>. The task was to predict heart attack risk (low/high) given 25 features of lifestyle and biometrics. Like at most Kaggle competitions, my model was evaluated for <b>accuracy</b>: how well it predicts high vs. low risk of heart attack, and true vs. false cases (<a href="https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3_clean_KaggleV1.ipynb">preprocessing and Kaggle-optimized solution</a>). However, while accuracy is a good "general" metric, I argue that in this case <b>precision</b> is a better metric for model performance given the high cost of missing true positive (high risk) cases (see my <i>Sensible approach</i> <a href="https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v5_probability_xgboost_KaggleV2.ipynb">notebook</a>). Therefore, I created my version to improve detection in production. After preprocessing and several training rounds, I settled for an XGBoost model with <b>probability estimation</b>, resulting in correctly detecting truly high-risk cases 43% of the time.</p>

    <h3 style="color:#228B22;">Task and Data</h3>

    <p>The task was to train a model for predicting a binary target based on 25 features and 7010 cases. My submission was evaluated for accuracy on Kaggle given a set of test features (N=1753). There is no information about the source of data, but given that there are no missing values and that datapoints are uniformly distributed on most variables, I assume this is an artificial or upcycled database. Means and distributions appear to be representative of the general population.</p>

    <h3 style="color:#228B22;">Preprocessing</h3>

    <p>Continuous features are typically close to a uniform distribution, and none of the categories are extremely underrepresented. There are no outliers or missing data. Mean values and distributions appear to reflect that of the normal population. I created the following <i>new features</i>: 
    <ul>
        <li>blood pressure was split into Systolic and Diastolic values and their proportion calculated,</li>
        <li>cholesterol was split into low and high based on sample mean.</li>
    </ul>
    Given the lack of outliers and near-uniform distribution of data, I opted for the <b>Min Max Scaler</b> for the continuous variables to prepare them for gradient-based optimization algorithms and the <b>One Hot Encoder</b> for categorical features. There was no <i>multicollinearity</i> among features (all VIF < 4).</p>

    <h3 style="color:#228B22;">Kaggle model performance</h3>

    <p>In order to obtain the highest accuracy, I tested 7 models in the pipeline:</p>

    ![Models Accuracy](../plots/models_accuracy.png)

    <p>SVM and the Neural Network had the same accuracy, but <b style="color:#228B22;">SVM</b> being a simpler model, I picked this for further processing. By fine-tuning with GridSearchCV, accuracy did not improve much (<b>0.6429</b>). The model was then trained on the entire train dataset, and predictions for the test data were made.</p>

    <h3 style="color:#228B22;">All things strange</h3>

    <p>My best SVM-based model did not predict any positive case on the N=1753 unseen test data. Neither did any other model with similar accuracy. Given that there were 35% positive cases in the 7010 train data, 0% appears to be strange behavior. I <a href="https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/train_test_diff_plots.ipynb">compared the train vs. test features</a>, but they did not seem to be very different from each other to account for a lack of positive cases. Submitting all zeros got me to place 46 on the competition, but places 5+ have the same or worse accuracy than an all-zero submission.</p>

    <h3 style="color:#228B22;">Sensible Approach</h3>

    <p>It was not only the lack of positive cases but also the fact that risk prediction should be optimized for detecting positive cases that has led me to the decision of opting for <b>precision</b> as a measure of goodness of fit. Optimizing for precision will allow a more sensitive flagging of potentially high-risk cases in production. Missing a positive case (high risk for heart attack) would potentially be fatal, thus "expensive", whereas flagging a low-risk case results "only" in higher costs due to unnecessary secondary screening, thus it is "cheap". Consequently, the model should identify the true positive cases but avoid false positives as much as possible (so we disregard the identification of negative cases).</p>

    <p>Mathematically speaking, precision is:</p>

    <p style="margin-left: 30px;">
        $$ \text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}} $$
    </p>

    <p>Thus, the detection of negative cases will be ignored in this metric.</p>

    <p><b>Precision</b> scores for the models trained for the Kaggle competition in decreasing order were: <b>XGBoost: 0.388</b>, Decision Tree: 0.37, Gradient Boosting: 0.3609, Random Forest: 0.3553, SVM: 0.3454, Logistic Regression: 0.3376, Neural Network: 0.1778. Therefore, XGBoost was selected for further evaluation, because this model had the highest precision at baseline.</p>

    <p>Additionally, in order to further increase sensitivity of detection, I used <b>probability estimation</b> instead of the binary approach. This approach predicts the <i>probability</i> of a case belonging to a certain label given the XGBoost model, not the actual state. After training, the best threshold was identified as 0.8505. This approach resulted in an improvement of <b>precision to 0.4286</b> and a similar <b>accuracy of 0.6400</b>.</p>

    <img src="../plots/model_xgb_proba_metrics.png" alt="model metrics" style="width: 50%;">

    <h2 style="color:#228B22;">The Product</h2>

    <p>The model implemented in production demonstrates a high sensitivity in identifying positive cases, correctly flagging 43% of instances as high risk of heart attack. However, it also shows a notable bias towards positivity, resulting in 57% of cases being incorrectly classified as high risk. This approach has led to 27 cases being flagged as high risk that would have been missed by the baseline accuracy-optimized model.</p>

    <p>Despite its efficacy in sensitivity, this bias towards positivity has impacted its performance on unseen Kaggle test data due to lower recall, resulting in a slightly lower accuracy of 0.63262 compared to 0.63776 achieved by the accuracy-optimized baseline model.</p>

    <p>To gain insights into the model's decision-making process, here is the Feature Importance matrix highlighting the key factors influencing predictions:</p>

    <img src="../plots/model_xgb_feature_importance.png" alt="feature importance" style="width: 50%;">
    
    """,
    unsafe_allow_html=True
)
