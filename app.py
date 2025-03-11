
import streamlit as st 
import pickle
import requests
st.header("Movie Recommendation")
def fetch_posters(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=499d72054454438985d54b9185f62c61&language=en-US"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if not poster_path:
            print(f"No poster available for movie ID {movie_id}.")
            return "https://via.placeholder.com/500x750?text=No+Poster+Available"  # Placeholder image
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except Exception as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error+Fetching+Poster"


movie_list=pickle.load(open('movie_list.pkl','rb'))
similar=pickle.load(open('similar.pkl','rb'))

searched_movie=st.selectbox("Select movie:",movie_list)


def recommend_movies(index):
    movies=[]
    posters=[]
    similar_indexes=sorted(list(enumerate(similar[index])),key=lambda x:x[1],reverse=True)[:10]
    similar_movies=list(movie_list.loc[i[0],['title','movie_id']] for i in similar_indexes)
    for i in similar_movies:
        movies.append(i[0])
        print(i[1])
        posters.append(fetch_posters(i[1]))
    return movies,posters
if st.button("Show recommend"):
    index= movie_list.loc[movie_list['title']==searched_movie].index[0]
    similar_movies=recommend_movies(index)
    recommended_movies,recommended_posters=recommend_movies(index)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 =st.columns(10)
    with   col1:
        st.text(recommended_movies[0])
        st.image(recommended_posters[0]) 
    with   col2:
        st.text(recommended_movies[1])
        st.image(recommended_posters[1]) 
    with   col3:
        st.text(recommended_movies[2])
        st.image(recommended_posters[2]) 
    with   col4:
        st.text(recommended_movies[3])
        st.image(recommended_posters[3]) 
    with   col5:
        st.text(recommended_movies[4])
        st.image(recommended_posters[4]) 
    with   col6:
        st.text(recommended_movies[5])
        st.image(recommended_posters[5]) 
    with   col7:
        st.text(recommended_movies[6])
        st.image(recommended_posters[6]) 
    with   col8:
        st.text(recommended_movies[7])
        st.image(recommended_posters[7]) 
    with   col9:
        st.text(recommended_movies[8])
        st.image(recommended_posters[8]) 
    with   col10:
        st.text(recommended_movies[9])
