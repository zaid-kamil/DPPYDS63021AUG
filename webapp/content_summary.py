import streamlit as st
from textblob import TextBlob, Word
import random
st.title("Simple Text Summarizer")
content = st.text_area("Enter some large text data")
btn = st.button("Summarize")
if content and btn:
    nouns = []
    blob = TextBlob(content)
    for word,tag in blob.tags:
        if tag == 'NN':
            nouns.append(word.lemmatize())
    output = []
    for item in random.sample(nouns,5):
        word =  Word(item)
        output.append(word.pluralize())
    output = ", ".join(output)
    st.subheader("the summary is ")
    st.success(output)