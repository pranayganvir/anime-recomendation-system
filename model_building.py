# %% [markdown]
# #### 1. Import Libraries

# %% [markdown]
# #### DATA
# Anime Dataset 2023
# https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset
# 
# i use anime dataset 2023 to develope a anime recomendation system
# 
# - anime_id: Unique ID for each anime.
# - Name: The name of the anime in its original language.
# - English name: The English name of the anime.
# - Other name: Native name or title of the anime(can be in Japanese, Chinese or Kaorean).
# - Score: The score or rating given to the anime.
# - Genres: The genres of the anime, separated by commas.
# - Synopsis: A brief description or summary of the anime's plot.
# - Type: The type of the anime (e.g., TV series, movie, OVA, etc.).
# - Episodes: The number of episodes in the anime.
# - Aired: The dates when the anime was aired.
# - Premiered: The season and year when the anime premiered.
# - Status: The status of the anime (e.g., Finished Airing, Currently Airing, etc.).
# - Producers: The production companies or producers of the anime.
# - Licensors: The licensors of the anime (e.g., streaming platforms).
# - Studios: The animation studios that worked on the anime.
# - Source: The source material of the anime (e.g., manga, light novel, original).
# - Duration: The duration of each episode.
# - Rating: The age rating of the anime.
# - Rank: The rank of the anime based on popularity or other criteria.
# - Popularity: The popularity rank of the anime.
# - Favorites: The number of times the anime was marked as a favorite by users.
# - Scored By: The number of users who scored the anime.
# - Members: The number of members who have added the anime to their list on the platform.
# - Image URL: The URL of the anime's image or poster.

# %%
# Import necessary libraries
import numpy as np
import pandas as pd



# %%
df = pd.read_csv('anime-dataset-2023.csv')

# %%
df.head()

# %%
df.shape

# %%
# removing the anime that have unknown genres
df = df[df['Genres'] != 'UNKNOWN']

# %%
df.shape

# %%
# removing the anime that have unknown Score
df = df[df['Score'] != 'UNKNOWN']

# %%
df.shape

# %%

df = df[df['Genres'] != 'Hentai']

# %%
df.shape

# %%
df.isna().sum()

# %% [markdown]
# 

# %%
## Popularity Based Recommender System
popular_df = df[['Name','English name', 'Score', 'Popularity','Favorites', 'Genres', 'Image URL']]

# %%
df.head()

# %%
popular_df.head()


# %%
popular_df.rename(columns = {'Score': 'Rating'}, inplace = True)

# %%
# popular_df['Rating']= popular_df['Rating'].astype(float)
popular_df = popular_df[popular_df['Popularity']<=2000]

# %%
popular_df

# %%
top_50 = popular_df.sort_values('Favorites', ascending = False).head(50)

# %%
top_50.iloc[0]['Image URL']

# %%
import pickle

# %%
with open('top_50.pkl', 'wb') as f:
    pickle.dump(top_50, f)

# %%
df

# %%
#Content Based Recommender System
#anime_id 
#Name
#English name
#Score
#Genres
#Synopsis
#Type
#Producers
# Studios
#Image URL



# %%
r_df = df[['anime_id', 'Name', 'English name', 'Score', 'Genres', 'Synopsis', 'Type', 'Producers', 'Studios','Image URL']]

# %%
r_df.head()

# %%
r_df['Genres'].unique()


# %%


# %%



# %%

r_df['Genres']= r_df['Genres'].apply(lambda x: [x.replace(' ','')])
r_df['Synopsis']= r_df['Synopsis'].apply(lambda x: [x.replace(' ',' ')])
r_df['Type']= r_df['Type'].apply(lambda x: [x.replace(' ','')])
r_df['Producers']= r_df['Producers'].apply(lambda x: [x.replace(' ','')])
r_df['Studios']= r_df['Studios'].apply(lambda x: [x.replace(' ','')])

# %%
r_df.head()

# %%
r_df['tags'] = r_df['Genres'] + r_df['Synopsis'] + r_df['Type'] + r_df['Producers'] + r_df['Studios']

# %%
r_df

# %%
new_df = r_df[['anime_id', 'Name', 'tags', 'Image URL']]

# %%
new_df.head()

# %%
new_df['tags'] = new_df['tags'].apply(lambda x: ' '.join(x))

new_df['tags']= new_df['tags'].apply(lambda x: [x.replace(',',' ')])


# %%
new_df['tags'] = new_df['tags'].apply(lambda x: ' '.join(x))

# %%
new_df.head()

# %%
new_df['tags'][20]

# %%
new_df['tags']=new_df['tags'].apply(lambda x: x.lower())

# %%
new_df['tags'][20]

# %%
import nltk

# %%
from nltk.stem import PorterStemmer
ps = PorterStemmer()

# %%
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return ' '.join(y)

# %%
new_df['tags'] = new_df['tags'].apply(stem)

# %%
from sklearn.feature_extraction.text import CountVectorizer


# %%
cv = CountVectorizer(max_features = 5000, stop_words = 'english')

# %%
vectors = cv.fit_transform(new_df['tags']).toarray()

# %%
vectors

# %%
vectors[0].shape

# %%
list(cv.get_feature_names_out())[:100]

# %%
from sklearn.metrics.pairwise import cosine_similarity

# %%
similarity = cosine_similarity(vectors)

# %%
similarity[1]

# %%
def recommend(anime):
    anime_index = new_df[new_df['Name'] == anime].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:11]
    for i in anime_list:
        print(new_df.iloc[i[0]].Name)
    
    

# %%
recommend('Naruto')

# %%
recommend('One Piece')

# %%
import pickle

# %%
with open('anime.pkl', 'wb') as f:
    pickle.dump(new_df, f)

# %%
with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

# %%
new_df[new_df['Name']=='Naruto']['Image URL']

# %%



