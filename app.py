import streamlit as st
import pandas as pd
import os

# Load data
def load_movies():
    if not os.path.exists('movies.csv'):
        st.error("movies.csv not found. Please run download_movielens.py first.")
        return None
    df = pd.read_csv('movies.csv')
    return df

def load_ratings():
    ratings_path = os.path.join('ml-latest-small', 'ratings.csv')
    if not os.path.exists(ratings_path):
        st.error("ratings.csv not found in ml-latest-small. Please extract all files from the zip.")
        return None
    ratings = pd.read_csv(ratings_path)
    return ratings

def get_unique_genres(df):
    genres = set()
    for genre_list in df['genres']:
        for genre in genre_list.split('|'):
            genres.add(genre)
    genres.discard('(no genres listed)')
    return sorted(list(genres))

# Recommend top 5 movies for a genre by best rating and popularity
def recommend_best_rated_popular(movies_df, ratings_df, genre, min_ratings=50):
    filtered = movies_df[movies_df['genres'].str.contains(genre, case=False, na=False)]
    # Calculate average rating and number of ratings per movieId
    rating_stats = ratings_df.groupby('movieId').agg(avg_rating=('rating', 'mean'), num_ratings=('rating', 'count')).reset_index()
    # Merge with filtered movies
    merged = pd.merge(filtered, rating_stats, on='movieId', how='left').fillna({'avg_rating': 0, 'num_ratings': 0})
    # Only consider movies with at least min_ratings
    merged = merged[merged['num_ratings'] >= min_ratings]
    # Sort by average rating, then by number of ratings
    top = merged.sort_values(['avg_rating', 'num_ratings'], ascending=[False, False]).head(5)
    return top[['title', 'genres', 'avg_rating', 'num_ratings']]

# Streamlit UI
st.title("🎬 Genre-Based Movie Recommender (Best Rated & Popular)")

movies_df = load_movies()
ratings_df = load_ratings()
if movies_df is not None and ratings_df is not None:
    genres = get_unique_genres(movies_df)
    selected_genre = st.selectbox("Select a genre:", genres)
    if selected_genre:
        st.subheader(f"Top 5 {selected_genre} Movies (Best Rated & Popular):")
        recommendations = recommend_best_rated_popular(movies_df, ratings_df, selected_genre)
        st.table(recommendations) 