import os
import pandas as pd

from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt


def clean_file_name(file_name):
    return file_name.strip().replace(" ", "_").replace("/", "_")


def seasonal_all(df, src_field, src_display, folder=None):
    temp_df = df.copy()

    temp_df.index = pd.to_datetime(temp_df['Date'])
    series = temp_df[src_field]

    decompose_data = seasonal_decompose(series, model="additive")

    trend_estimate = decompose_data.trend
    periodic_estimate = decompose_data.seasonal
    residual = decompose_data.resid

    fig, ax = plt.subplots()
    plt.plot(series, label='Original ' + src_display, color='blue')
    plt.plot(trend_estimate, label='Trend of ' + clean_file_name(src_display), color='red')
    plt.legend(loc='best')
    fig.tight_layout()
    if folder is not None:
        fig.savefig(os.path.join(folder, "Trend_" + clean_file_name(src_display) + ".png"))

    fig, ax = plt.subplots()
    plt.plot(periodic_estimate, label='Seasonality of ' + src_display, color='blue')
    plt.legend(loc='best')
    fig.tight_layout()
    if folder is not None:
        fig.savefig(os.path.join(folder, "Seasonality_" + clean_file_name(src_display) + ".png"))

    fig, ax = plt.subplots()
    plt.plot(residual, label='Decomposition residuals of ' + src_display, color='blue')
    plt.legend(loc='best')
    fig.tight_layout()
    if folder is not None:
        fig.savefig(os.path.join(folder, "Residuals_" + clean_file_name(src_display) + ".png"))
