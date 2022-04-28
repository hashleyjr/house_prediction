import pandas as pd

df = pd.read_csv("dataset/data.csv")


df.drop(['date', 'street','statezip','country'], axis = 1, inplace = True)