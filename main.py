import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.layers import Embedding,SimpleRNN,Dense
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import load_model
import re
model=load_model('model_rnn.h5')

word_index = imdb.get_word_index()
reversed_word_index = {value:key for key,value in word_index.items()}
reversed_word_index


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

def preprocess_text(text, vocab_size=10000):
    text = clean_text(text)
    words = text.split()
    encoded = []

    for word in words:
        index = word_index.get(word, 2)  
        if index >= vocab_size:
            index = 2
        encoded.append(index + 3) 
    
    padded = sequence.pad_sequences([encoded], maxlen=500)
    return padded

st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative.')
   
# User input
user_input = st.text_area('Movie Review')

if st.button('Classify'):

    preprocessed_input=preprocess_text(user_input)

    ## MAke prediction
    prediction=model.predict(preprocessed_input)
    sentiment='Positive' if prediction[0][0] > 0.5 else 'Negative'

    # Display the result
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {prediction[0][0]}')
else:
    st.write('Please enter a movie review.')

