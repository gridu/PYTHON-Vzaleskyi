import pandas
import os
from matplotlib import pyplot as plt


def top_5_authors(path):
    '''
    Extract top 5 authors from csv
    '''
    authors = pandas.read_csv(path)
    authors.drop_duplicates(inplace=True)
    converted_articles_cnt = pandas.to_numeric(authors['articles_cnt'])
    authors.drop(columns=['articles_cnt'], inplace=True)  
    authors['converted_articles_cnt'] = converted_articles_cnt 
    top5 = authors.nlargest(5, 'converted_articles_cnt')
    return top5


def top_articles_tags(path):
    '''
    Extract top 5 articles from csv
    '''
    articles = pandas.read_csv(path)
    articles.drop_duplicates(inplace=True)
    converted_pub_date = pandas.to_datetime(articles['pub_date'])
    articles.drop(columns=['pub_date'], inplace=True)
    articles['converted_pub_date'] = converted_pub_date
    articles.sort_values(by='converted_pub_date', ascending=False, inplace=True)
    top5 = articles.head()
    tags_freequency = articles['tags'].value_counts()
    top7 = tags_freequency.head(7)
    return top5, top7


def plot_tags(tag_series):
    '''
    Plot 7 most popular tags 
    '''
    tags = tag_series.plot(kind='bar',
                           figsize=(14, 8),
                           title="Top 7 tags")
    tags.set_xlabel("Tags")
    tags.set_ylabel("Frequency")
    plt.show()
   

