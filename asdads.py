import pandas as pd

xlsx = pd.read_excel("경로.xlsx")
xlsx.to_csv("경로.csv")