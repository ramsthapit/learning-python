import pandas as pd

ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
ratings = pd.merge(movies, ratings).drop(['genres', 'timestamp'], axis=1)

# print(ratings.head())

user_ratings = ratings.pivot_table(index=['userId'], columns=[
                                   'title'], values='rating')

user_ratings = user_ratings.dropna(thresh=10, axis=1).fillna(0)

# print(user_ratings.head())

# lets build our similarity matrix
item_similarity_df = user_ratings.corr(method='pearson')

print(item_similarity_df.head(5))


def get_similar_movies(movie_name, user_rating):
    similar_score = item_similarity_df[movie_name]*(user_rating-2.5)
    similar_score = similar_score.sort_values(ascending=False)

    return similar_score


# print(get_similar_movies("action1", 5))

action_lover = [("Toy Story (1995)", 5), ("Babe (1995)", 1),
                ("From Dusk Till Dawn (1996)", 1)]

similar_movies = pd.DataFrame()

for movie, rating in action_lover:
    similar_movies = similar_movies.append(
        get_similar_movies(movie, rating), ignore_index=True)


similar_movies.sum().sort_values(ascending=False)

print(similar_movies.head(50))
