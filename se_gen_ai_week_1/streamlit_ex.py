import streamlit as st
from textblob import TextBlob

# Page config
st.set_page_config(page_title="Live Sentiment Analysis", layout="centered")

# Title
st.title("📝 Live Text Sentiment Analysis App")

# Instructions
st.write("""
Enter any text below to analyze its **sentiment polarity and subjectivity** using `TextBlob`.
This is useful for:
- Social media analysis
- Reviews analysis
- NLP pipeline experimentation
""")

# User input
text_input = st.text_area("Enter your text here", height=200)

if st.button("Analyze Sentiment"):
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        blob = TextBlob(text_input)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        st.subheader("Results:")
        st.write(f"**Polarity:** {polarity:.2f} (range: -1 = negative, 0 = neutral, 1 = positive)")
        st.write(f"**Subjectivity:** {subjectivity:.2f} (range: 0 = objective, 1 = subjective)")

        if polarity > 0:
            st.success("The sentiment is Positive 😊")
        elif polarity < 0:
            st.error("The sentiment is Negative 😞")
        else:
            st.info("The sentiment is Neutral 😐")

st.sidebar.title("About")
st.sidebar.info("""
This app demonstrates **live text sentiment analysis** using Streamlit and TextBlob.
Great for practice and learning **NLP + Streamlit** integration for your portfolio projects.
""")
