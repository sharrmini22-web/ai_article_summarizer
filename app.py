import streamlit as st
from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

# Streamlit app title
st.title("AI Article Summarizer")

# Text area for user input
article_text = st.text_area("Enter the article text here:")

# Button to trigger summarization
if st.button("Summarize"):
    if article_text:
        summary = summarizer(article_text, max_length=130, min_length=30, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
