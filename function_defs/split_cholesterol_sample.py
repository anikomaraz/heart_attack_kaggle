import pandas as pd
   


def split_cholesterol_sample(df):

 	# split cholesterol according to sample mean
	cholesterol_sample_mean = df_raw_train["Cholesterol"].mean()
	
	df["Cholesterol_sample_split"] = np.where(
        	df["Cholesterol"] > cholesterol_sample_mean, 1, 0
    		)
    
    
	return df


