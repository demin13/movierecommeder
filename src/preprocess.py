from preprocessmethod import *

movies['genres'] = movies['genres'].apply(converter)
movies['keywords'] = movies['keywords'].apply(converter)
movies['cast'] = movies['cast'].apply(converterspecificnums)
movies['crew'] = movies['crew'].apply(fetch_director)
movies['overview'] = movies['overview'].apply(lambda x:x.split())

# print(movies.head(5)['genres'])
# print(movies.head()['genres'])
# print(movies.head()['keywords'])
# print(movies.head()['cast'])
# print(movies.head()['crew'])
# print(movies['overview'][0])
# print(movies.head())


#removing all spaces between two words 

movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])
# movies['overview'] = movies['overview'].apply(lambda x:[i.replace(" ","") for i in x])
movies['tags'] = movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']

# print(movies.head()['tags'])
movie = pd.DataFrame()
movie = movies[['movie_id','title','tags']]
movie['tags'] = movie['tags'].apply(lambda x:" ".join(x))
movie['tags'] = movie['tags'].apply(lambda x:x.lower())

# print(movie['tags'][0])
# print(movie['tags'][1])