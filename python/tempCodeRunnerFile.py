                              #top 10 countries
# country = (df["country"].value_counts().head(10))
# print(country)

# plt.figure(figsize=(10,6))
# country.sort_values().plot(kind="barh", color="#E50914", edgecolor="black")
# plt.title("Top 10 content Producing Countries", fontsize=14, fontweight="bold")
# plt.xlabel("Number of Titles")
# plt.ylabel("Country")
# plt.grid(axis="x", linestyle="--")
# plt.savefig(r"D:\PROJECT\NETFLIX_DATA_ANALYSIS\images\top10Countries.png",dpi=300)
# plt.show()

#                                 #Content Added by Year
# content_year = (df["year_added"].value_counts().sort_index())        
# print(content_year)

# plt.figure(figsize=(10,5))
# content_year.plot(kind="line", color="#E50914", marker="o", linewidth=3)
# plt.title("Content Added by Year", fontsize=14, fontweight="bold")
# plt.xlabel("Year")
# plt.ylabel("Number of Titles")
# plt.grid(True, linestyle="--")
# plt.savefig(r"D:\PROJECT\NETFLIX_DATA_ANALYSIS\images\content_added_year.png",dpi=300)
# plt.show()

#                                  #Top genere
# genre = (df['listed_in']).str.split(",").explode().value_counts().head(10)
# print(genre)

# genre.sort_values().plot(kind='barh', color='#E50914', edgecolor="black")
# plt.title("Top 10 Genres", fontsize=14, fontweight="bold")
# plt.xlabel("Number of Titles")
# plt.ylabel("Genre")
# plt.grid(axis="x", linestyle="--")
# plt.savefig(r"D:\PROJECT\NETFLIX_DATA_ANALYSIS\images\top10genre.png",dpi=300)
# plt.show()

#                                 #Rating Distribution
# rating = df["rating"].value_counts()
# print(rating)

# rating.plot(kind="bar", color="#E50914",edgecolor="black")
# plt.title("Content Rating Distribution", fontsize=14, fontweight="bold")
# plt.xlabel("Rating")
# plt.ylabel("Number of Titles")
# plt.xticks(rotation=45)
# plt.grid(axis="y", linestyle="--")
# plt.savefig(r"D:\PROJECT\NETFLIX_DATA_ANALYSIS\images\rating_distribution.png",dpi=300) 
# plt.show()

#                                 #Top Directors
# top_directors = (df[df["director"] != "Unknown"]["director"].value_counts().head(10))
# print(top_directors)
# plt.figure(figsize=(10,6))

# top_directors.sort_values().plot(kind="barh", color="#E50914", edgecolor="black")
# plt.title("Top 10 Directors", fontsize=14, fontweight="bold")
# plt.xlabel("Number of Titles")
# plt.ylabel("Director")
# plt.grid(axis="x", linestyle="--")
# plt.savefig(r"D:\PROJECT\NETFLIX_DATA_ANALYSIS\images\top_director.png", dpi=300)
# plt.show()

#                                 #Content Age Distribution
# plt.figure(figsize=(10,5))
# plt.hist(df["content_age"], bins=20, color="#E50914", edgecolor="black")
# plt.title("Content Age Distribution", fontsize=14, fontweight="bold")
# plt.xlabel("Content Age (Years)")
# plt.ylabel("Frequency")
# plt.grid(axis="y", linestyle="--", alpha=0.5)
# plt.savefig(r"D:\PROJECT\NETFLIX_DATA_ANALYSIS\images\age_distribution.png", dpi=300)
# plt.show()