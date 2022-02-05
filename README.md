# Most Common Words

I find languages quite interesting, and I have spent some time learning foreign languages. When starting a new language, I have found that an effective way to increase your vocabulary in a new language is to study the top *x* words in the target language. For example, you may start with the top *100* words, then increase to *300* words, then *500* words, and so on.

There are websites that provide this information, but I thought it would be fun to collect some data myself. This project uses Twitter API with the Python library, `Tweepy`, to collect tweets from selected Twitter accounts and extract the most common words from those tweets. 

## Process
The process is split into three separate iPython notebooks:
- Tweet Collection
    - We collect the tweets using the `Tweepy` library
- Data Cleaning
    - Tweets contain characters, symbols, and emojis that we do not want for the analysis
        - For example, _'RT', '#', '@'_, links, etc.
    - In this notebook, we remove all the unnecessary characters from the data
- Common Words
    - We create a Word Cloud for each language
    - We also create a DataFrame of the document-term matrix
    - To get the most common words, we sort the data by the word frequency in descending order

## Streamlit Web App
After we collect the data in the iPython notebooks, we create a [web application](https://share.streamlit.io/johng034/language-tweets/app.py) using the `Streamlit` library.

In the web app:
- The user chooses a language and the number of words
- A Web Cloud and a table with their selection of words are displayed

## Improvements
I'm interested in the outout of words for some of the languages. I hypothesis that the accounts I collected tweets from are not a diverse representation of the languages. I am working on selecting different accounts for the data collection to test my hypothesis. 
