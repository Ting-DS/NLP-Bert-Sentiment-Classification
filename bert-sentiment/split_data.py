import pandas as pd

d1 = pd.read_csv('IMDB_Dataset.csv')
# print(d1.head(10))

d1_train_positive = d1[d1['sentiment']=='positive'][:50]
d1_train_negative = d1[d1['sentiment']=='negative'][:50]

d1_train = pd.concat([d1_train_positive,d1_train_negative],axis=0)


d1_train[['review']].to_csv('imdb_train.csv',index=False)

d1_test_positive = d1[d1['sentiment']=='positive'][12500:12550]
d1_test_negative = d1[d1['sentiment']=='negative'][12500:12550]

d1_test = pd.concat([d1_test_positive,d1_test_negative],axis=0)


d1_test[['review']].to_csv('imdb_test.csv',index=False)
print(d1_test[['review']].head(10))



