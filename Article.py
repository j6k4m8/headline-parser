class Article(object):
    """
    a generic article class that holds article information and provides functions
    to process the text of an article (get_keyword_ngrams or someshit)
    """
    # this might have to parse an articles text and deduce the member variables,
    # it all really depends on the format of the article
    def __init__(self, headline, text, datetime):
        # is news source relevant? or will that be implicit?
        self.headline = headline
        self.text = text
        # assert() some sort of datetime format or type?
        self.datetime = datetime

    # are these necessary?
    def get_headline():
        return self.headline

    def set_headline(headline):
        self.headline = headline

    def get_text():
        return self.text

    def set_text(text):
        self.text = text

    def get_datetime():
        return self.datetime

    def set_datetime(datetime):
        self.datetime = datetime
