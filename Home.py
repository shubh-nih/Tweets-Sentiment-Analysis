import streamlit as st
import pandas as pd

st.set_page_config(layout = 'wide',
                   page_icon = '🧠',
                   page_title = 'Tweet Sentiment Analyzer',
                   initial_sidebar_state = "expanded")

st.markdown("""
    <style>
    .sub-header {
        font-size: 1.2rem;
        color: #6b7280;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html = True)

st.markdown("<h3 style='text-align: center;color: white; font-size: 60px; font-family: Modern Sans-Serif;'>🧠 Tweet Sentiment Analysis</h3>", unsafe_allow_html=True)

st.markdown('<p class="sub-header">Powered By Machine Learning</p>', unsafe_allow_html = True)

st.markdown("---")

st.header("📘 About the Project")
st.write("""
This project analyzes the sentiment of tweets using Machine Learning models.
- **Dataset:** 1.6M tweets (Positive, Negative) | [Dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)
- **Preprocessing:** TF-IDF Vectorization
- **Model:** Logistic Regression
""")
st.write("It allows users to enter any tweet and get a predicted sentiment in real time.")
st.markdown("---")

st.header("🧩 Workflow Overview")
st.markdown("""
        1. Text preprocessing (cleaning, tokenization, removing stopwords)
        2. TF-IDF vectorization of the text
        3. Logistic Regression model training
        4. Model evaluation using metrics like accuracy, precision, recall, and F1-score
            """)

st.markdown("---")

st.header("📊 Model Performance Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Accuracy", "77%")
col2.metric("Precision", "79%")
col3.metric("Recall", "75%")

st.write("Sample sentiment distribution from dataset:")
st.bar_chart({"Positive": 8000, "Negative": 8000})

st.markdown("---")

st.header("🛠️ Tech Stack")
st.markdown("""
**Languages & Tools:**  
Python, Pandas, Scikit-learn, Streamlit

**ML Models Used:**  
Logistic Regression and TF-IDF Text Vectorization
            """)

st.markdown("---")

st.write("""
## 👨‍💻 Developer
**Shubham Bisht** 
""")
st.markdown("📧 [Mail](mailto:shubhambisht149@gmail.com)")
st.markdown("🪪 [LinkedIn](https://www.linkedin.com/in/shubhambisht7/)")
st.caption("© 2025 Tweet Sentiment Analysis Project | Built using Streamlit & Machine Learning")
