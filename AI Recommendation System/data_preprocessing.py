import pandas as pd
import ast

movies = pd.read_csv("data/tmdb_5000_movies.csv")

# Analysis
# print(movies.columns)
# print(movies.info())
# print(movies.isnull().sum())
# print(movies.shape)

# Cleaning 
movies = movies[
    [
        "id",
        "title",
        "genres",
        "original_language",
        "overview",
        "vote_average",
        "vote_count",
        "popularity",
        "runtime",
        "release_date",
        "keywords",
    ]
]

print(movies.head())

# Handle null  values
movies = movies.dropna()
print(movies.isnull().sum())

# Check genres column
print(movies["genres"].iloc[0])


# Processing Genre Column
def extract_names(text):
    """
    Converts a JSON-like string into a comma-separated list of names.
    """
    items = ast.literal_eval(text)
    return ", ".join(item["name"] for item in items)

movies["genres"] = movies["genres"].apply(extract_names)
movies["keywords"] = movies["keywords"].apply(extract_names)

movies = movies[movies["genres"] != ""]

# Check
print(movies["genres"].iloc[0])

# Language Column Check
print(movies["original_language"].value_counts())

# Mapping languages to full names
language_map = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "zh": "Chinese",
    "cn": "Chinese",
    "de": "German",
    "hi": "Hindi",
    "ja": "Japanese",
    "it": "Italian",
    "ko": "Korean",
    "ru": "Russian",
    "pt": "Portuguese",
    "da": "Danish",
    "sv": "Swedish",
    "nl": "Dutch",
    "fa": "Persian",
    "th": "Thai",
    "he": "Hebrew",
    "id": "Indonesian",
    "cs": "Czech",
    "ta": "Tamil",
    "ro": "Romanian",
    "ar": "Arabic",
    "te": "Telugu",
    "hu": "Hungarian",
    "xx": "Unknown",
    "af": "Afrikaans",
    "is": "Icelandic",
    "tr": "Turkish",
    "vi": "Vietnamese",
    "pl": "Polish",
    "nb": "Norwegian Bokmål",
    "no": "Norwegian",
    "ky": "Kyrgyz",
    "sl": "Slovenian",
    "ps": "Pashto",
    "el": "Greek"
}

movies["original_language"] = (
    movies["original_language"]
    .map(language_map)
    .fillna("Other")
)

languages = sorted(movies["original_language"].unique())

print(languages)

# Extract Release Year 
movies["release_date"] = pd.to_datetime(movies["release_date"])

movies["release_year"] = movies["release_date"].dt.year

# Drop release date
movies.drop(columns=["release_date"], inplace=True)

# Create Tags column
movies["tags"] = (
    movies["genres"] + " " +
    movies["keywords"] + " " +
    movies["overview"]
)

movies.to_csv("data/clean_movies.csv", index=False)

print("Clean dataset saved successfully!")

# Final check
print("\nFinal Dataset:")
print(movies.head())

print("\nColumns:")
print(movies.columns)

print("\nShape:")
print(movies.shape)