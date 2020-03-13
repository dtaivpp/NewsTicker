from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze(text):
    '''Takes text and returns vaderSentiment intensity object'''
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    return score

if __name__=="__main__":
    from util.load_test_data import get_test_text
    
    test_text = get_test_text()
    results = []

    for text in test_text:
        data = text.decode('utf-8')
        results.append(analyze(data))
    
    [print(result) for result in results]