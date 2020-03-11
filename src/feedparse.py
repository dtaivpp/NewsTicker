import feedparser
from util.future_call import Future

hit_list = [ "https://rss.nytimes.com/services/xml/rss/nyt/US.xml", 
             "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml", 
             "https://feeds.a.dj.com/rss/RSSMarketsMain.xml",
             "https://feeds.a.dj.com/rss/RSSWSJD.xml",
             "https://seekingalpha.com/feed.xml" ] # list of feeds to pull down

def query_rss():
    '''Query All RSS Feeds'''
    # pull down all feeds
    future_calls = [Future(feedparser.parse,rss_url) for rss_url in hit_list]
    # block until they are all in
    feeds = [future_obj() for future_obj in future_calls]

    entries = []
    for feed in feeds:
        entries.extend( feed[ "items" ] )
    
    update_db(entries)

def update_db(recordset):
    '''Find which articles are new and send to db'''
    pass

if __name__=="__main__":
    query_rss()