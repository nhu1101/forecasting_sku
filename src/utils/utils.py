import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def fill_missing_values(data):
    data_filled = data.copy()
    data_filled['qty'] = data_filled.groupby('sku')['qty'].transform(lambda x: x.fillna(x.mean()))
    data_filled['revenue'] = data_filled.groupby('sku')['revenue'].transform(lambda x: x.fillna(x.mean()))
    data_filled['COGS'] = data_filled.groupby('sku')['qty'].transform(lambda x: x.fillna(x.mean()))
    return data_filled

def correct_outliers(df, factor=3):
    """Identify and correct outliers in the 'sales' column by reducing them to the mean"""
    df_corrected = df.copy()

    # Identify outliers using z-score
    z_scores = (df_corrected["qty"] - df_corrected["qty"].mean()) / df_corrected[
        "qty"
    ].std()
    outlier_indices = np.abs(z_scores) > factor  # Adjust the threshold as needed
    # Correct outliers by reducing them to the mean
    df_corrected.loc[outlier_indices, "qty"] = df_corrected["qty"].mean()

    return df_corrected

def fill_date_template(data,min_date, max_date):
    date_range = pd.date_range(start=min_date, end=max_date)
    date_range['key'] = 1
    sku_template = pd.DataFrame({'sku': data['sku'].unique()})
    sku_template['key'] = 1
    template = pd.merge(sku_template, date_range, on='key').drop('key', axis=1)

    data_merge = pd.merge(template, data, on=['sku', 'shipped_date'], how='left')
    data_merge['qty'] = data_merge['qty'].fillna(0)
    data_merge['revenue'] = data_merge['revenue'].fillna(0)
    data_merge['COGS'] = data_merge['COGS'].fillna(0)
    
    return data_merge

