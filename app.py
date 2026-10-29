import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mohd Furqaan Ahmed", layout="wide")

st.markdown("""
<style>
header, footer {visibility: hidden;}
.block-container {padding: 0 !important; max-width: 100% !important;}
</style>
""", unsafe_allow_html=True)

html = open("index.html", encoding="utf-8").read()

resize = """
<script>
function fit(){
  try{
    window.frameElement.style.height = document.documentElement.scrollHeight + 'px';
  }catch(e){}
}
window.addEventListener('load', fit);
window.addEventListener('resize', fit);
setTimeout(fit, 500);
</script>
"""

components.html(html.replace("</body>", resize + "</body>"), height=3000, scrolling=False)
