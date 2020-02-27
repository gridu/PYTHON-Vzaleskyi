import scrapy
from ..items import AuthorItem, ArticleItem


domain = 'https://blog.griddynamics.com/'


class AuthorsSpider(scrapy.Spider):
    ''' Crawls authors` data '''
    name = 'authors_spider'
    allowed_domains = ['griddynamics.com']
    start_urls = ['https://blog.griddynamics.com/all-authors/']

    def parse(self, response):
        ''' Parse links reference to athors '''
        self.logger.info('parse function called on %s', response.url)        
        for a in response.css('a.authormore').xpath('@href').getall():
            author_url = domain + a[1:] 
            yield scrapy.Request(author_url, callback=self.parse_author)

    def parse_author(self, response):
        ''' Parse athor`s data'''
        self.logger.info('parse_author function called on %s', response.url)        
        full_name = response.xpath('//*[@id="authorbox"]/div[1]/div[2]/h1/text()')\
                            .extract_first() 
        job_title = response.xpath('//*[@id="authorbox"]/div[1]/div[2]/h2/text()')\
                            .extract_first() 
        li_url = response.xpath('//*[@id="authorbox"]/div[1]/div[2]/div[2]')\
                         .xpath('//a[contains(@class, "linkedin")]/@href')\
                         .extract_first()
        articles_cnt = len(response.xpath('//*[@id="authorbox"]/did').css('a'))

        author_item = AuthorItem()

        author_item['full_name'] = full_name
        author_item['job_title'] = job_title 
        author_item['li_url'] = li_url
        author_item['articles_cnt'] = articles_cnt

        yield author_item


class ArticlesSpider(scrapy.Spider):
    ''' Crawls articles` data '''
    name = 'articles_spider'
    allowed_domains = ['griddynamics.com']
    start_urls = ['https://blog.griddynamics.com/']

    def parse(self, response): 
        ''' Parse links reference to athors '''
        self.logger.info('parse function called on %s', response.url)        
        for a in response.xpath('//article[contains(@class, "regular")]')\
                         .xpath('//a[contains(@class, "img")]/@href')\
                         .re(r'^(?:(?!/tag/).)+$'):
            yield scrapy.Request(domain + a[1:], callback=self.parse_article)

    def parse_article(self, response):
        ''' Parse articles data'''
        self.logger.info('parse_article function called on %s', response.url)        
        title = response.xpath('//*[@id="postcontent"]/h1/text()')\
                        .extract_first()
        url = response.url
        text = response.xpath('//p/text()').extract_first()[:160]
        pub_date = response.xpath('//*[@id="postcontent"]/div[1]/span/text()')\
                           .extract_first()
        author_f_name = response.xpath('//*[@id="postcontent"]/div[2]/div[2]/span/a/span/text()')\
                                .extract_first()
        tags = response.xpath('//*[@id="postcontent"]/div[3]/a/text()')\
                       .extract()

        article_item = ArticleItem()

        article_item['title'] = title
        article_item['url'] = url
        article_item['text'] = text
        article_item['pub_date'] = pub_date
        article_item['author_f_name'] = author_f_name
        article_item['tags'] = tags

        yield article_item

 