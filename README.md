# Genre-Based Movie Recommender System

A simple content-based movie recommender system built with Python and Streamlit. This app recommends the top 5 movies for a selected genre, prioritizing both high ratings and popularity (number of ratings), using the MovieLens public dataset.

## Features
- Select a movie genre and get the top 5 best-rated and popular movies in that genre
- Uses MovieLens data for real-world relevance
- Interactive web UI built with Streamlit

## Demo
![screenshot](screenshot.png) <!-- Add a screenshot if you wish -->

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/CHINTALAVIVEK1/<repo-name>.git
   cd <repo-name>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download MovieLens data**
   - Run the provided script:
     ```bash
     python download_movielens.py
     ```
   - Or manually download and extract `ml-latest-small.zip` from [MovieLens](https://grouplens.org/datasets/movielens/latest/) into the `ml-latest-small` folder.

4. **Run the app**
   ```bash
   streamlit run app.py
   ```
   - Open the local URL shown in your terminal (e.g., http://localhost:8501)

## How it works
- The app loads movie and rating data from MovieLens
- For the selected genre, it recommends movies with at least 50 ratings, sorted by average rating and then by popularity

## Credits
- Movie data from [MovieLens](https://grouplens.org/datasets/movielens/)
- Built with [Streamlit](https://streamlit.io/) and [pandas](https://pandas.pydata.org/)

## License
This project is for educational purposes. 