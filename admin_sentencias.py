import streamlit as st
import pandas as pd
import os

CSV_FILE = "sentencias.csv"

st.title("Administrador de Sentencias")

# Formulario de carga
with st.form("form_sentencia"):
    titulo = st.text_input("Título de la sentencia")
    fecha = st.text_input("Fecha (Ej: 05 de agosto de 2025)")
    descripcion = st.text_area("Descripción")
    url = st.text_input("URL para fallo completo (opcional)")
    enviado = st.form_submit_button("Subir sentencia")

    if enviado:
        nueva = {"Título": titulo, "Fecha": fecha, "Descripción": descripcion, "URL": url}
        if os.path.exists(CSV_FILE):
            df = pd.read_csv(CSV_FILE)
            df = df.append(nueva, ignore_index=True)
        else:
            df = pd.DataFrame([nueva])
        df.to_csv(CSV_FILE, index=False)
        st.success("Sentencia subida exitosamente.")

# Mostrar sentencias existentes
if os.path.exists(CSV_FILE):
    st.subheader("Sentencias cargadas")
    df = pd.read_csv(CSV_FILE)
    st.dataframe(df)
