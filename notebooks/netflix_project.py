import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


df = pd.read_csv("netflix_titles.csv")
print("✅ Dataset loaded successfully!")

# Basic info
print(df.shape)
print(df.head())

##Data Cleaning
# Check for missing values
print(df.isnull().sum())

# Fill or drop missing values (for simplicity)
df['country'].fillna('Unknown', inplace=True)
df['cast'].fillna('Not Specified', inplace=True)
df['director'].fillna('Not Specified', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)

# Drop rows with missing dates
df.dropna(subset=['date_added'], inplace=True)

#Exploratory Data Analysis (EDA)
sns.countplot(data=df, x='type', palette='Set2')
plt.title("Count of Movies vs TV Shows")
plt.show()

#Top 10 producing countries
top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='coolwarm')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()

#Most popular genres
# Split 'listed_in' column (contains multiple genres)
from collections import Counter

genres = df['listed_in'].dropna().apply(lambda x: x.split(', '))
flat_genres = [genre for sublist in genres for genre in sublist]
top_genres = pd.Series(flat_genres).value_counts().head(10)

sns.barplot(x=top_genres.values, y=top_genres.index, palette='magma')
plt.title("Top 10 Genres on Netflix")
plt.show()




#Content added over the years
df['year_added'] = pd.to_datetime(
    df['date_added'].str.strip(),  # removes leading/trailing spaces
    errors='coerce',               # replaces bad dates with NaT (Not a Time)
    infer_datetime_format=True     # automatically detects date format
).dt.year
yearly = df['year_added'].value_counts().sort_index()

plt.figure(figsize=(10,5))
sns.lineplot(x=yearly.index, y=yearly.values, marker='o')
plt.title("Netflix Titles Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()


# Top 10 Directors with Most Titles
top_directors = df['director'].value_counts().head(10)
sns.barplot(x=top_directors.values, y=top_directors.index, palette='viridis')
plt.title("Top 10 Directors with Most Netflix Titles")
plt.show()

df.to_csv("cleaned_netflix_data.csv", index=False)
print("✅ Cleaned data saved!")