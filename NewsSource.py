class NewsSource(object):
    """
    A class to hold a single news source, such as an RSS feed or
    simply a manually entered list of article texts.
    """

    def __init__(self, name):
        """
        Constructs a parent class for a generic NewsSource.
        """
        self.articles = []
        self.name = name

class RSSNewsSource(NewsSource):
    """
    A news source that points to an RSS feed
    """

    def __init__(self, name, url):
        """
        url: the web location of the RSS feed where
        articles can be found
        """
        self.url = url
        super(RSSNewsSource, self).__init__(name)

    def check_url(self):
        """
        verifies that self.url points to a real page
        """
        r = requests.get(self.url)
        return r.status_code is 200
