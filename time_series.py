import pandas as pd
import plotly.express as px
import streamlit as st
from history import save_to_history

def run():
    #Unsere Datensätze--------------------------------------------------------
    file_path1, file_path2, file_path3, file_path4 = 'time_series_data/schule.csv', 'time_series_data/einfamilienhaus.csv', 'time_series_data/krankenhaus.csv', 'time_series_data/einzelhandel.csv'

    schule_data = pd.read_csv(file_path1, delimiter=';')
    schule_data['Zeit'] = pd.to_datetime(schule_data['Zeit'],dayfirst=True)
    school_df = pd.DataFrame(schule_data)

    home_data = pd.read_csv(file_path2, delimiter=';')
    home_data['Zeit'] = pd.to_datetime(home_data['Zeit'],dayfirst=True)
    home_df = pd.DataFrame(home_data)

    krankenhaus_data = pd.read_csv(file_path3, delimiter=';')
    krankenhaus_data['Zeit'] = pd.to_datetime(krankenhaus_data['Zeit'],dayfirst=True)
    krankenhaus_df = pd.DataFrame(krankenhaus_data)

    einzelhandel_data = pd.read_csv(file_path4, delimiter=';')
    einzelhandel_data['Zeit'] = pd.to_datetime(einzelhandel_data['Zeit'],dayfirst=True)
    einzelhandel_df = pd.DataFrame(einzelhandel_data)
    #-------------------------------------------------------------------------

    st.header("Wärmebedarfsanalyse für Deutschland")

    st.markdown('''
    **Bitte füllen Sie die folgenden Felder aus!**
    ''')

    col1, col2, col3, col4 = st.columns(4)
    options = ["Schule", "Einzelhandel", "Krankenhaus", "Einfamilienhaus"]
    selected_values = []

    with col1:
        filtered_options_1 = [opt for opt in options if opt not in selected_values]
        geb_typ_1 = st.selectbox("Gebäudetyp 1:", filtered_options_1, index=None, key="geb_typ_1",
                                 placeholder="Bitte wählen Sie einen Gebäudetyp",)
        anzahl_geb_1 = st.number_input("Anzahl für Gebäudetyp 1:", 0, 5000, key="anzahl_geb_1")
        if geb_typ_1:
            st.write(f"Ausgewählte Anzahl von {geb_typ_1}: {anzahl_geb_1}")
            selected_values.append(geb_typ_1)

    with col2:
        filtered_options_2 = [opt for opt in options if opt not in selected_values]
        geb_typ_2 = st.selectbox("Gebäudetyp 2:", filtered_options_2, key="geb_typ_2", index=None,
                                 placeholder="Bitte wählen Sie einen Gebäudetyp",)
        anzahl_geb_2 = st.number_input("Anzahl für Gebäudetyp 2:", 0, 5000, key="anzahl_geb_2")
        if geb_typ_2:
            st.write(f"Ausgewählte Anzahl von {geb_typ_2}: {anzahl_geb_2}")
            selected_values.append(geb_typ_2)

    with col3:
        filtered_options_3 = [opt for opt in options if opt not in selected_values]
        geb_typ_3 = st.selectbox("Gebäudetyp 3:", filtered_options_3, key="geb_typ_3", index=None,
                                 placeholder="Bitte wählen Sie einen Gebäudetyp",)
        anzahl_geb_3 = st.number_input("Anzahl für Gebäudetyp 3:", 0, 5000, key="anzahl_geb_3")
        if geb_typ_3:
            st.write(f"Ausgewählte Anzahl von {geb_typ_3}: {anzahl_geb_3}")
            selected_values.append(geb_typ_3)

    with col4:
        filtered_options_4 = [opt for opt in options if opt not in selected_values]
        geb_typ_4 = st.selectbox("Gebäudetyp 4:", filtered_options_4, key="geb_typ_4", index=None,
                                 placeholder="Bitte wählen Sie einen Gebäudetyp",)
        anzahl_geb_4 = st.number_input("Anzahl für Gebäudetyp 4:", 0, 5000, key="anzahl_geb_4")
        if geb_typ_4:
            st.write(f"Ausgewählte Anzahl von {geb_typ_4}: {anzahl_geb_4}")
            selected_values.append(geb_typ_4)

#Funktion für Button Herunterladen
    if st.button("Startanalyse"):
        if geb_typ_1 == None and geb_typ_2 == None and geb_typ_3 == None and geb_typ_4 == None:
            st.error("Sie haben keinen Gebäudetyp eingegeben! Bitte wählen Sie mindestens einen Gebäudetyp!")
        else:
            save_to_history(geb_typ_1, anzahl_geb_1, geb_typ_2, anzahl_geb_2, geb_typ_3, anzahl_geb_3, geb_typ_4, anzahl_geb_4)

            st.success("Ihre Wärmebedarfsanalyse wurde erfolgreich erstellt.")

            dataframes = []
            selections = [
                {"typ": geb_typ_1, "anzahl": anzahl_geb_1},
                {"typ": geb_typ_2, "anzahl": anzahl_geb_2},
                {"typ": geb_typ_3, "anzahl": anzahl_geb_3},
                {"typ": geb_typ_4, "anzahl": anzahl_geb_4}
            ]

            for selection in selections:
                geb_typ = selection["typ"]
                anzahl = selection["anzahl"]

                if geb_typ == "Schule":
                    df = school_df.copy()
                    df['Raumwaerme'] = df['Raumwaerme'] * anzahl
                    dataframes.append(df.rename(columns={'Raumwaerme': f'Raumwaerme_{geb_typ}'}))
                elif geb_typ == "Einzelhandel":
                    df = einzelhandel_df.copy()
                    df['Raumwaerme'] = df['Raumwaerme'] * anzahl
                    dataframes.append(df.rename(columns={'Raumwaerme': f'Raumwaerme_{geb_typ}'}))
                elif geb_typ == "Krankenhaus":
                    df = krankenhaus_df.copy()
                    df['Raumwaerme'] = df['Raumwaerme'] * anzahl
                    dataframes.append(df.rename(columns={'Raumwaerme': f'Raumwaerme_{geb_typ}'}))
                elif geb_typ == "Einfamilienhaus":
                    df = home_df.copy()
                    df['Raumwaerme'] = df['Raumwaerme'] * anzahl
                    dataframes.append(df.rename(columns={'Raumwaerme': f'Raumwaerme_{geb_typ}'}))

            if dataframes:
                df_merged = dataframes[0]
                for df in dataframes[1:]:
                    df_merged = pd.merge(df_merged, df, on='Zeit', how='outer')

                df_merged['insgesamt_kWh'] = df_merged[[col for col in df_merged.columns if 'Raumwaerme' in col]].sum(axis=1)
                df_merged = df_merged.sort_values(by='Zeit')

                fig = px.line(df_merged, x='Zeit', y='insgesamt_kWh')
                st.plotly_chart(fig)

                df_csv = df_merged.to_csv(index=False)
                st.download_button("Herunterladen als CSV-Datei", df_csv)


