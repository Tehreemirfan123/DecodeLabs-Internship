import streamlit as st
import pandas as pd

from recommendation import (
    get_filtered_movies,
    recommend_movies
)

st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align: center; color:#FF4B4B;'>
        🎬 AI Movie Recommendation System
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align: center; font-size:18px; color:#6C757D'> 
        Discover movies similar to your favorites using
        <b>Content-Based Filtering</b>.
    </p>
    """,
    unsafe_allow_html=True
)

movies = pd.read_csv("data/clean_movies.csv")

print(movies["genres"].isnull().sum())
print(movies[movies["genres"].isnull()])

# Genre Dropdown
genres = sorted({
    genre.strip()
    for genre_list in movies["genres"].dropna()
    for genre in genre_list.split(",")
})

selected_genre = st.selectbox(
    "Select Genre",
    genres
)

# Language Dropdown
languages = sorted(
    movies["original_language"].unique()
)

selected_language = st.selectbox(
    "Select Language",
    languages
)

# Rating Slider
minimum_rating = st.slider(
    "Minimum Rating",
    min_value=0.0,
    max_value=10.0,
    value=7.5,
    step=0.5
)

# Filter movies
filtered_movies = get_filtered_movies(
    selected_genre,
    selected_language,
    minimum_rating
)

# Movie Droopdown
selected_movie = st.selectbox(
    "Select a Movie",
    filtered_movies["title"]

)