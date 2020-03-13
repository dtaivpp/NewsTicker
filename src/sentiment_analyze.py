from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    return score

if __name__=="__main__":
    test_txt = "(For a live blog on the U.S. stock market, click or type LIVE/ in a news window) \
                * Energy stocks, banks set to lead rebound \
                * Trump's news conference due on Tuesday \
                * Futures up: Dow 2.99%, S&P 2.97%, Nasdaq 3.14% (Adds comments, details) \
                By Sanjana Shivdas and Medha Singh \
                March 10 (Reuters) - Wall Street was set for strong opening gains on Tuesday, with the Dow Jones on track to recover almost half its losses from a day earlier on hopes of coordinated policy easing to avert a global recession.\
                The three main U.S. stock indexes plunged more than 7% on Monday, the 11th anniversary of the market's longest bull run, as oil prices plummeted following pledges by top producers Saudi Arabia and Russia \
                to increase output in an over-supplied market. \
                The selloff was so sharp it triggered trading halts put in place in the wake of 1987's \"Black Monday\" crash, with the blue-chip Dow Jones shedding as much as 2,000 points and the indexes slipping toward a bear market. \
                Sentiment recovered on Tuesday on signs of further monetary easing to shore up the economy. Traders now expect the Federal Reserve to cut interest rates for a second time this month, while Japan unveiled \
                a $4 billion package to combat the coronavirus outbreak. \
                \"Investors are trying to look for any signs that there is light at the end of the tunnel,\" said Adam Sarhan, chief executive officer of 50 Park Investments in New York. \
                \"If they get any sign that this coronavirus is not as devastating economically, then this market can rip higher.\" \
                At 8:51 a.m. ET, Dow e-minis were up 713 points, or 2.99%. S&P 500 e-minis were up 81.5 points, or 2.97% and Nasdaq 100 e-minis were up 249.5 points, or 3.14%. \
                S&P futures briefly hit a 5% upper trading limit in early deals. \
                If the S&P 500 rose 5%, it would be the first time since the current bull market began in 2009. \
                President Donald Trump gives a news conference on Tuesday, a day after he promised \"major\" steps to combat the virus outbreak and said he would discuss a payroll tax cut with congressional Republicans.   \
                The CBOE Volatility index, a gauge of investor anxiety, slipped about six points to 48.37, after closing at its highest levels since the financial crisis.\
                Oil also recouped some losses from its biggest one-day decline since the Gulf War in 1991, supported by expectations for a settlement to the price war and potential U.S. output cuts.\
                Exxon Mobil Corp and Chevron Corp climbed more than 6% in premarket trading, while Occidental Petroleum Corp, Apache Corp and Marathon Oil Corp jumped between 20% and 32%.\
                American Airlines rose 4.5%, echoing broader market sentiment even as the carrier suspended its full-year results forecast on the virus impact on demand, but said a fall in fuel prices was expected to drive about $3 billion in 2020 cost savings. \
                Shares of U.S. banks including Bank of America Corp, Citigroup Inc, JPMorgan Chase & Co, Goldman Sachs , Wells Fargo & Co and Morgan Stanley were up between 4.2% and 5.8%. \
                The S&P banks index fell about 14.2% on Monday, in its worst day since April 2009, as the yield on the U.S. 10-year Treasury slid to a record low. (Reporting by Sanjana Shivdas and Medha Singh in Bengaluru; Additional reporting by Thyagaraju Adinarayan in London; Editing by Sriraj Kalluvila)"

    print(analyze(test_txt))