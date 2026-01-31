import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv('NetflixData.csv')
print(df.head())


df=df.dropna(subset=['show_id','type','title','director','cast','date_added','release_year','rating','duration','listed_in','description'])

type_count=df['type'].value_counts()
plt.figure(figsize=(6,4))

plt.bar(type_count.index,type_count.values,color=['skyblue','orange'])
plt.title("Number of movies vs TV shows on Netflix")

plt.xlabel("types")
plt.ylabel('count')
plt.tight_layout()
plt.savefig('../netflix_movies _vs_tvshow_plot.png')


#pie chart
rating_counts=df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Percnetage of content rating ")

plt.tight_layout()
plt.savefig('pie_chart_comparison.png')


#HISTOGRAM
movie_df=df[df['type']=='Movie'].copy()
movie_df['duration_int']=movie_df['duration'].str.replace('min','').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='black')
plt.title("Histagram  Distribution movies data")
plt.xlabel("duration")
plt.ylabel('number of moveis')
plt.tight_layout()
plt.savefig('moveis_duration_histogram.png')




plt.show()