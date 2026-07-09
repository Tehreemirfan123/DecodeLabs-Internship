import streamlit as st
import pandas as pd

from recommendation import (
    get_filtered_movies,
    recommend_movies, 
    fetch_poster
)

st.set_page_config(
    page_title="CineMatch AI",
    page_icon="🎬",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align: center; color:#FF4B4B;'>
        🎬 CineMatch AI
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

# Genre Dropdown
genres = sorted({
    genre.strip()
    for genre_list in movies["genres"]
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

# Filter Movies
filtered_movies = get_filtered_movies(
    selected_genre,
    selected_language,
    minimum_rating
)

# Movie Dropdown
selected_movie = st.selectbox(
    "Select a Movie",
    filtered_movies["title"]
)

if st.button("🎬 Recommend Movies"):

    st.subheader("✨ Recommended For You")

    recommendations = recommend_movies(
        movie_title=selected_movie,
        filtered_movies=filtered_movies
    )

    if recommendations.empty:
        st.warning("No similar movies found.")

    else:
        # st.dataframe(recommendations)
        # st.success("Recommendations generated successfully!")

        cols = st.columns(5)

        for index, (_, movie) in enumerate(recommendations.iterrows()):
            with cols[index % 5]:
                with st.container(border=True):
                    poster = fetch_poster(movie["id"])

                    if poster:
                        _, center, _ = st.columns([1, 4, 1])
                        with center:
                            st.image(poster, width=160)
                        # st.image(poster, width=170)
                    st.markdown(f"### {movie['title']}")
                    st.markdown(f"⭐ **Rating:** {movie['rating']}")
                    st.markdown(f"📅 **Year:** {movie['release_year']}")
                    st.markdown(
                        f"📊 **Match:** {movie['similarity_score']}%"
                    )
                    with st.expander("Synopsis"):
                        st.write(movie["overview"])