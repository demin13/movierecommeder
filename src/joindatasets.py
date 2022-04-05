from importdata import *

movies = movies.merge(credits, on='title')
# print(movies.info())
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]
# print(movies.head())
# print(movies.info())
# print(movies.head()['overview'])
# print(movies.isnull().sum())        #check if any columns contains null values

movies.dropna(inplace=True)
# print(movies.isnull().sum())        #check if any columns contains null values
