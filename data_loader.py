import pandas as pd
def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns.")
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None
    
# call the function here
if __name__ == "__main__": 
    df = load_data("marketing_AB.csv")
    if df is not None:
        print(df.head())
        print(df.info())
        print(df.describe())