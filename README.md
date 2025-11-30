# 🎬 IMDB Movie Review Sentiment Analysis (RNN + Streamlit)

This project is a **Sentiment Classification Web Application** built using a **Recurrent Neural Network (RNN)** trained on the **IMDB Movie Review Dataset**.  
The app allows users to enter a movie review and instantly predicts whether the sentiment is **Positive** or **Negative** using a deployed TensorFlow model.

---

## 🚀 Live Streamlit App  
🔗 **Deployed Web App:**  
👉 https://moviereviewrnn-kacqwjqyu2uvsqhzhely6x.streamlit.app/

---

## 📌 Features

### 🔥 Real-time Sentiment Prediction  
Instant classification using a trained **SimpleRNN** model.

### 🧠 Official IMDB Word Index  
Uses Keras’ built-in `imdb.get_word_index()` for accurate tokenization.

### 🎨 Interactive Streamlit UI  
Simple, clean, and responsive interface for entering movie reviews.

### 📈 Sentiment + Confidence Score  
Displays both the predicted class and model probability.

### 🛠 Fully Reproducible Pipeline  
Complete flow:  
**Preprocessing → Integer Encoding → Padding → Prediction**

---
## 🧠 About the Model

### 📐 Neural Network Architecture

- **Embedding Layer** (vocab size = 10,000)  
- **SimpleRNN Layer**  
- **Dense Output Layer** with **Sigmoid activation**

### 📊 Dataset: IMDB Movie Reviews  
Trained on the official IMDB dataset:

- Reviews are **integer-encoded**
- Maximum sequence length = **500**
- **Binary sentiment classification**
  - `1` → Positive  
  - `0` → Negative  

---

## 🔍 Text Preprocessing Steps

Before predicting the sentiment, the review goes through these steps:

### 1️⃣ Convert text to lowercase  
Ensures consistency.

### 2️⃣ Remove punctuation and special symbols  
Keeps only alphanumeric characters + spaces.

### 3️⃣ Split text into words  
Basic tokenization.

### 4️⃣ Convert words → integer indices  
Using IMDB’s official `word_index`.

### 5️⃣ Replace unknown words  
Words not in vocabulary become **OOV token = 2**.

### 6️⃣ Apply index shift (+3)  
IMDB identifies:

| Token | Meaning |
|-------|---------|
| 0 | Padding |
| 1 | Start token |
| 2 | OOV token |
| 3+ | Actual words |

### 7️⃣ Pad to length = **500**  
Ensures that the RNN receives a fixed input size.

---

## ▶️ Running the Project Locally

```bash
git clone https://github.com/yourusername/imdb-rnn-sentiment-app.git
cd imdb-rnn-sentiment-app
pip install -r requirements.txt
streamlit run app.py


