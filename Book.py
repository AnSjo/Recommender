import pandas as pd
dt1=pd.read_csv('ratings.csv')
dt2=pd.read_csv('books.csv')
dt3=pd.read_csv('book_tags.csv')
dt4=pd.read_csv('tags.csv')
dt5=pd.read_csv('to_read.csv')

#Removes duplicates
x1=dt1.drop_duplicates(subset=['book_id','user_id'],keep='first')

#contains all rows having author name as 'Suzanne Collins'
x2=dt2.loc[dt2['authors'] == 'Suzanne Collins']
