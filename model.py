import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn import preprocessing
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("dataset/data.csv",parse_dates=True)


df.drop(['date', 'street','statezip','country','yr_built'], axis = 1, inplace = True)


df['yr_renovated'] = df['yr_renovated'].map(lambda x: 0 if x == 0 else 1)
df['sqft_basement'] = df['sqft_basement'].map(lambda x: 0 if x == 0 else 1)

le = preprocessing.LabelEncoder()
df['city'] = le.fit_transform(df.city.values)

# Fix random_state
seed = 0

# get data

X = df.loc[:, df.columns != 'price'].values
y = df.loc[:,['price']].values

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = seed)


regressor = ensemble.GradientBoostingRegressor(max_depth=3)
regressor.fit(X_train, y_train.ravel())

y_pred = regressor.predict(X_test)


print("Test MAE",mean_absolute_error(y_test,y_pred))
print("Train MAE",mean_absolute_error(y_train,regressor.predict(X_train)))

pickle.dump(regressor, open('model.pkl', 'wb'))