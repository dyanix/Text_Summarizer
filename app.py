import streamlit as st
from gensim.summarization import summarize
from sumy.nlp.tokenizers import Tokenizer
# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer


# NLP
# summary pkgs


# Function for Sumy Summarization
def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result


# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Fetch Text From Url
@st.cache
def get_text(raw_url):
    page = urlopen(raw_url)
    soup = BeautifulSoup(page)
    fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
    return fetched_text

def main():

    st.title("Best Summary Tool !!")
    activities = ["Summarize for Text","Summarize For URL"]
    text1 = st.sidebar.text("Made by dyanesh ♛ ♛")
    text1 = st.sidebar.text("(Mini-Project)")
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
        text_preview_length = st.slider("Length to Preview", 1, 100)
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
