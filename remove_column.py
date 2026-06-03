import pandas as pd

df = pd.read_csv('./data/titanic_procesado.csv')

df = df.rename(columns={'Ebmarked': 'Embarked' })

df.to_csv('./data/titanic_procesado.csv', index=False)