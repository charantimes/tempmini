import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid_object = SentimentIntensityAnalyzer()
    
def analyze(text):
    # sentiment report 
    report = sid_object.polarity_scores(text)
    
    state    = "Neutral"
    if report['compound'] >= 0.05:
        state = "Positive"
    elif report['compound'] <= -0.05:
        state = "Negative"
    
    return {
        "positive" : round(report['pos'] * 100, 2), 
        "negative" : round(report['neg'] * 100, 2), 
        "neutral"  : round(report['neu'] * 100, 2), 
        "state"    : state
    }