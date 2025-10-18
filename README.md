# 🧠 Tweet Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.24-orange?logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.5.2-green?logo=scikit-learn&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-3.9-yellow?logo=nltk&logoColor=black)

---

## 🔍 Project Overview

**Tweet Sentiment Analysis** is a machine learning project that classifies tweets into **Positive**, or **Neutral** sentiments.  
It uses **Natural Language Processing (NLP)** techniques along with a **Logistic Regression model** for prediction.  

This project is deployed as a **Streamlit web app** for portfolio demonstration.

**Deployed Web App:** [Click Here to View](https://sentiment-analysisnih.streamlit.app/)

---

## 🛠 Features

- ✅ Predict sentiment of individual tweets.
- ✅ Clean and preprocess text using **NLTK**:
  - Lowercasing
  - Stem
  - Tokenization
  - Stopwords removal
  - Punctuation & special characters cleaning
- ✅ Convert text into numerical vectors using **TF-IDF**.
- ✅ Trained **Logistic Regression classifier** for sentiment prediction.
- ✅ Interactive **Streamlit UI** for real-time predictions.

---

## 📈 Workflow

1. **Data Collection**  
   - Dataset is taken from Kaggle | [Dataset Link](https://www.kaggle.com/datasets/kazanova/sentiment140)

2. **Data Preprocessing**  
   - Clean and tokenize text  
   - Remove stopwords and special characters  
   - Convert text into **TF-IDF vectors**  

3. **Model Training**  
   - Logistic Regression classifier is trained on preprocessed data  
   - Model performance evaluated  
   - Trained model saved using `pickle` (`model/tweets-model.pkl`)

4. **Deployment with Streamlit**  
   - Interactive UI 
   - Users can input text and get predicted sentiment 

---

## 📊 Model Evaluation

**Logistic Regression Model Performance:**

| Metric | Score |
|--------|---------|
| Accuracy | 0.77 |
| Precision | 0.75 |
| Recall | 0.79 | 

---

## 🔧 Technologies Used

- Python 3.11
- NLTK - Text preprocessing
- Scikit-learn - Logistic Regression and TF-IDF vectorizer
- Streamlit - Web app deployment
- Pandas & NumPy - Data handling and preprocessing

---

## 📷 Screenshots

<img width="960" height="475" alt="image" src="https://github.com/user-attachments/assets/cf8a47b4-9bff-4f29-b4d9-de7df492e020" />
<img width="959" height="429" alt="image" src="https://github.com/user-attachments/assets/7b9492b4-01a2-409c-a175-6f3eca2f61c5" />



---
⚠️ Note

> This project is exclusively for portfolio demonstration purposes.
> It is not intended for public use or deployment.

