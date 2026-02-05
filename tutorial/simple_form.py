import os
import requests
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv

# --- Variabili d'ambiente --- #

load_dotenv()
n8n_url = os.getenv("N8N_URL")

# --- Request di invio della FORM --- #

def send_data(data):
    try:
        response = requests.post(n8n_url, json=data)
        print("POST Status Code:", response.status_code)
        return response.text
    except Exception as e:
        print("Errore nella POST:", e)
        return "ERROR"

# --- Costruzioni della FORM --- #

st.title("Form Di Ticketing")

introduction = '''
Scriviamo una semplice form di ticketing. Questa form
ci permetterà di aprire semplicissimi ticket, che poi
verranno raccolti su un foglio di Google.
'''

st.write(introduction)

with st.form("my-form"):
    possible_cat = ["Problema tecnico","Problema amministrativo","Altro"]
    category = st.selectbox("Categoria del problema",possible_cat)
    description = st.text_input("Fornisci una descrizione accurata del problema")
    submit = st.form_submit_button("Invia al ticketing")

if submit:
    ticket_data = {
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    st.subheader("Ticket inviato con successo!")
    response = send_data(ticket_data)
    st.write(response)



