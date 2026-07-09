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