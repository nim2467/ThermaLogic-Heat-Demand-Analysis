import streamlit as st
from pathlib import Path

def run():
    # Pfad zum Erklärungs-Videos
    vid_path = "documentation_files/ThermaLogic.mp4"



    # Überschrift der Subpage
    st.markdown("# Dokumentation")


    # Intro: Beschreibung der Anwendung
    st.markdown("""
            ## Beschreibung der Anwendung:
        
            Das Tool **ThermaLogic** dient der Ermittlung 
            des Gesamtwärmebedarfs Ihres gewünschten Einzuggebiets. 
        
            Im folgenden Video wird die korrekte Herangehensweise erklärt.
            """)


    # Trennlinie
    st.markdown("***")


    # 1. Spalten definieren
    col1, col2, col3= st.columns([0.1, 0.8, 0.1])

    # Realisierung der Spalte1 und Bild1: Text zu Bildern
    with col2:
        # Einbetten des Videos
        if Path(vid_path).is_file():
            st.video(vid_path)
        else:
            st.info("Das Erklärungsvideo ist derzeit nicht verfügbar.")


    # Trennlinie
    st.markdown("***")


    # Erklärung der Berechnung der Zeitreihe
    st.markdown("""
            ## Wie kommt unsere Zeitreihe zustande?

            Für jeden Gebäudetyp sind typische Daten hinterlegt, die mittels dem wissenschaftlichen Tool nPro 
            professionell kalkuliert wurden. (Link zum Tool: https://acad.npro.energy/)
            
            Dabei handelt es sich jeweils um einen Datensatz bestehend aus dem Wärmebedarf in Kilowatt
            zur jeweiligen Stunde eines gesamten Jahresverlaufs.
            Hierbei wird von einem Jahr mit 365 Tagen mit jeweils 24 Stunden ausgegangen.
            Somit gibt es insgesamt 8.760 Datenpunkte pro Datensatz.
            
            Wie wird nun die Zeitreihe in ThermaLogic berechnet?
            
            Mit der Eingabe des Gebäudetyps und der jeweiligen Gebäudeanzahl werden die zugrunde liegenden
            Daten miteinander verrechnet. 
            
            Hier ein Beispiel:
            
            - Eingabe des ersten Gebäudetyps: Krankenhaus
            - Eingabe der Anzahl an Krankenhäusern: 1
            - Eingabe des zweiten Gebäudetyps: Schule
            - Eingabe der Anzahl an Schulen: 1
            
            → zur ersten Stunde eines Jahres wurde für den Gebäudetyp **Schule** mittels nPro ein Wärmebedarf von
            56,9 kW ermittelt. Der Gebäudetyp **Krankenhaus** benötigt zu dieser Zeit 35,83 kW Wärme. 
            
            → Nun werden diese beiden Werte summiert und es kommt zu einem Endwärmebedarf von 92,73 kW zu der
            ersten Stunde des Jahres.
            
            Diese Berechnung erfolgt für alle 8.760 Stunden im Jahr und es kommt zur dargestellten Zeitreihe.
            
            Damit können Sie nun Ihren individuellen Wärmebedarf für bis zu vier Gebäudetypen mit einer beliebigen 
            Gebäudeanzahl für ein gesamtes Jahr auf stündlicher Basis einplanen.
            """)









