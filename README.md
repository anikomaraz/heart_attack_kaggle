# Heart Attack Risk Analysis Project

This project was done for the [Heart Attack Risk Analysis](https://www.kaggle.com/competitions/heart-attack-risk-analysis/overview) challenge on Kaggle, and the predictions were submitted to a live (active) competition.

## Project Steps

1. **[First Attempt](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v1.ipynb)**
   - Preprocessed the data.
   - Fitted XGBoost and SVM models in addition to the baseline.
   - Fine-tuned the XGBoost model hyperparameters.
   - Optimized feature selection.
   - Result: Placed 56th in the competition.

2. **[Second Round](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v2.ipynb)**
   - Used pipelines to preprocess the data.
   - Trimmed the features.
   - Tested Logistic Regression, XGBoost, SVM, and Decision Trees as competing models in the same pipeline.
   - Result: SVM fit the data the best, used this model to make predictions on Kaggle, placing 46th (although places 9-46 had the same accuracy).

3. **[Version 3](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v3.ipynb)**
   - Fine-tuned the SVM model.
   - Added and tuned a Neural Network model.
   - Result: Both solutions had the same accuracy on the Kaggle competition, which was not better than the V2 model with default parameters.

4. **[Final (4th) Version](https://github.com/anikomaraz/heart_attack_kaggle/blob/main/notebooks/heart_attack_v4.ipynb)**
   - For interpretability and computational efficiency, I picked the SVM model (with optimal parameters).
   - [Version 4](...) contains the clean notebook.

5. **Deployment**
   - The notebook was turned into a package and deployed.
   - The backend runs on Google Container Run, while Streamlit hosts the frontend.

## Results

- The final accuracy is around 0.64.
- Currently working on improving model accuracy, as the model has a hard time picking up positive cases.

## Access the App

<div align="center">

### [https://fake-heart-attack.streamlit.app/](https://fake-heart-attack.streamlit.app/)

</div>

Happy faking! 😃
