import streamlit as st
import pickle 

new_movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(moviename):
    movie_index = new_movies[new_movies['title'] == moviename].index[0]
    movie_list = sorted(enumerate(similarity[movie_index]), key = lambda x: x[1], reverse = True)[1:6]
    recommended_list = []

    for title in movie_list:
        recommended_list.append(new_movies.iloc[title[0]]['title'])

    return recommended_list
        
st.title("Movie Recommender")
selected_movie = st.selectbox('Select a movie: ', new_movies['title'].values)
if st.button('Recommend Me '):
    recommended_movies = recommend(selected_movie)
    for title in recommended_movies:
        st.write(title)










