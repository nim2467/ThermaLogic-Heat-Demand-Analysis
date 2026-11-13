# ThermaLogic – Interaktive Wärmebedarfsanalyse

[English](README.md) | [**Deutsch**](README.de.md)

## Projektübersicht

ThermaLogic ist eine Streamlit-Anwendung, die im Hochschulmodul **Projekt Wissenschaftliches Arbeiten** als **Gruppenprojekt** entwickelt wurde. Sie ermöglicht die Analyse des kombinierten Raumwärmebedarfs unterschiedlicher Gebäudetypen anhand vorhandener Zeitreihendaten. Nutzende wählen Gebäudetypen und Gebäudeanzahlen aus, visualisieren den aggregierten Wärmebedarf im Zeitverlauf und können die Ergebnisse als CSV herunterladen.

Unterstützt werden Schulen, Krankenhäuser, Einfamilienhäuser und Einzelhandelsgebäude.

## Methodik und Funktionen

1. **Zeitreihendaten einlesen:** Semikolongetrennte CSV-Dateien für vier Gebäudetypen mit Pandas laden und die Spalte `Zeit` als Datum interpretieren
2. **Gebäudekombination auswählen:** Bis zu vier Gebäudetypen und die jeweilige Anzahl festlegen
3. **Wärmebedarf berechnen:** Die Werte in `Raumwaerme` mit der Gebäudeanzahl multiplizieren, die Zeitreihen anhand ihrer Zeitstempel zusammenführen und den gesamten Wärmebedarf (`insgesamt_kWh`) berechnen
4. **Ergebnisse visualisieren:** Den aggregierten Zeitverlauf als interaktives Plotly-Liniendiagramm darstellen
5. **Export und Navigation:** Berechnete Daten als CSV exportieren und die Bereiche Startseite, Dokumentation, Historie und Team aufrufen

## Verwendete Technologien

- Python
- Streamlit
- Pandas
- Plotly Express
- Pillow (PIL)

## Mein Beitrag

Es handelt sich um ein gemeinsam entwickeltes Projekt. **Meine persönlichen Beiträge waren die beiden folgenden Module:**

- **`home.py` – Startseite:** Umsetzung der Streamlit-Startseite, Einführungstexte, zweier Bildbereiche und einer Übersicht der Anwendungsfunktionen.
- **`time_series.py` – Wärmebedarfsanalyse:** Implementierung des Einlesens der vier CSV-Datensätze und der Datumsumwandlung, der Eingaben für Gebäudetyp und Anzahl, der gewichteten Berechnungen, der Zusammenführung der Zeitreihen, des Diagramms für den Gesamtbedarf und des CSV-Exports. Das Modul ruft außerdem die gemeinsam genutzte Historienfunktion auf.

Die übrigen Module und die Gesamtanwendung sind Teil der **Gruppenarbeit** und werden nicht als ausschließlich eigene Leistung ausgegeben.

## Interpretation und Einschränkungen

- Die Anwendung berechnet **Szenarien auf Grundlage vorhandener Zeitreihen**. Der geprüfte Code trainiert oder evaluiert **kein** Prognose- oder Machine-Learning-Modell.
- Die Ergebnisse hängen von den Quelldaten, deren Einheiten und der gewählten Gebäudeanzahl ab.
- Der Code wurde eingesehen, die vollständige Anwendung jedoch noch nicht unabhängig in einer frischen Umgebung ausgeführt und geprüft.

