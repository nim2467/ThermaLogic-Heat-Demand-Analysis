import streamlit as st
import home, documentation, history, time_series, ueber_uns
from PIL import Image

st.set_page_config(page_title='ThermaLogic', page_icon="📈",layout="wide")

logo = Image.open("logoTL.jpg")
st.image(logo, width=60)

page1, page2, page3,page4, page5 = st.tabs(["🏠Home", "📋Dokumentation", "📉Wärmebedarfsanalyse", "📂Historie", "👥 Über uns"])
with page1:
    home.run()
with page2:
    documentation.run()
with page3:
    time_series.run()
with page4:
    history.run()
with page5:
    ueber_uns.run()