import subprocess
import os
import logging
from extracter import top_5_authors, top_articles_tags, plot_tags


logging.basicConfig(
    # filename='grid_scraper/grid_scraper/spiders/report.log', 
    level=logging.INFO, 
    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s'
)
                    
rel_path = 'grid_scraper/grid_scraper/spiders/'
authors_file_name = 'authors.csv'
articles_file_name = 'articles.csv'
authors_csv = rel_path+authors_file_name
articles_csv = rel_path+articles_file_name


def run_crawler(path, spider_name, file):
    ''' 
    Function checks: if first crawler run then creates file and writes to it,
    otherwise append new data to existing file
    '''
    pwd = os.getcwd()
    os.chdir(path)
    logging.info(f'CRAWLING WITH {spider_name.upper()}')
    if os.path.isfile(file):
        subprocess.call(f'scrapy crawl {spider_name}'.split())
    else:
        subprocess.call(f'scrapy crawl {spider_name} -o {file}'.split())    
    os.chdir(pwd)


def main():
    ''' 
    Main function wich call crawles, extracts searched data and outputs results
    '''
    run_crawler(rel_path, 'authors_spider', authors_file_name)
    run_crawler(rel_path, 'articles_spider', articles_file_name)
    logging.info('PRINTING TOP 5 AUTHORS')
    authors = top_5_authors(authors_csv)
    print(authors)
    logging.info('PRINTING TOP 5 ARTICLES')
    articles, tags = top_articles_tags(articles_csv)
    print(articles)
    logging.info('PLOTING TOP 7 TAGS')
    plot_tags(tags)

    return 0


if __name__ == "__main__":
    main()
