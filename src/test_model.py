from train_model import *

def recommend(movie_name):
    final_movies = []
    movie_index = movie[movie['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]
    for i in movie_list:
        final_movies.append(movie.iloc[i[0]].title)
    return final_movies