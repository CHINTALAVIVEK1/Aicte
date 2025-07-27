import os
import zipfile
import requests

DATA_URL = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
ZIP_PATH = "ml-latest-small.zip"
EXTRACT_DIR = "."

# Download the dataset if not already present
def download_dataset():
    if not os.path.exists(ZIP_PATH):
        print("Downloading MovieLens dataset...")
        r = requests.get(DATA_URL)
        with open(ZIP_PATH, 'wb') as f:
            f.write(r.content)
    else:
        print("Zip file already exists.")

# Extract movies.csv
def extract_movies_csv():
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith('movies.csv'):
                print(f"Extracting {file}...")
                zip_ref.extract(file, EXTRACT_DIR)
                # Move to current directory as movies.csv
                os.rename(os.path.join(EXTRACT_DIR, file), 'movies.csv')
                break

if __name__ == "__main__":
    download_dataset()
    extract_movies_csv()
    print("movies.csv is ready!") 