# Heart Attack Risk Analysis Project

This project was done for the [Heart Attack Risk Analysis](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview) challenge on Kaggle, and the predictions were submitted to a live (active) competition.


## Access the App

<div align="center">

### [https://fake-heart-attack.streamlit.app/](https://fake-heart-attack.streamlit.app/)

</div>

## Project Steps

1. **First Version**
   - Explored the data
   - Preprocessing: created new columns, encoded, normalised and balanced the dataset
   - Created visualisations to explore relationships in the dataset
   - Created feature selection
   - Fitted a baseline model (logistic regression), XGBoost, SVM model 
   - Optimised feature selection
   - Hyper-tuned hyperparameters for XGBoost and SVM
   - Picked a final model: **XGBoost** with an **accuracy of 0.62** on Kaggle unseen test data
   - Visualised model performance and feature importance
   - Result: Placed 56th in the competition.

2. **Version 2**
   - I transferred everything to the **pipeline** to preprocess data & train the model
   - Trimmed the features.
   - Tested Logistic Regression, XGBoost, SVM, and Decision Trees as competing models in the same pipeline.
   - Result: **SVM** fit the data the best, 
   - Used this model to make predictions on Kaggle, obtained an accuracy of **0.63776** placing 46th (although places 9-46 had the same accuracy).

3. **[Version 3](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3_clean_KaggleV1.ipynb)**
   - I trained 6 different models in the pipeline (LogRegression, XGBoost, SVM, Decision Tree, Random Forest, Gradient Boosting and Neural Network)
   - Fine-tuned the XGBoost and SVM models
   - Result: the **fine-tuned XGBoost** did not improve upon the V2 model (accuracy of **0.63776**)
   - This notebook version is clean, and was also uploaded onto Kaggle

4. **Version 4**
   - For interpretability and computational efficiency, I picked the SVM model (with optimised parameters).
   - This version contains a clean notebook (no visualisations) before package creation / deployment

5. **Deployment**
   - The notebook was turned into a package and deployed
   - The backend runs on the **Google Cloud Platform**, while **Streamlit** hosts the frontend.
   - The frontend is able to **receive user-input data** (although defaults are offered), which is then sent to the backend
   - The backend runs the model, makes the prediction
   - Frontend receives prediction data and displays it
   
6. **Model Improvement**
   - I noticed that although 35% of the train dataset is a positive case, most of my models predict only negative cases for the N=1700 test data
   - Therefore I revisited the **XGBoost model** to optimise for **precision** instead of accuracy which is a better metric to capture true positive cases
   - Given the low number of positive cases on the test set I decided to employ **probability estimation** and find an optimal **treshold** to classify positive cases.
   - This resulted in 339 positive cases on the Kaggle test dataset, thus the model is more sensitive to pick up high risk
   - accuracy is now 0.59, but precision improved to 0.35
   - details are in [Version 5](https://nbviewer.org/github/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v5_probability_xgboost_KaggleV2.ipynb) of the notebook

7. **Redeployment**
   - I redeployed the app with the new model 
   - adjusted the defaults to get high risk


## Results

- I am currently 46th on the Kaggle competition 
- The model (optimised for precision) runs in production and correctly fake-predicts the risk of heart attack (as expected by the test cases)



Happy faking! 😃
