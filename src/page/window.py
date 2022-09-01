import streamlit as st

def render(words):
    st.title('Word_Remember')
    list(map(st.write, words))

