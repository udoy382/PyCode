# Python Exercise 9 Solution #92

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("News for today... lets begin")
    url = "http://newsapi.org/v2/top-headlines?country=gb&apiKey=29409e84425647eda978d31225bd7a8d"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict["articles"]
    for article in arts:
        speak(article["title"])
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening...")