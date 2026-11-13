import streamlit as st
import numpy as np
import pandas as pd
from streamlit_navigation_bar import st_navbar
from datetime import datetime


def save_to_history(geb_typ_1, anzahl_geb_1, geb_typ_2, anzahl_geb_2, geb_typ_3, anzahl_geb_3, geb_typ_4, anzahl_geb_4):

    if "history" not in st.session_state:
        st.session_state.history = []
    entry = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Gebäudetyp 1": geb_typ_1 if geb_typ_1 else "Kein Eingabe",
        "Anzahl 1": anzahl_geb_1 if anzahl_geb_1 else 0,
        "Gebäudetyp 2": geb_typ_2 if geb_typ_2 else "Keine Eingabe",
        "Anzahl 2": anzahl_geb_2 if anzahl_geb_2 else 0,
        "Gebäudetyp 3": geb_typ_3 if geb_typ_3 else "Keine Eingabe",
        "Anzahl 3": anzahl_geb_3 if anzahl_geb_3 else 0,
        "Gebäudetyp 4": geb_typ_4 if geb_typ_4 else "Keine Eingabe",
        "Anzahl 4": anzahl_geb_4 if anzahl_geb_4 else 0
    }
    st.session_state.history.append(entry) 

    # st.session_state.history.append(entry)

def run():
    st.title("Historie")
    if "history" in st.session_state and st.session_state.history:
        history_df = pd.DataFrame(st.session_state.history)
        st.table(history_df)
    else:
        st.write("Kein Historie zur Verfuegung.")


