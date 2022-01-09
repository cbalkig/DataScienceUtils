# Data Science Utilities and Helpers

```
pip install dats-lab
```

```
seasonal_all(df, "USD_mean_Rate", "USD Rate")
```
Or, to save into a folder:
```
seasonal_all(df, "USD_mean_Rate", "USD Rate", destination_folder_path)
```

![seasonal_all_1.png](./images/seasonal_all_1.png)

![seasonal_all_2.png](./images/seasonal_all_2.png)

![seasonal_all_3.png](./images/seasonal_all_3.png)

```
trends(df, ["USD_mean_Rate", "Inflation_Rate"], ["USD Rate", "Inflation Rate"], date_col_name="Date")
``` 
Or, to save into a folder:
```
trends(df, ["USD_mean_Rate", "Inflation_Rate"], ["USD Rate", "Inflation Rate"], date_col_name="Date", folder=trend_figures_path)
```

![trends.png](./images/trends.png)
