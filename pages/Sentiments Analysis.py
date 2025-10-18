import streamlit as st
import pickle
from txt_preprocess import transform_txt 
import pandas as pd

st.set_page_config(
    page_title = "Tweet Sentiment Analyzer",
    page_icon = "🧠",
    layout = "wide",
)

@st.cache_resource
def load_models():
    with open('model/tweets-model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('model/tfidf.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
    return model, vectorizer

st.markdown("<h3 style='text-align: center;color: white; font-size: 60px; font-family: Modern Sans-Serif;'>🧠 Tweet Sentiment Analysis</h3>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #666;'>Analyze the sentiment of your tweets in real time</p>", unsafe_allow_html=True)

model, vectorizer = load_models()

if "history" not in st.session_state:
    st.session_state.history = []
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

col1, col2 = st.columns([3, 1])
    
with col1:
    user_input = st.text_area(
        "Enter your tweet:",
        placeholder = "Type or paste your tweet here...",
        height = 120,
        label_visibility = "collapsed"
    )
    st.text(f"{len(user_input)} / 300 characters")
    
with col2:
    st.markdown("")
    st.markdown("")
    analyze_button = st.button("🔍 Analyze", use_container_width = True, type = "primary")
    clear_button = st.button("🗑️ Clear", use_container_width = True)

    if clear_button:
        st.session_state.input_text = ""
        st.rerun()

if analyze_button and user_input.strip():
    processed_text = transform_txt(user_input)
    
    vectorized_text = vectorizer.transform([processed_text])

    prediction = model.predict(vectorized_text)[0]
    probabilities = model.predict_proba(vectorized_text)[0]

    threshold = 0.6
    if max(probabilities) < threshold:
        st.markdown("# Neutral / Unsure 😐")
    else:
        col1, col2 = st.columns([2, 1])
        with col1:
            if prediction == 0:
                st.markdown("# Negative Sentiment ☹️")
            else:
                st.markdown("# Positive Sentiment 😊")
            
    st.markdown("---")
    st.markdown("### 📊 Detailed Breakdown")
            
    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
    with metrics_col1:
            st.markdown(f"""
                **Positive Sentiment**
                <h3 style='color: #6c757d; margin: 0;'>{probabilities[1]*100:.1f}%</h3>
                """, unsafe_allow_html=True)
    with metrics_col2:
        st.markdown(f"""
                **Negative Sentiment**
                <h3 style='color: #dc3545; margin: 0;'>{probabilities[0]*100:.1f}%</h3>
                """, unsafe_allow_html = True)
    with metrics_col3:
        st.markdown("**Probability Gauge**")
        st.progress(int(probabilities[1]*100))

    prob_df = pd.DataFrame({
        'Sentiment': ['Negative', 'Positive'],
        'Probability': [probabilities[0]*100, probabilities[1]*100]
    })
    st.markdown("#### Sentiment Probability Chart")
    st.bar_chart(prob_df.set_index('Sentiment'))

    st.session_state.history.append((user_input, prediction))

    st.markdown("## 📜 Recent Analysis")
    with st.container():
        for t, p in reversed(st.session_state.history[-5:]):
            st.markdown(f"**Tweet:** {t}")
            st.markdown(f"**Sentiment:** {'Positive 😊' if p else 'Negative ☹️'}")
            st.markdown("---") 

elif analyze_button and not user_input:
    st.toast("Provide Tweet", icon='⚠️')
            