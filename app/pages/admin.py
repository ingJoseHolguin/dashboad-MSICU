import streamlit as st
import pandas as pd
import os

# Ruta al archivo CSV
FILE_PATH = "./app/data/responses.csv"

st.title("Administración de Evaluaciones")
st.write("Aquí el administrador puede eliminar cuestionarios.")

if os.path.exists(FILE_PATH):
    # Cargar los datos
    df = pd.read_csv(FILE_PATH)

    # Mostrar los datos
    st.subheader("Resultados Actuales")
    st.dataframe(df)

    # Seleccionar cuestionarios para eliminar
    delete_name = st.selectbox("Selecciona el nombre del cuestionario a eliminar:", df["Nombre"].unique())

    if st.button("Eliminar Cuestionario"):
        df = df[df["Nombre"] != delete_name]
        df.to_csv(FILE_PATH, index=False)
        st.success(f"Cuestionario de {delete_name} eliminado.")
else:
    st.info("No hay cuestionarios para administrar.")