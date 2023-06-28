import pandas as pd
df = pd.read_csv('~/Downloads/dataset/test.csv')

df.head(1)
df.drop('BULLET_POINT',axis=1, inplace=True)

#SAVE
df.to_csv('~/Downloads/dataset/testClean.csv', index=False)


