import streamlit as st
from PIL import Image
from pathlib import Path


def show_team_image(path, size):
    """Show a team photo if available; otherwise show an informative placeholder."""
    if not Path(path).is_file():
        st.info("Teamfoto nicht verfügbar.")
        return
    try:
        with Image.open(path) as image:
            st.image(image.resize(size))
    except OSError:
        st.warning("Teamfoto konnte nicht geladen werden.")

def run():

    # 1st title
    st.title("Schön dich zu sehen 👋🏼")

    # mission statement
    st.header("Wir sind Gruppe B,")
    st.write(
        """
        Unsere Mission ist es, unseren Kunden – einen führenden Akteur im Bereich 
        erneuerbarer Energien – bei der Erweiterung von Fernwärmenetzen in 
        Norddeutschland zu unterstützen. Mit fortschrittlichen Optimierungstools
        fördern wir eine effiziente Energiesystemplanung und eine präzise stündliche 
        Energieoptimierung für nachhaltiges Wachstum.
        """
    )

    # team Mitglieder
    st.header("Meet the Team 🚀")

    # Martin
    st.header("Martin")
    st.subheader("Product Owner")
    col1, col2 = st.columns([1, 2])
    with col1:
        martin_path = "project_images/martin_picture.jpeg"
        show_team_image(martin_path, (200, 300))
    with col2:
        st.write(
            """
            Servus, ich bin der Martin.
            Ich studiere Data Science im fünften Semester, lese sehr gerne Romane
            und liebe es auf alte Art und Weise Musik zu machen.

            Meine Rolle in diesem Projekt ist der Product Owner und ich wirke bei der
            Tool-Entwicklung mit.
            """
        )

    st.markdown("---")

    # Murvet
    st.header("Mürvet")
    st.subheader("Scrum Master")
    col1, col2 = st.columns([1, 2])
    with col1:
        murvet_path = "project_images/muervet_picture.jpeg"
        show_team_image(murvet_path, (200, 250))

    with col2:
        st.write(
            """
            Ich bin Mürvet und meine Rolle als Scrum Master im Projekt ist es,
            die Entwicklung der Gruppe B durch die Steigerung der Zusammenarbeit und
            Effizienz sicherzustellen. Mit den Beiträgen des gesamten Teams ist dieses
            Projekt nun bei Ihnen!

            In meiner Freizeit liebe ich es, neue Dinge zu lernen und zu erforschen.
            Ich bin auch als Bücherwurm bekannt 🙂
            """
        )

    st.markdown("---")

    # Olti
    st.header("Olti")
    st.subheader("Entwickler")
    col1, col2 = st.columns([1, 2])
    with col1:
        olti_path = "project_images/olti_picture.jpeg"
        show_team_image(olti_path, (200, 250))
    with col2:
        st.write(
            """
            Mein Name ist Olti Gashi, ich studiere Data Science in 5. Semester an der THI.
            Ich liebe es, Daten zu analysieren und innovative Lösungen zu entwickeln.
            """
        )
    st.markdown("---")

    # Nillab
    st.header("Nillab")
    st.subheader("Entwicklerin")
    col1, col2 = st.columns([1, 2])
    with col1:
        nillab_path = "project_images/nillab_picture.jpeg"
        show_team_image(nillab_path, (250, 200))
    with col2:
        st.write(
            """
            Ich bin Nillab und studiere Data Science. Als Entwicklerin ist es meine Aufgabe,
            die Homepage zu erstellen und euch einen Überblick zu unserem Tool zu geben.
            Ich reise gerne, da ich es liebe neue Länder, Menschen und Kulturen kennenzulernen und
            mich auf einer persönlichen Ebene weiterzuentwickeln
            """
        )
    st.markdown("---")

    # Anabelle
    st.header("Anabelle")
    st.subheader("Entwicklerin")
    col1, col2 = st.columns([1, 2])
    with col1:
        abel_path = "project_images/anabelle.jpeg"
        show_team_image(abel_path, (200, 250))
    with col2:
        st.write(
            """
            Ich bin Anabelle aus Data Science 3. Ich bin verantwortlich für die Seite, die du jetzt geöffnet hast.
            Meine Rolle in diesem Projekt ist die Erstellung von diesem Page und auch als einer der Tool-Entwickler(in).
            Neue Matcha- und Kaffeespots auszuprobieren ist eigentlich mein Lebenspassion.
            """
        )
