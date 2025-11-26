🎬 IMDB Movie Review Sentiment Analysis (RNN + Streamlit)

This project is a Sentiment Classification Web Application built using a Recurrent Neural Network (RNN) trained on the IMDB Movie Review Dataset.
The app allows users to enter a movie review and predicts whether it is Positive or Negative using a deployed TensorFlow model.

🚀 Live Demo 

👉 https://moviereviewrnn-kacqwjqyu2uvsqhzhely6x.streamlit.app/

📌 Features
🔥 Real-time Sentiment Prediction

Uses a trained SimpleRNN model to classify reviews instantly.

🧠 Official IMDB Word Index

Preprocessing uses the official IMDB vocabulary for accurate tokenization.

🎨 Interactive Streamlit Interface

A clean and user-friendly UI for entering movie reviews.

📈 Sentiment + Prediction Score

Displays both binary sentiment and confidence score.

🛠 Fully Reproducible Pipeline

Complete preprocessing → encoding → padding → prediction pipeline.

📂 Project Structure
📦 imdb-rnn-sentiment-app
│
├── model_rnn.h5                 # Trained RNN model
├── app.py                       # Streamlit application
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation

🧠 About the Model
Neural Network Architecture

Embedding layer (vocab_size = 10,000)

SimpleRNN layer

Dense output layer (Sigmoid)

Dataset Details

Trained on the IMDB Movie Review Dataset, where:

Reviews are integer-encoded

Maximum sequence length = 500

Task: Binary sentiment classification

1 → Positive

0 → Negative

🔍 Text Preprocessing Steps

Before predicting sentiment, the user’s input is preprocessed as follows:

1️⃣ Convert Text to Lowercase

Ensures uniformity.

2️⃣ Remove Punctuation & Special Characters

Keeps only alphanumeric characters and spaces.

3️⃣ Split Text into Words

Tokenizes the input sentence.

4️⃣ Convert Words to Integer Indices

Maps each word using IMDB’s official word_index.

5️⃣ Replace Unknown Words

Words not present in the IMDB vocabulary are replaced by the OOV token (2).

6️⃣ Add Index Shift (+3)

IMDB reserves:

0 → padding

1 → start token

2 → OOV token

So actual words start from index 3.

7️⃣ Pad Sequence to Length = 500

Ensures consistent input dimension for the RNN model.
