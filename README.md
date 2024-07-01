# Heart Attack Risk Analysis Project

This project was done for the [Heart Attack Risk Analysis](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview) challenge on Kaggle, and the predictions were submitted to a live (active) competition.


## Access the App

<div align="center">

### [https://fake-heart-attack.streamlit.app/](https://fake-heart-attack.streamlit.app/)

</div>

## Project Steps

1. **[First Version](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v1.ipynb)**
   - Preprocessed the data.
   - Fitted XGBoost and SVM models in addition to the baseline.
   - Fine-tuned the XGBoost model hyperparameters.
   - Optimized feature selection.
   - Result: Placed 56th in the competition.

2. **[Version 2](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v2.ipynb)**
   - Used pipelines to preprocess the data.
   - Trimmed the features.
   - Tested Logistic Regression, XGBoost, SVM, and Decision Trees as competing models in the same pipeline.
   - Result: SVM fit the data the best, used this model to make predictions on Kaggle, placing 46th (although places 9-46 had the same accuracy).

3. **[Version 3](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3.ipynb)**
   - Fine-tuned the SVM model.
   - Added and tuned a Neural Network model.
   - Result: Both solutions had the same accuracy on the Kaggle competition, which was not better than the V2 model with default parameters.

4. **[The 4th Version](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v4.ipynb)**
   - For interpretability and computational efficiency, I picked the SVM model (with optimal parameters).
   - This version contains a clean notebook (no visualisations).

5. **Deployment**
   - The notebook was turned into a package and deployed.
   - The backend runs on Google Container Run, while Streamlit hosts the frontend.
   - The frontend is able to receive user-input data (although defaults are offered), which is then sent to the backend
   - The backend runs the model, makes the prediction
   - Frontend receives prediction data and displays it
   
6. **Model Improvement**
- I noticed that although 35% of the train dataset is a positive case, most of my models predict only negative cases for the N=1700 test data
- Therefore I opted to optimise for precision which is a better metric to capture true positive cases
- This resulted in 339 positive cases on the Kaggle test dataset 
- details are in [Version 5](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v5_probability_xgboost.ipynb) of the notebook


## Results

- The final accuracy on the Kaggle test dataset is 0.63776
- In production I opted to optimise for precision (instead of accuracy) which is more appropriate given the nature of the data, but resulted in an accuracy of 0.58699 in the competition
- I am currently implementing this model into the app in production



Happy faking! 😃
