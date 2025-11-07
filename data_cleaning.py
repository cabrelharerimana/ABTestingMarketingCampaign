def Clean_data(df):
    
    # Drop duplicates

    if 'user_id' in df.columns:
        df = df.drop_duplicates(subset='user_id')
    
    # clean group column
    if 'group' in df.columns:
        df['test_group'] = df['test_group'].str.strip().str.upper()

    # convert conversion column to binary (1/0)
    if 'converted' in df.columns:
        df['converted'] = df['converted'].map({'Yes': 1, 'No': 0}).fillna(df['converted'])
        df['converted'] = df['converted'].astype(int)
    
    print("Data Cleaned Successfully.")
    return df
