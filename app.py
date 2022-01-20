from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title='Common Words')

st.title('Most Common Words')
st.markdown("""
            Use the dropdown menu and the slider to find the common words in a language. 
            The data was collected from Twitter using the Tweepy library with Python.

            If you're interested to learn more about this project, here is the [link to the Github repository](https://github.com/johng034/language-tweets).
            """)

df = pd.read_csv('./data/cleaned_data.csv')

# Dropdown menu to choose language
language = st.selectbox('Select a language', options=df.columns)

# Slider to choose the number of words
num_of_words = st.slider('Number of Words', min_value=10, max_value=500, value=100, step=10)

# Read the file containing common words data
language_df = pd.read_csv(f'./data/common_words/{language}_common.csv')
# Set index to start at 1
language_df.set_index(np.arange(1,language_df.shape[0]+1), inplace=True)

## TODO
# Add a download button to save the data as a csv/xlsx file

# Show word cloud
with st.expander('See WordCloud'):
    image = Image.open(f'./wordclouds/{language}_wordcloud.png')
    st.image(image, caption=f'{language} Word Cloud')

# Print table
st.header(f'Top {num_of_words} Most Common {language} Words')
data = language_df['word'][:num_of_words]
st.table(data)
