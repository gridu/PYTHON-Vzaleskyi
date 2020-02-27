from pandas import Timestamp, DataFrame, Series
import numpy

articles_dict = {
    'author_f_name': [
        'Aleksey Romanov',
        'Maria Dyuldina',
        'Ilya Katsov',
        'Max Martynov',
        'Eugene Steinberg'
    ],
    'tags': [
        'Search',
        'Search',
        'Data Science', 
        'E-commerce', 
        'Search'
    ],
    'text': [
        'Online retailers are always looking for ways to provide delightful and frictionless shopping experience to their customers. Product discovery, powered by search',
        'Merchandising is an ',
        'Supply chain and price management were among the first areas of enterprise operations that adopted data science and combinatorial optimization methods and have ',
        'Initially, digital transformation for brick-and-mortar retailers meant creating a good customer experience over web and mobile channels. While that started to c',
        'Since the dawn of ecommerce in the end of the nineties, online retailers have coined a famous “If they can’t find ‘em, they can’t buy ‘em” motto, which stands t'
    ],
    'title': [
        'Understanding search query intent with deep learning',
        'How to replatform Endeca rules to Elasticsearch',
        'Deep reinforcement learning for supply chain and price optimization',
        'Unified commerce: Making the most of a true omnichannel experience',
        'Not your father’s search engine: a brief history of retail search'
    ],
    'url': [
        'https://blog.griddynamics.com/understanding-search-query-intent-with-deep-learning/',
        'https://blog.griddynamics.com/how-to-replatform-endeca-rules-to-elasticsearch/',
        'https://blog.griddynamics.com/deep-reinforcement-learning-for-supply-chain-and-price-optimization/',
        'https://blog.griddynamics.com/unified-commerce-making-the-most-of-a-true-omnichannel-experience/',
        'https://blog.griddynamics.com/not-your-fathers-search-engine-a-brief-history-of-retail-search/'
    ],
    'converted_pub_date': [
        Timestamp('2020-02-22 00:00:00'),
        Timestamp('2020-02-18 00:00:00'),
        Timestamp('2020-02-11 00:00:00'),
        Timestamp('2020-02-03 00:00:00'),
        Timestamp('2020-01-23 00:00:00')
    ]
}

authors_dict = {
    'full_name': [
        'Victoria Livschitz',
        'Max Martynov',
        'Eugene Steinberg',
        'Ilya Katsov',
        'Joseph Gorelik'
    ],   
    'job_title': [
        'Founder and EVP of Customer Success',
        'CTO',
        'Principal Architect',
        'Head of Practice, Industrial AI',
        'Data Scientist'
    ],
    'li_url': [
        'https://www.linkedin.com/in/victorialivschitz/',
        'https://www.linkedin.com/company/grid-dynamics',
        'https://www.linkedin.com/in/eugene-steinberg-9bb4884',
        'https://www.linkedin.com/company/grid-dynamics',
        'https://www.linkedin.com/in/joseph-gorelik-8492a7b0'
    ],
    'converted_articles_cnt': [20, 14, 13, 10, 7]   
}

tag_names = ['ML & AI', 'E-commerce', 'Search', 'Mobile', 'Data Science', 'Big Data', 'User Interface']
tag_cnt = [17, 11, 11, 10,  7,  4,  3]


auth_data_frame = DataFrame(data=authors_dict)
# auth_data_frame['new_index'] = [8, 25, 32, 29, 26]
# auth_data_frame.set_index('new_index', inplace=True)
# auth_data_frame.reset_index(drop=True)


articles_data_frame = DataFrame(data=articles_dict)
tag_series = Series(numpy.array(tag_cnt), tag_names)