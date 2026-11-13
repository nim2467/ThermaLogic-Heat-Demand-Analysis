import streamlit as st  # Füge diesen Import hinzu
from PIL import Image

def run():
    st.title("🏠 Willkommen bei ThermaLogic")
    st.subheader("Ihr Begleiter für eine effiziente Wärmebedarfsanalyse")
    st.write(
        """
        Mit ThermaLogic können Sie den Wärmebedarf präzise analysieren, Daten historisch vergleichen und Berichte erstellen. 
        Nutzen Sie die Tabs oben, um mehr zu entdecken!
        """
    )

    # Bildgröße festlegen
    target_size = (400, 200)  # Breite x Höhe (Pixel)

    # Zwei Bilder skalieren
    image1 = Image.open("home_images/waermebild.jpeg").resize(target_size)
    image2 = Image.open("home_images/thermografie.jpeg").resize(target_size)

    # Zwei gleich große Spalten für die Bilder
    col1, col2 = st.columns(2)
    with col1:
        st.image(image1, caption="Energieeffizienz beginnt mit der richtigen Analyse", use_container_width=True)
    with col2:
        st.image(image2, caption="Nachhaltige Lösungen für die Zukunft", use_container_width=True)

    # Übersicht der Funktionen mit Hyperlinks zu Tabs
    st.markdown("### Übersicht der Funktionen")
    st.markdown("""
    - 📋 **Dokumentation**: Hier finden Sie alle wichtigen Informationen zur Funktionsweise des Tools.
    - 📉 **Wärmebedarfsanalyse**: Starten Sie Ihre Analyse und erhalten Sie detaillierte Ergebnisse.
    - 📂 **Historie**: Greifen Sie auf frühere Analysen zurück.
    - 👥 **Über Uns**: Erfahren Sie mehr über unser Team und die Vision.
    """, unsafe_allow_html=True)