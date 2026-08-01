import pandas as pd
import numpy as np
# load the dataset
df = pd.read_csv(r"D:\PROJECT\NETFLIX_DATA_ANALYSIS\dataset\netflix_titles.csv", encoding="utf-8")

# Analyze the dataset
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

# print the number of row of missing values
print(df.isnull().sum())

# Fill the missing value with the unknown
df['director'] = (df['director'].fillna('Unknown').str.strip().str.title())
df['cast'] = (df['cast'].fillna('unknown').str.strip())
df['country'] = (df['country'].fillna('unknown').str.strip().str.title())

# delete missling data if not required
# df.dropna(subset=['date_added'], inplace=True)

# Remove the extra space in the formate
df['date_added'] = df['date_added'].str.strip()  
# convert august 14,2026 into 2026-07-14 
df['date_added'] = pd.to_datetime(df['date_added'], errors="coerce")
df.dropna(subset=['date_added'], inplace=True)
# this is used for finding the most frequently rate used
print(df['rating'].mode())
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

#show only where the duration is missing
df[df['duration'].isnull()]  
#show only where the duration is missing
df.dropna(subset=['duration'], inplace=True)

# for handling the duplicates
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

print(df.isnull().sum())

# instead storing the entire date we can  seprate it.
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month_name()
df['day_added'] = df['date_added'].dt.day

CURRENT_YEAR = 2026
df['content_age'] = (CURRENT_YEAR - df['release_year'])

print(df.info())
# save the cleaned files
df.to_csv(r"D:\PROJECT\NETFLIX_DATA_ANALYSIS\output\netflix_cleaned.csv", index=False)
df.to_exel(r"D:\PROJECT\NETFLIX_DATA_ANALYSIS\output\netflix_cleaned.xlsl", index=False)

