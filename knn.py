import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# Recolección
df = pd.read_csv("penguins_size.csv")

# Procesamiento
df = pd.get_dummies(df, columns=['sex', 'island'], drop_first=True)
df.iloc[:, 1:5] = df.iloc[:, 1:5].fillna(df.iloc[:, 1:5].mean())

scale = StandardScaler()
scale.fit(df.drop(['species'], axis=1))
transformed = scale.transform(df.drop(['species'], axis=1))
df_scaled = pd.DataFrame(transformed, columns=df.columns[1:])

# Entrenamiento
X = df_scaled
y = df['species']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.35)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(x_train, y_train)


def prediction(penguin):
    scaled_penguin = scale.transform(
        pd.DataFrame([penguin], columns=df.columns[1:]))
    transformed_penguin = pd.DataFrame(scaled_penguin, columns=df.columns[1:])
    species = knn.predict(transformed_penguin)
    return species[0]


print(prediction([46.3, 15.8, 215, 5050, 0, 1, 0, 0]))
