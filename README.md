#🎬 IMDB Movie Review Sentiment Analysis (RNN + Streamlit)

This project is a Sentiment Classification Web App built using a Recurrent Neural Network (RNN) trained on the IMDB Movie Review Dataset.
The app allows users to enter a movie review and predicts whether it is Positive or Negative using a deployed TensorFlow model.

🚀 Live Demo

👉 Add your Streamlit deployment link here

#📌 Features

🔥 Real-time sentiment prediction using a trained SimpleRNN model

🧠 Uses the official IMDB word index for preprocessing

🎨 Clean and interactive Streamlit interface

📈 Displays both Sentiment and Prediction Score

🛠 Fully reproducible pipeline

#📂 Project Structure
📦 imdb-rnn-sentiment-app
│
├── model_rnn.h5                 # Trained RNN model
├── app.py                       # Streamlit application
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation

#🧠 About the Model

The model consists of:

Embedding layer with vocab_size=10,000

SimpleRNN layer

Dense output layer (Sigmoid)

It was trained on the IMDB movie review dataset where:

Reviews are integer-encoded

Maximum sequence length = 500

Binary classification: Positive (1) / Negative (0)

#🔍 Text Preprocessing Steps

Before predicting sentiment, the input review is processed as follows:

Convert to lowercase

Remove punctuation and special characters

Split into words

Replace each word with its integer index using IMDB's official vocabulary

Replace unknown words with OOV token = 2

Add index shift (+3) as required by the IMDB dataset

Pad the review to a fixed length (500)

This ensures consistency between training and real-time inference.
