def recomended_popular (nmovies):
    import pandas as pd
    ### Downloading the datasets
    links = pd.read_csv('links.csv')
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    tags = pd.read_csv('tags.csv')
    
    ### Creating ratings and count of evaluations
    ratings_counts = ratings.groupby(by = "movieId").count()
    ratings_counts = ratings_counts.reset_index()
    ratings_counts = ratings_counts[["movieId","userId"]]
    
    ratings_mean = ratings.groupby(by = "movieId").mean()
    ratings_mean = ratings_mean.reset_index()
    ratings_mean = ratings_mean[["movieId","rating"]]

    ### Merging the columns with the movies dataframe and re-naming
    
    movies = movies.merge(ratings_counts,
                      on = "movieId",
                      how = "left"
                     )

    movies = movies.merge(ratings_mean,
                      on = "movieId",
                      how = "left"
                     )
    
    movies = movies.rename(columns = {"userId":"count_users", "rating":"mean_rating"})
    
    ### Creating total score based on the amount of evaluations and mean rating
    movies["total_score"] = movies["count_users"] * movies["mean_rating"]**2
    
    ### Filtering only movies which were rated more than the "mean" value of "count"
    top_movies = movies.copy()
    top_movies = top_movies.drop_duplicates("movieId")
    mask_ids = top_movies.nlargest(nmovies,"total_score")
    recomended_movies = movies.loc[movies["movieId"].isin(mask_ids["movieId"]), :] 
    recomended_movies = recomended_movies[["movieId","title","genres","count_users","mean_rating","total_score"]].sort_values(by = "mean_rating", ascending = False)
    recomended_movies = recomended_movies.drop_duplicates()
    recomended_movies = recomended_movies.merge(links,
                                                on="movieId",
                                                how = "left",
                                               )
    

    return recomended_movies


def pictures(tmdbId):
    import requests
    import random

    url = f"https://api.themoviedb.org/3/movie/{tmdbId}/images"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzNDg3Zjc0NTBkZDA3M2IyYzY5NTY4NWYzNmQ2ZDAwMCIsInN1YiI6IjY1Y2QwMDY2MjU4ODIzMDE3ZGE3NjEzNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XNPdNDUUjwg8La9nO-Hhj9wRWN27TtgzTwXjl95DxyE"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    
    if len(data["backdrops"]) == 1:
        poster_path = data["backdrops"][0]["file_path"]
        return f'https://image.tmdb.org/t/p/w500{poster_path}'
    if len(data["backdrops"]) >= 1:
        poster_path = data["backdrops"][random.randint(0, len(data["backdrops"])-1)]["file_path"]
        return f'https://image.tmdb.org/t/p/w500{poster_path}'
    else:
        numero = random.randint(1,2)
        if numero == 1:
            return "https://images7.alphacoders.com/111/1112855.jpg"
        else:
            return "https://www.chromethemer.com/wallpapers/chromebook-wallpapers/images/960/colorful-space-cat-chromebook-wallpaper.jpg"

def process_string(s):
    import re
    # Extract content within parentheses
    parentheses_content = re.findall(r'\(.*?\)', s)
    # Remove content within parentheses from the original string
    s_without_parentheses = re.sub(r'\s*\(.+?\)\s*', ' ', s)  # Ensure a space remains after removal
    
    # Check if there's a comma and split
    if ',' in s_without_parentheses:
        parts = s_without_parentheses.split(',')
        parts.reverse()
        # Add a space after the inversion if there's content to append later
        inverted_string = ' '.join(parts).strip()  # Use strip() to remove any leading/trailing spaces
    else:
        inverted_string = s_without_parentheses.strip()
    
    # Append parentheses content to the end, if any, with a space in between
    if parentheses_content:
        inverted_string += ' ' + ' '.join(parentheses_content).strip()
    
    return inverted_string

    # Function to show image and title with fixed height for the title
def display_movie_with_fixed_height(col, image_url, title):
    col.markdown(f"""
        <div style="text-align: center;">
            <img src="{image_url}" style="max-height: 200px;">
            <p style="color: white; height: 3em;">{title}</p>
            </div>
        """, unsafe_allow_html=True)
    
