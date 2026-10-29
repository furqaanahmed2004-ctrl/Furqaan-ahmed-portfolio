import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mohd Furqaan Ahmed", layout="wide")

with open("Mohd Furqaan Ahmed – Data Engineer Portfolio.html", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=2200, scrolling=True)
