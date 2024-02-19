import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Import and filter the dataset
dataset = pd.read_csv('movies.csv')
dataset['tags'] = dataset['overview']+dataset['keywords']
dataset.dropna(inplace=True)

# Vectorization of Required Coluumns
cv = CountVectorizer(max_features=10000, stop_words='english')
vector = cv.fit_transform(dataset['tags'].values.astype('U')).toarray()

# Creating similarity matrix (COLLABORATIVE-FILTERING)
similarity = cosine_similarity(vector)

# Class definition of actual code

class Recommendation:
    
    def rectification(self, category, value):
        if category == 'Name':
            return 'original_title', value.capitalize()
        elif category == 'Genre':
            return 'genres', value.capitalize()
        elif category == 'Keyword':
            return 'keywords', value.lower()
        elif category == 'Cast':
            return 'cast', value.capitalize()

    def recommend(self, type_of_search, name):
        movies = []
        try:
            index = dataset[dataset[str(type_of_search)].str.contains(str(name))].index[0]
            distance = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda vector:vector[1])
            for i in distance[:24]:
                movies.append([dataset.iloc[i[0]].id, dataset.iloc[i[0]].original_title, dataset.iloc[i[0]].imdb_id])
            return movies
        except IndexError:
            return None
