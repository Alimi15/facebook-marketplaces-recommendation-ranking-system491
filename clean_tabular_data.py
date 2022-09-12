import pandas as pd
import numpy as np

def remove_missing_rows(df: pd.DataFrame):
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df.drop(df[df["location"].str.len() == 0].index, inplace=True)
    df.drop(df[df["location"] == np.nan].index, inplace=True)
    df.drop(df[df["price"] == np.nan].index, inplace=True)
    df.drop(df[df["product_description"] == np.nan].index, inplace=True)
    df.drop(df[df["product_description"].str.len() == 0].index, inplace=True)
    df.drop(df[df["category"] == np.nan].index, inplace=True)
    df.drop(df[df["category"].str.len() == 0].index, inplace=True)
    df.drop(df[df["product_name"] == np.nan].index, inplace=True)
    df.drop(df[df["product_name"].str.len() == 0].index, inplace=True)
    vals = df["price"].values
    for i, value in enumerate(vals):
        vals[i] = value.replace("£", "").replace(",", "")
    df["price"].replace(df["price"].values, vals, inplace=True)
    df["price"] = df["price"].astype("float64")
    vals = df["category"].values
    for i, value in enumerate(vals):
        vals[i] = value.split("/")[0].strip()
    df["category"].replace(df["category"].values, vals, inplace=True)
    df["category"] = pd.Categorical(df["category"])
    df["category"] = df["category"].cat.codes
    return df