import scrapy


class AuthorItem(scrapy.Item):
    full_name = scrapy.Field() 
    job_title = scrapy.Field() 
    li_url = scrapy.Field()
    articles_cnt = scrapy.Field()
    

class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
    pub_date = scrapy.Field()
    author_f_name = scrapy.Field()
    tags = scrapy.Field()
