import streamlit as st
import pandas as pd
from functions import recomended_popular, pictures, process_string

st.set_page_config(layout="wide")

css = """
<style>
    /* Change the background color of the page and the color of the general text */
    body {
        background-color: #000000; /* Negro */
        color: #ffffff; /* Blanco */
    }
    .stApp {
        background-color: #000000; /* Negro */
    }
    /* Specific for changing the color of the heads */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff; /* Blanco */
    }
    /* Button style */
    .stButton>button {
        border: 2px solid #ffffff; /* Borde blanco para el botón */
        border-radius: 20px; /* Bordes redondeados */
        color: #000000; /* Letras negras */
        background-color: #ffffff; /* Fondo blanco */
    }
</style>
"""


st.markdown(css, unsafe_allow_html=True)

# Custom CSS to apply st.markdown()
st.markdown("""
<style>
.lightblue-text {
    color: #add8e6;  /* Azul claro */
}
.yellow-text {
    color: #ffff00;  /* Amarillo */
}
</style>
""", unsafe_allow_html=True)

# Using st.markdown() to create a header with specific colors
st.markdown("""
<h1>
    <span class=" yellow-text">Welcome to</span> <span class="lightblue-text">WBSFLIX</span> 
</h1>
""", unsafe_allow_html=True)

# Using st.markdown() to create a header with specific colors
st.markdown("""
<h1>
    <span class="lightblue-text">Movie Recomendations</span> 
</h1>
""", unsafe_allow_html=True)

Options = st.selectbox("_Types of Movie Recommendations_",
                       ("Popular Recommendations", "Based on the movies you saw", "Surprise yourself"))

if Options == "Popular Recommendations":

    recomended_popular_movies = recomended_popular(50)
    recomended_popular_movies = recomended_popular_movies.sample(10)
    recomended_popular_movies = recomended_popular_movies[["title","tmdbId"]]
    recomended_popular_movies["tmdbId"] = recomended_popular_movies["tmdbId"].astype(int)
    recomended_popular_movies['title'] = recomended_popular_movies['title'].apply(process_string)


    movies_first_row = recomended_popular_movies.iloc[:5]
    movies_second_row = recomended_popular_movies.iloc[5:]

    columns = st.columns(5, gap="small")
    for i, col in zip(movies_first_row["tmdbId"], columns):
        # Use the column as the context for displaying the image
        with col:
            st.image(pictures(i), use_column_width=True)
            if len(movies_first_row.loc[movies_first_row["tmdbId"] == i, ["title"]].values[0][0]) < 30:
                movie_name = movies_first_row.loc[movies_first_row["tmdbId"] == i, ["title"]].values[0][0]
                tmdbIds = movies_first_row.loc[movies_first_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbIds}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{movie_name}</a>', unsafe_allow_html=True)
            else:
                my_string = movies_first_row.loc[movies_first_row["tmdbId"] == i, ["title"]].values[0][0]
                new_string = my_string[:30] + "..."
                tmdbId = movies_first_row.loc[movies_first_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbId}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{new_string}</a>', unsafe_allow_html=True)
                
    columns = st.columns(5, gap="small")
    for i, col in zip(movies_second_row["tmdbId"], columns):
        # Use the column as the context for displaying the image
        with col:
            st.image(pictures(i), use_column_width=True)
            if len(movies_second_row.loc[movies_second_row["tmdbId"] == i, ["title"]].values[0][0]) < 30:
                movie_name = movies_second_row.loc[movies_second_row["tmdbId"] == i, ["title"]].values[0][0]
                tmdbIds = movies_second_row.loc[movies_second_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbIds}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{movie_name}</a>', unsafe_allow_html=True)
            else:
                my_string = movies_second_row.loc[movies_second_row["tmdbId"] == i, ["title"]].values[0][0]
                new_string = my_string[:30] + "..."
                tmdbId = movies_second_row.loc[movies_second_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbId}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{new_string}</a>', unsafe_allow_html=True)
            
            
if Options == "Based on the movies you saw":

    recomended_popular_movies = recomended_popular(30)
    item_based = pd.read_csv('item_based_cos_top_50 (1).csv') 
    item_based = item_based.sample(10)
    item_based["tmdbId"] = item_based["tmdbId"].astype(int)
    item_based = item_based[["title", "tmdbId"]]
    item_based['title'] = item_based['title'].apply(process_string)
    
    movies_first_row = item_based.iloc[:5]
    movies_second_row = item_based.iloc[5:]

    columns = st.columns(5, gap="small")
    for i, col in zip(movies_first_row["tmdbId"], columns):
        # Use the column as the context for displaying the image
        with col:
            st.image(pictures(i), use_column_width=True)
            if len(movies_first_row.loc[movies_first_row["tmdbId"] == i, ["title"]].values[0][0]) < 30:
                movie_name = movies_first_row.loc[movies_first_row["tmdbId"] == i, ["title"]].values[0][0]
                tmdbIds = movies_first_row.loc[movies_first_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbIds}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{movie_name}</a>', unsafe_allow_html=True)
            else:
                my_string = movies_first_row.loc[movies_first_row["tmdbId"] == i, ["title"]].values[0][0]
                new_string = my_string[:30] + "..."
                tmdbId = movies_first_row.loc[movies_first_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbId}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{new_string}</a>', unsafe_allow_html=True)
                
    columns = st.columns(5, gap="small")
    for i, col in zip(movies_second_row["tmdbId"], columns):
        # Use the column as the context for displaying the image
        with col:
            st.image(pictures(i), use_column_width=True)
            if len(movies_second_row.loc[movies_second_row["tmdbId"] == i, ["title"]].values[0][0]) < 30:
                movie_name = movies_second_row.loc[movies_second_row["tmdbId"] == i, ["title"]].values[0][0]
                tmdbIds = movies_second_row.loc[movies_second_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbIds}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{movie_name}</a>', unsafe_allow_html=True)
            else:
                my_string = movies_second_row.loc[movies_second_row["tmdbId"] == i, ["title"]].values[0][0]
                new_string = my_string[:30] + "..."
                tmdbId = movies_second_row.loc[movies_second_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbId}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{new_string}</a>', unsafe_allow_html=True)
    
if Options == "Surprise yourself":
    
    recomended_popular_movies = recomended_popular(50)
    item_based = pd.read_csv('item_based_cos_top_50 (1).csv') 
    user_based = pd.read_csv('user_based_top_50.csv') 
    user_based = user_based.sample(10)
    user_based["tmdbId"] = user_based["tmdbId"].astype(int)
    user_based = user_based.loc[~user_based["movieId"].isin(recomended_popular_movies["movieId"]),:]
    user_based = user_based.loc[~user_based["movieId"].isin(item_based["movieId"]),:]
    user_based = user_based[["title", "tmdbId"]]
    user_based['title'] = user_based['title'].apply(process_string)

    movies_first_row = user_based.iloc[:5]
    movies_second_row = user_based.iloc[5:]

    columns = st.columns(5, gap="small")
    for i, col in zip(movies_first_row["tmdbId"], columns):
        # Use the column as the context for displaying the image
        with col:
            st.image(pictures(i), use_column_width=True)
            if len(movies_first_row.loc[movies_first_row["tmdbId"] == i, ["title"]].values[0][0]) < 30:
                movie_name = movies_first_row.loc[movies_first_row["tmdbId"] == i, ["title"]].values[0][0]
                tmdbIds = movies_first_row.loc[movies_first_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbIds}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{movie_name}</a>', unsafe_allow_html=True)
            else:
                my_string = movies_first_row.loc[movies_first_row["tmdbId"] == i, ["title"]].values[0][0]
                new_string = my_string[:30] + "..."
                tmdbId = movies_first_row.loc[movies_first_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbId}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{new_string}</a>', unsafe_allow_html=True)
                
    columns = st.columns(5, gap="small")
    for i, col in zip(movies_second_row["tmdbId"], columns):
        # Use the column as the context for displaying the image
        with col:
            st.image(pictures(i), use_column_width=True)
            if len(movies_second_row.loc[movies_second_row["tmdbId"] == i, ["title"]].values[0][0]) < 30:
                movie_name = movies_second_row.loc[movies_second_row["tmdbId"] == i, ["title"]].values[0][0]
                tmdbIds = movies_second_row.loc[movies_second_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbIds}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{movie_name}</a>', unsafe_allow_html=True)
            else:
                my_string = movies_second_row.loc[movies_second_row["tmdbId"] == i, ["title"]].values[0][0]
                new_string = my_string[:30] + "..."
                tmdbId = movies_second_row.loc[movies_second_row["tmdbId"] == i, "tmdbId"].values[0]
                url = f"https://www.themoviedb.org/movie/{tmdbId}"
                st.markdown(f'<a href="{url}" style="color: white;" target="_blank">{new_string}</a>', unsafe_allow_html=True)

# Set a key in the session state to track whether to update the film set
if 'update_movies' not in st.session_state:
    st.session_state.update_movies = False

# Function to update the session status and force film reloading
def update_movie_set():
    # Change the value to force the update
    st.session_state.update_movies = not st.session_state.update_movies

# Button that calls the update_movie_set() function
st.button("Show more", on_click=update_movie_set)


st.markdown("""
<style>
.custom-text {
    font-size: 24px; /* Ajusta este valor según necesites */
    font-weight: bold; /* Hace el texto en negrita */
}
.lightblue-text {
    color: #add8e6;  /* Azul claro */
}
.yellow-text {
    color: #ffff00;  /* Amarillo */
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<h1 class="custom-text">
    <span class="lightblue-text">Website design by:</span> 
</h1>
""", unsafe_allow_html=True)
st.markdown(f'<p style="color: yellow;">Sweta</p>', unsafe_allow_html=True)
st.markdown(f'<p style="color: yellow;">Helene</p>', unsafe_allow_html=True)
st.markdown(f'<p style="color: yellow;">Dante</p>', unsafe_allow_html=True)

