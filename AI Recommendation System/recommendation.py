from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import requests
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

movies = pd.read_csv("data/clean_movies.csv")

# Matrix
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["tags"])
cosine_sim = cosine_similarity(tfidf_matrix)

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
# filtered = get_filtered_movies(
#     "Action",
#     "English",
#     7.5
# )

# print(filtered[["title", "vote_average"]].head())

# Recommend Similar Movies
def recommend_movies(movie_title, filtered_movies, top_n=10):
    """
    Recommend the most similar movies using
    TF-IDF + Cosine Similarity.
    """

    # Check whether movie exists
    if movie_title not in movies["title"].values:
        return pd.DataFrame()

    # Check filtered dataset
    if filtered_movies.empty:
        return pd.DataFrame()

    # Find selected movie index
    movie_index = movies[movies["title"] == movie_title].index[0]

    # Get similarity scores
    similarity_scores = list(enumerate(cosine_sim[movie_index]))

    # Sort by similarity
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Keep only filtered movie indices
    filtered_indices = set(filtered_movies.index)

    recommendations = []

    for index, similarity in similarity_scores:

        # Skip selected movie
        if index == movie_index:
            continue

        # Recommend only filtered movies
        if index in filtered_indices:

            recommendations.append({
                "id": movies.iloc[index]["id"],
                "title": movies.iloc[index]["title"],
                "genres": movies.iloc[index]["genres"],
                "language": movies.iloc[index]["original_language"],
                "rating": movies.iloc[index]["vote_average"],
                "release_year": movies.iloc[index]["release_year"],
                "overview": movies.iloc[index]["overview"],
                "similarity_score": round(similarity * 100, 2)
            })

        # Stop after top_n recommendations
        if len(recommendations) == top_n:
            break

    return pd.DataFrame(recommendations)

# Test
# if __name__ == "__main__":

#     filtered_movies = get_filtered_movies(
#         genre="Action",
#         language="English",
#         min_rating=7.5
#     )

#     recommendations = recommend_movies(
#         movie_title="Avatar",
#         filtered_movies=filtered_movies
#     )

#     print(recommendations)

# Poster Fetch
@st.cache_data
def fetch_poster(movie_id):

    api_key = os.getenv("TMDB_API_KEY")

    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}"
        f"?api_key={api_key}"
    )

    response = requests.get(url)

    data = response.json()

    poster_path = data.get("poster_path")

    if poster_path:

        return (
            "https://image.tmdb.org/t/p/w500"
            + poster_path
        )

    return None

# Test
# print(fetch_poster(19995))