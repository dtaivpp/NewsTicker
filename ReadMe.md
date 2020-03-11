# NewsTicker

News ticker is a tool to track the public opinion of a company. It will use several data sources (Twitter, News, etc.) to gather how the public feels about certain companies. It will then plot these onto either a box and wisker chart or a line chart. 

### Architecture

1. `feedparse.py` First we poll several RSS feeds to find if we have new articles. If we do we add our new articles to the database. 
2. `download_pages.py` Next we download the content of the pages. The whole request is saved in a pickled file onto disk.  
3. `scrape_page.py` After that we scrape the content with Beatutiful Soup 4. We use a config file to determine where the article content is on the page. 
4. `nlp.py` Finally, we use a combination of NLP and sentiment analysis to determine what the page is about and the mood of the article. 

