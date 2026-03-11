import pandas as pd

def build_features(df):

    df["bytes_per_login"] = df["bytes_transferred"] / (df["login_attempts"] + 1)

    return df