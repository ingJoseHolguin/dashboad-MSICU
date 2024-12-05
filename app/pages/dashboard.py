import streamlit as st
import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
# Ruta al archivo CSV
FILE_PATH = "./app/data/responses.csv"

st.title("Resultados de Evaluación SUS")
st.write("Aquí se mostrarán los resultados de las evaluaciones.")

preguntas = [
    "Creo que me gustaría utilizar este sistema con frecuencia",
    "Encontré el sistema innecesariamente complejo",
    "Pensé que el sistema era fácil de usar",
    "Creo que necesitaría el apoyo de un técnico para poder utilizar este sistema",
    "Encontré que las diversas funciones de este sistema estaban bien integradas",
    "Pensé que había demasiada inconsistencia en este sistema",
    "Me imagino que la mayoría de la gente aprendería a utilizar este sistema muy rápidamente",
    "Encontré el sistema muy complicado de usar",
    "Me sentí muy seguro usando el sistema",
    "Necesitaba aprender muchas cosas antes de empezar con este sistema"
]

if os.path.exists(FILE_PATH):
    df = pd.read_csv(FILE_PATH)

    if "SUS_Score" in df.columns and "Edad" in df.columns:
        # Llenar valores nulos con 0 o cualquier valor predeterminado
        df["SUS_Score"].fillna(0, inplace=True)

        # Mostrar la cantidad de encuestas contestadas
        num_encuestas = len(df)
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 100%; text-align: center;">
                <div>
                    <h3>Encuestas Contestadas</h3>
                    <h1>{num_encuestas}</h1>
                </div>
            </div>
            """, unsafe_allow_html=True
        )

        # Promedio del puntaje SUS
        avg_sus_score = df["SUS_Score"].mean()

        # Crear gráfico de velocímetro del puntaje SUS
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=avg_sus_score,
            title={'text': "Promedio del Puntaje SUS"},
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': "rgba(255, 255, 255, 0.6)"},
                   'steps': [
                       {'range': [0, 50], 'color': "red"},
                       {'range': [50, 70], 'color': "yellow"},
                       {'range': [70, 100], 'color': "green"}
                   ]},
            number={'suffix': " "}
        ))
        st.plotly_chart(fig_gauge, use_container_width=True)

        # Crear gráfico Boxplot para las edades
        fig_box = px.box(df, y="Edad", title="Distribución de las Edades de los Participantes",
                         labels={"Edad": "Edad"})
        st.plotly_chart(fig_box, use_container_width=True)

        fig_age = px.histogram(df, x="Edad", nbins=10, title="Distribución de las Edades",
                        labels={"Edad": "Edad"})
        st.plotly_chart(fig_age)

        fig_pie_gender = px.pie(
            df,
            names="Género",  # Nombre de la columna que contiene los géneros
            title="Distribución de Géneros",
            labels={"Género": "Género"},  # Etiqueta para el gráfico
        )
        st.plotly_chart(fig_pie_gender)

        # OCUPACION Y ESTUDIOS
        fig_occupation = px.bar(
        df,
        x="Ocupación",
        title="Distribución de Ocupación",
        category_orders={
            "Ocupación": ["Sin Ocupacion", "Estudiante", "Empleado sector privado", 
                          "Empleado sector Publico", "Independiente", "Empresario", "Jubilado"]
        },
        labels={"Ocupación": "Ocupación", "count": "Número de participantes"}
        )
        st.plotly_chart(fig_occupation)

        fig_studies = px.bar(
        df,
        x="Nivel_de_estudios",
        title="Distribución de Nivel de Estudios",
        category_orders={
            "Nivel_de_Estudios": ["Sin estudios", "Educacion Basica y Media", "Licenciatura", 
                                  "Maestría", "Doctorado"]
        },
        labels={"Nivel_de_Estudios": "Nivel de Estudios", "count": "Número de participantes"}
        )
        st.plotly_chart(fig_studies)

        preguntas_cols = [
            "Respuesta1", "Respuesta2", "Respuesta3", "Respuesta4", 
            "Respuesta5", "Respuesta6", "Respuesta7", "Respuesta8", 
            "Respuesta9", "Respuesta10"
        ]

        # Asegurarse de que las columnas estén presentes en el DataFrame
        if all(col in df.columns for col in preguntas_cols):
            # Convertir las respuestas a tipo numérico, si no lo están ya
            df[preguntas_cols] = df[preguntas_cols].apply(pd.to_numeric, errors='coerce')

            # Crear un boxplot para cada respuesta
            for i, pregunta in enumerate(preguntas):
                fig_respuesta = px.box(
                    df, 
                    y=preguntas_cols[i],  # Seleccionamos la columna de la respuesta
                    title=f"Distribución de las respuestas a: {pregunta}",
                    labels={preguntas_cols[i]: pregunta}
                )
                st.plotly_chart(fig_respuesta)
        else:
            st.error("No se encuentran todas las columnas de respuestas.")
               
    else:
        st.error("El archivo no contiene las columnas 'SUS_Score' o 'Edad'.")
else:
    st.error("El archivo CSV no existe.")