import streamlit as st
import pickle
import pandas as pd
import requests


recommended_anime_list = []
recommended_anime_poster = []
def recommend(anime):
    anime_index = anime_list[anime_list['Name'] == anime].index[0]
    distances = similarity[anime_index]
    sorted_anime_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:11]
    
    for i in sorted_anime_list:
        recommended_anime_list.append(anime_list.iloc[i[0]].Name)
        
    
    return recommended_anime_list
        

anime_list = pickle.load(open('anime.pkl', 'rb'))
anime_list = pd.DataFrame(anime_list)
animes_list = anime_list['Name'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

top_50 = pickle.load(open('top_50.pkl', 'rb'))

st.sidebar.title("Anime Recommender System")
#to run the projcet use cmd --> streamlit run app.py
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Top 50 Anime', 'Anime Recommender System')
)

if user_menu == "Top 50 Anime":
    st.title('Top 50 Anime')
    top_50 = pd.DataFrame(top_50)
    anime_names = top_50['Name'].values

    index = 0
    for j in range(10):
        col = st.columns(5)
        for i in range(5):
            with col[i]:
                st.write(f"**{anime_names[index][:16]}**")
                st.image(top_50.iloc[index]['Image URL'])
                index += 1

    
if user_menu == "Anime Recommender System":
    st.title('Anime Recommender System')

    selected_anime_name = st.selectbox(
        'Select an anime',
        (animes_list))



    if st.button("Recommend"):
        names = recommend(selected_anime_name)
        new_names = []
        posters = []
        for i in names:
            posters.append(list(anime_list[anime_list['Name']==i]['Image URL']))
            new_names.append(i[:16])
        

    
        col1, col2, col3, col4, col5 = st.columns(5)
        # col1, col2, col3, col4, col5, col6, col7, col8,  col9, col10 = st.columns(10)

        with col1:
            st.write(names[0][:16])
            st.image(posters[0])
            

        with col2:
            st.text(new_names[1])
            st.image(posters[1])

        with col3:
            st.text(new_names[2])
            st.image(posters[2])
            
        with col4:
            st.text(new_names[3])
            st.image(posters[3])

        with col5:
            st.text(new_names[4])
            st.image(posters[4])
            
            
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(new_names[5])
            st.image(posters[5])

        with col2:
            st.text(new_names[6])
            st.image(posters[6])

        with col3:
            st.text(new_names[7])
            st.image(posters[7])
            
        with col4:
            st.text(new_names[8])
            st.image(posters[8])

        with col5:
            st.text(new_names[9])
            st.image(posters[9])



