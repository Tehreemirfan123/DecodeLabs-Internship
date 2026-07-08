import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("data/clean_movies.csv")

# Matrix
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(
    movies["tags"]
)

# print(tfidf_matrix.shape)

# Calculate cosine Similarity
cosine_sim = cosine_similarity(
    tfidf_matrix,
    tfidf_matrix
)

# print(cosine_sim.shape)

# Filter movies first
def get_filtered_movies(genre, language, min_rating):

    filtered_movies = movies[
        (movies["genres"].str.contains(genre, case=False, na=False))
        &
        (movies["original_language"] == language)
        &
        (movies["vote_average"] >= min_rating)
    ]

    return filtered_movies

# Test it 
filtered = get_filtered_movies(
    "Action",
    "English",
    7.5
)

print(filtered[["title", "vote_average"]].head())
