from test_model import recommend, movie
import sys
import os

if __name__ == '__main__':
    print(movie.head()['title'])
    inp_movie = input("Choose movie name: ")
    lst = recommend(inp_movie)
    print(lst)