# Text_Summarizer
Web app summarise the text.

Title
Text Summariser using nlp.


problem statement
 Building a summarization app  using streamlit, spacy,gensim and sumy. 

software used
pycharm ide

Intro
In this project, we will be building a summarization appusing streamlit, spacy,gensim and sumy. The NLP app will consist of two parts.

Summarizer
 Text Extracted from a URL
We will be using displacy from spacy to display our Named Entity in a nice html format on our front end.

Streamlit makes it quite easy to convert our python code into production ready applications. Let us see the basic idea and workflow of our app. The basic workflow of our app includes

Receiving Text Input From User using streamlit st.text_area() and st.text_input() functions
Summarizing our Received Text Using Gensim,Sumy and any other packages such as NLTK or SpaCy.
Extracting Text From a Given URL using BeautifulSoup and Urllib or Request
Entity Recognition using Spacy
Rendering our Extracted Named Entities using Displacy and Streamlit
Algorithm/workflow


First of all we will import our necessary packages

import streamlit as st 

from gensim.summarization import summarize

# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import spacy
from spacy import displacy
nlp = spacy.load('en')

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen
Then we will also have some individual functions to process our text, extract our entities and summarize our text.

# Function for Sumy Summarization
def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result


# Fetch Text From Url
@st.cache
def get_text(raw_url):
	page = urlopen(raw_url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	return fetched_text


@st.cache(allow_output_mutation=True)
def analyze_text(text):
	return nlp(text)
Our Main logic will be in a main function as below.

def main():

    st.title("Best Summary Tool !!")
    activities = ["Summarize for Text", "Summarize For URL"]
    # text1 = st.sidebar.text("Made by dyanesh ♛ ♛")
    choice = st.sidebar.selectbox("Select Activity", activities)



    if choice == 'Summarize for Text':
        st.subheader("Summarize the Document")
        raw_text = st.text_area("Enter Text Here", "Type Here")

        text = st.text("   ")
        summarizer_type = st.selectbox("Summarizer Type", ["Gensim", "Sumy Lex Rank"])

        text = st.text("   ")
        if st.button("Summarize"):
            if summarizer_type == "Gensim":
                summary_result = summarize(raw_text)
            elif summarizer_type == "Sumy Lex Rank":
                summary_result = sumy_summarizer(raw_text)


            st.write(summary_result)
    # NER For URL
    if choice == 'Summarize For URL':
        st.subheader("Analysis on Text From URL")
        raw_url = st.text_input("Enter URL Here", "Type here")
        text_preview_length = st.slider("Length to Preview", 50, 100)
        if st.button("Analyze"):
            if raw_url != "Type here":
                result = get_text(raw_url)
                len_of_full_text = len(result)
                len_of_short_text = round(len(result) / text_preview_length)
                st.success("Length of Full Text::{}".format(len_of_full_text))
                st.success("Length of Short Text::{}".format(len_of_short_text))
                st.info(result[:len_of_short_text])


if __name__ == '__main__':
    main()
To run app simply write 

 streamlit run app.py

