import streamlit as st
from textblob import TextBlob

st.image('header.png')
st.title("Welcome")

msg = st.text_area("Enter some message here😎")
btn = st.button("check sentiment")
if btn and msg:
    blob = TextBlob(msg)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        st.success("the msg is Positive 😃")
    elif sentiment < 0:
        st.error("the msg is negative 😡")
    else:
        st.warning("the msg is neutral 😑")
# streamlit run webapp/sentiment_analysis.py