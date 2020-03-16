# NewsTicker

News ticker is a tool to track the public opinion of a company. It will use several data sources (Twitter, News, etc.) to gather how the public feels about certain companies. It will then plot these onto either a box and wisker chart or a line chart. 

## Architecture

### Backend

![GitHub Logo](/images/NewsTicker_Backend.png)

1. `feedparse.py` First we poll several RSS feeds to find if we have new articles. If we do we add our new articles to the database. 
2. `download_pages.py` Next we download the content of the pages. The whole request is saved in a pickled file onto disk.  
3. `scrape_page.py` After that we scrape the content with Beatutiful Soup 4. We use a config file to determine where the article content is on the page. 
4. `sentiment_analyze.py` Finally, we use a combination of NLP and sentiment analysis to determine what the page is about and the mood of the article. 


## Developing
Still in the process of making scripts to auto generate test data. Also, in the process of creating mocks for requests. 

#### Install requirements
Install requirements with `pip install -r requirments.txt`

#### Testing 
If you make a function create a test for it right below the originial. Or if you update a file test it/update the tests to ensure it still works. 

```
def return_one():
    return 1

def test_return_one():
    # Assertion statements should have the format: 
    #    assert (True/False Statement), "Output message if False"
    assert return_one() == 1, "Return value outside expected range"
```
Then you can run your test like so `pytest -v path\to\your\file.py` 


## NewsTicker ToDo:

Architecture: 
- MongoDB integration 
- Kafka integration 
- Docker wrapper?

Data Needs:
- Need more article models 
- Stock Symbols and Company Names file 
- Process to create 10 min aggregations 
- Twitter integration 
- Discord integration / bot

Front End: 
- API Planning 
- Page Graphs 
- Filters

FOSS Needs: 
- Unit tests 
- Better development instructions 
- Development environment scripts