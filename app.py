import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mohd Furqaan Ahmed", layout="wide")
html = open("index.html", encoding="utf-8").read()
components.html(html, height=2600, scrolling=True)
