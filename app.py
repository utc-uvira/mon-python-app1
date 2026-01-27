import streamlit as st

st.title("Mon Application de Bienvenue")

st.write("Hello")

# Utilisation des widgets Streamlit au lieu de input()
nom = st.text_input("Entrez votre nom")
gender = st.radio("Sexe", ["M", "F"])

if nom: # On attend que l'utilisateur ait écrit son nom
    if gender == "F":
        st.success(f"Bonjour Mme {nom}")
    elif gender == "M":
        st.success(f"Bonjour Mr {nom}")
    
    # Petit bonus visuel
    st.balloons()
