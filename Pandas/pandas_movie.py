import pandas as pd
import matplotlib.pyplot as plt

#define users_columns as the three entires we want to read from u.user
users_columns = ['user_id', 'age', 'sex']
#third argument passes in our user_columns as the column names
users = pd.read_csv('movie_lens/u.user', sep='|', names=users_columns, usecols=range(3))

rating_columns = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('movie_lens/u.data', sep='\t', names=rating_columns, usecols=range(3))

movie_columns = ['movie_id', 'title']
movies = pd.read_csv('movie_lens/u.item', sep='|', names=movie_columns, usecols=range(2), encoding="iso-8859-1")

#create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
movie_data = pd.merge(movie_ratings, users)

#now we can work with the DataFrame movie_data

#Top rated movies

#movie_data.groupby('title') -- group data by title (files are grouped by index)
#arange data in descending order (movies with more ratings appear at top)-- show only 20
print("The top rated movies (overall):\n")
print(movie_data.groupby('title').size().sort_values(ascending=False)[:20])

oldies = movie_data[(movie_data.age > 60)]
#get top rated for age: 60+
oldies = oldies.groupby('title').size().sort_values(ascending=False)
#extract movies for teens (could add movie_data.gender=='F') if we wanted teenage girls
teens = movie_data[(movie_data.age > 12) & (movie_data.age < 20)]
#get top rated movies for teens
teens = teens.groupby('title').size().sort_values(ascending=False)

print("The top ten movies for oldies: \n")
print(oldies[:10])
print("The top ten movies for teens: \n")
print(teens[:10])

#now lets copare the ratings by gender
ratings_by_title = movie_data.groupby('title').size()
#avoid movies that have one review, using at least 250 reviews
popular_movies = ratings_by_title.index[ratings_by_title >= 250]

#ratings of the movies selected by gender
#pivot_table(arrange it by...,index should be title, columns should be based on gender)
ratings_by_gender = movie_data.pivot_table('rating', index='title',columns='sex')
print("Rated movies by gender (contains movies that may few have few ratings)\n")
print(ratings_by_gender.head())
print("-----------------------------------------------------------------")

#select movies that are popular (greater then 250)
ratings_by_gender = ratings_by_gender.ix[popular_movies]
top_movies_women = ratings_by_gender.sort_values(by='F', ascending=False)

print("Top rated movies by women \n")
print(top_movies_women.head())

#lets add a new column to our table, which will calulate the differenc between men and women
#ratings

ratings_by_gender['diff'] = ratings_by_gender['M'] - ratings_by_gender['F']
gender_diff = ratings_by_gender['diff']
#only get absolute value
gender_diff = abs(gender_diff)

#sort by descedning size -- biggest differences show up on top
gender_diff.sort_values(inplace=True, ascending = False)
gender_diff[:10].plot(kind='barh')
#plt.show()
plt.savefig('gender_diff_movies.png', bbox_inches='tight')
plt.close("all")
