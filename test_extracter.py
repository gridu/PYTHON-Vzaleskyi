import unittest
import pandas
import numpy
from test_data import auth_data_frame, articles_data_frame, tag_series
from extracter import top_5_authors, top_articles_tags
from pandas.testing import assert_frame_equal


class TestExtracter(unittest.TestCase):
    ''' A class used for testing function output '''
    authors_csv = 'test_authors.csv'
    articles_csv = 'test_articles.csv'

    def test_top_5_authors(self):
        ''' Checks top_5_authors function output '''
        tested_auth_data_frame = top_5_authors(self.authors_csv)
        assert_frame_equal(
            tested_auth_data_frame.reset_index(drop=True), 
            auth_data_frame.reset_index(drop=True)
        )

    def top_articles_tags(self):
        ''' Checks top_articles_tags function output '''
        tested_articles_data_frame, tested_tag_series = top_articles_tags(self.articles_csv)
        assert_frame_equal(
            tested_articles_data_frame.reset_index(drop=True), 
            articles_data_frame.reset_index(drop=True)
        )
        assert_frame_equal(tested_tag_series, tag_series)


if __name__ == '__main__':
    unittest.main()