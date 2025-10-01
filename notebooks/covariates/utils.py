import matplotlib.dates as mdates 
import matplotlib.pyplot as plt 
import pandas as pd

def plot_series(df, col_name: str):
    
    """
    Plots a line plot for a given dataset and a column name.
    """
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['date'], df[col_name])
    
    # Title and labels
    ax.set_title(col_name.capitalize())
    ax.set_xlabel("Date")
    ax.set_ylabel(col_name)
    
    # Format x-axis as YYYY-MM-DD
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    
    # Rotate labels for readability
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show() 

def create_future_dataframe():
    """
    Creates the future dataframe that will be used to make the 2025 predictions
    """ 

    test_df = pd.DataFrame(
    {
        "date": [f"2025-{i}-01" for i in range(1,13)],
        "t": [i for i in range(120, 132)]
    }
    )

    test_df['date'] = pd.to_datetime(test_df['date'], format="%Y-%m-%d")
    test_df['month'] = test_df['date'].dt.month  

    return test_df

def get_filtered_data(df_path=None) -> pd.DataFrame:
    """
    This function filters the data to select on the entries that begin at 2015. 
    That filter is required because we have NA values prior to that date and we also do not need
    all that historical data because it behaves very differently from the years of 2020 and ahead
    """ 
    if df_path is None:
        df = pd.read_csv("../../data/tidy_data.csv", parse_dates=[0])
    else:
        df = pd.read_csv(df_path, parse_dates=[0])

    df_new = df.dropna(axis=0)
    df_new = df_new.iloc[5:, ] 

    return df_new