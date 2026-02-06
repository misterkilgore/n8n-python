import re
import os
import requests
import streamlit as st
from dotenv import load_dotenv


# --- GET URL --- #

load_dotenv()
url = os.getenv("N8N_FULL_FLOW")

# --- BUILD FORM --- #

st.title("Acquisizione contatto clienti con full form")

with st.form("client"):
    
    col1, col2 = st.columns(2)
    with col1:
        firstname = st.text_input("Nome")
        telephone = st.text_input("Telefono")

    with col2:
        lastname = st.text_input("Cognome")
        email = st.text_input("Email")

    question = st.text_area("Scrivi qua la tua domanda")

    submit = st.form_submit_button("Invia")

# --- SUBMISSION LOGIC --- #

if submit:

    pattern_telephone = r"^(\+39)?\s?\d{10,13}$"
    pattern_email = 

    if re.match(pattern_telephone, telephone):
        st.success("Numero di telefono valido")
    else:
        st.error("Numero di telefono non valido. Inserisci un numero italiano corretto.")
