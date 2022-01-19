import os

import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose


def _clean_file_name(file_name):
    return file_name.strip().replace(" ", "_").replace("/", "_")


def seasonal_all(df, col_name, col_display, date_col_name, folder=None, orig_color="blue", trend_color="red",
                 legend_position="best", legend_bbox_to_anchor=None, x_label_rotation=0, period=2, plot_trends=True,
                 plot_seasonal=True, plot_residual=True):
    temp_df = df.copy()

    temp_df.index = pd.to_datetime(temp_df[date_col_name])
    series = temp_df[col_name]

    decompose_data = seasonal_decompose(series, model="additive", period=period)

    trend_estimate = decompose_data.trend
    periodic_estimate = decompose_data.seasonal
    residual = decompose_data.resid

    if plot_trends:
        fig, ax = plt.subplots()
        plt.plot(series, label='Original data', color=orig_color)
        plt.plot(trend_estimate, label='Trend', color=trend_color)
        plt.xticks(rotation=x_label_rotation)
        plt.legend(loc=legend_position, bbox_to_anchor=legend_bbox_to_anchor)
        fig.tight_layout()
        if folder is not None:
            if not os.path.exists(folder):
                os.mkdir(folder)
            fig.savefig(os.path.join(folder, "Trend_" + _clean_file_name(col_display) + ".png"))

    if plot_seasonal:
        fig, ax = plt.subplots()
        plt.plot(periodic_estimate, label='Seasonality', color=orig_color)
        plt.xticks(rotation=x_label_rotation)
        fig.tight_layout()
        if folder is not None:
            fig.savefig(os.path.join(folder, "Seasonality_" + _clean_file_name(col_display) + ".png"))

    if plot_residual:
        fig, ax = plt.subplots()
        plt.plot(residual, label='Residuals', color=orig_color)
        plt.xticks(rotation=x_label_rotation)
        fig.tight_layout()
        if folder is not None:
            fig.savefig(os.path.join(folder, "Residuals_" + _clean_file_name(col_display) + ".png"))


def trends(df, col_names, col_displays, date_col_name, folder=None, file_name=None, colors=None, legend_position="best",
           legend_bbox_to_anchor=None, x_label_rotation=0, period=2, method='plot'):
    if colors is None:
        colors = ["blue", "red", "green", "yellow"]
    temp_df = df.copy()

    temp_df.index = pd.to_datetime(temp_df[date_col_name])

    fig, ax = plt.subplots()
    for idx in range(len(col_names)):
        series = temp_df[col_names[idx]]

        decompose_data = seasonal_decompose(series, model="additive", period=period)
        trend_estimate = decompose_data.trend

        if method == 'plot':
            plt.plot(trend_estimate, label=col_displays[idx], color=colors[idx])
        elif method == 'scatter':
            plt.scatter(df['Date'], trend_estimate, label=col_displays[idx], color=colors[idx])

    plt.xticks(rotation=x_label_rotation)
    plt.legend(loc=legend_position, bbox_to_anchor=legend_bbox_to_anchor)
    fig.tight_layout()
    if folder is not None:
        if not os.path.exists(folder):
            os.mkdir(folder)
        fig.savefig(os.path.join(folder, "Trend_" + _clean_file_name(file_name) + ".png"))
