import pandas as pd
   


def split_cholesterol_sample(df):

 	# split cholesterol according to sample mean
	cholesterol_sample_mean = df_raw_train["Cholesterol"].mean()
	
	df["Cholesterol_sample_split"] = np.where(
        	df["Cholesterol"] > cholesterol_sample_mean, 1, 0
    		)
    
    
	return df
	


def split_blood_pressure(df):

    df[["Systolic", "Diastolic"]] = df["Blood Pressure"].str.split("/", expand=True)
    df["Systolic"] = pd.to_numeric(df["Systolic"])
    df["Diastolic"] = pd.to_numeric(df["Diastolic"])
    df.drop(columns=["Blood Pressure"], inplace=True)

    #return dataframe
    return df

