from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import *
from preprocessmethod import stemwords

movie['tags'] = movie['tags'].apply(stemwords)
cv = CountVectorizer(max_features=5000, stop_words='english')
movie_vector = cv.fit_transform(movie['tags']).toarray()

# print(movie_vector[0])
# print(cv.get_feature_names_out())

similarity = cosine_similarity(movie_vector)

# print(similarity[1])