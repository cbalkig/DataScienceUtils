def standardize(series):
    return (series - series.mean()) / series.std()