import streamlit as st
import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
# Ruta al archivo CSV
FILE_PATH = "./app/data/responses.csv"

st.set_page_config(
    page_title="Resultados SUS",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Resultados de Evaluación SUS")
st.markdown("**Explora los resultados de las encuestas SUS**")


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

        # Llenar valores nulos
        df["SUS_Score"].fillna(0, inplace=True)
        promedio_sus = df["SUS_Score"].mean()

        # División en columnas
        col1, col2, col3 = st.columns(3)

        # Métricas principales
        col1.metric("Encuestas Contestadas", len(df))
        col2.metric("Puntaje SUS Promedio", f"{promedio_sus:.2f}")
        col3.metric("Máximo Puntaje SUS", f"{df['SUS_Score'].max()}")


        # Crear gráfico de velocímetro del puntaje SUS
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=promedio_sus,
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
        # Añadir leyendas para los rangos
        fig_gauge.add_annotation(
            x=0.25, y=-(0.1),
            text="Inaceptable (0 - 50)",
            showarrow=False,
            font=dict(size=12, color="black"),
            align="center"
        )

        fig_gauge.add_annotation(
            x=0.5, y=-(0.1),
            text="Marginal (50 - 70)",
            showarrow=False,
            font=dict(size=12, color="black"),
            align="center"
        )

        fig_gauge.add_annotation(
            x=0.75, y=-(0.1),
            text="Aceptable (70 - 100)",
            showarrow=False,
            font=dict(size=12, color="black"),
            align="center"
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig_gauge, use_container_width=True)



        # Crear dos columnas
        col1, col2 = st.columns(2)

        # Columna 1: Gráfico de distribución de edades
        with col1:
            fig_age = px.histogram(df, x="Edad", nbins=10, title="Distribución de las Edades", labels={"Edad": "Edad"})
            st.plotly_chart(fig_age, use_container_width=True)

        # Columna 2: Gráfico de distribución de géneros
        with col2:
            fig_pie_gender = px.pie(
                df,
                names="Género",  # Nombre de la columna que contiene los géneros
                title="Distribución de Géneros",
                labels={"Género": "Género"}  # Etiqueta para el gráfico
            )
            st.plotly_chart(fig_pie_gender, use_container_width=True)

        # Crear dos columnas para Ocupación y Nivel de Estudios
        col1, col2 = st.columns(2)

        # Columna 1: Gráfico de distribución de ocupaciones
        with col1:
            fig_occupation = px.bar(
                df,
                x="Ocupación",
                title="Distribución de Ocupación",
                category_orders={
                    "Ocupación": ["Sin Ocupación", "Estudiante", "Empleado sector privado",
                                "Empleado sector público", "Independiente", "Empresario", "Jubilado"]
                },
                labels={"Ocupación": "Ocupación", "count": "Número de participantes"}
            )
            st.plotly_chart(fig_occupation, use_container_width=True)

        # Columna 2: Gráfico de distribución de nivel de estudios
        with col2:
            fig_studies = px.bar(
                df,
                x="Nivel_de_estudios",
                title="Distribución de Nivel de Estudios",
                category_orders={
                    "Nivel_de_estudios": ["Sin estudios", "Educación Básica y Media", "Licenciatura",
                                        "Maestría", "Doctorado"]
                },
                labels={"Nivel_de_estudios": "Nivel de Estudios", "count": "Número de participantes"}
            )
            st.plotly_chart(fig_studies, use_container_width=True)

        preguntas_cols = [
            "Respuesta1", "Respuesta2", "Respuesta3", "Respuesta4", 
            "Respuesta5", "Respuesta6", "Respuesta7", "Respuesta8", 
            "Respuesta9", "Respuesta10"
        ]

        if all(col in df.columns for col in preguntas_cols):
            # Calcular el promedio de las respuestas por pregunta
            promedio_respuestas = df[preguntas_cols].mean()

            # Crear etiquetas del eje X como Q1, Q2, Q3, ...
            etiquetas_x = [f"Q{i+1}" for i in range(len(preguntas_cols))]

            # Crear el gráfico de barras
            fig_barras_promedios = px.bar(
                x=etiquetas_x,  # Etiquetas abreviadas en el eje X
                y=promedio_respuestas,  # Promedios de las respuestas
                labels={"x": "Pregunta", "y": "Promedio de Respuestas"},
                title="Promedio de Respuestas por Pregunta",
                text_auto=True  # Mostrar valores sobre las barras
            )
            fig_barras_promedios.update_layout(
                yaxis=dict(range=[0, 5])  # Establecer el rango del eje Y entre 0 y 5
            )

            # Mostrar el gráfico
            st.plotly_chart(fig_barras_promedios, use_container_width=True)

            legend_text = """
            - Q1: Creo que me gustaría utilizar este sistema con frecuencia  
            - Q2: Encontré el sistema innecesariamente complejo  
            - Q3: Pensé que el sistema era fácil de usar  
            - Q4: Creo que necesitaría el apoyo de un técnico para poder utilizar este sistema  
            - Q5: Encontré que las diversas funciones de este sistema estaban bien integradas  
            - Q6: Pensé que había demasiada inconsistencia en este sistema  
            - Q7: Me imagino que la mayoría de la gente aprendería a utilizar este sistema muy rápidamente  
            - Q8: Encontré el sistema muy complicado de usar  
            - Q9: Me sentí muy seguro usando el sistema  
            - Q10: Necesitaba aprender muchas cosas antes de empezar con este sistema  
            """

            # Mostrar las frases como leyenda
            st.markdown(legend_text)

        else:
            st.error("No se encuentran todas las columnas de respuestas.")
            

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
                # Ajustar la escala del eje Y
                fig_respuesta.update_layout(
                    yaxis=dict(
                        range=[0, 5]  # Establece el rango de la escala de 0 a 5
                    )
                )
                st.plotly_chart(fig_respuesta)
        else:
            st.error("No se encuentran todas las columnas de respuestas.")
                    
    else:
        st.error("El archivo no contiene las columnas 'SUS_Score' o 'Edad'.")
else:
    st.error("El archivo CSV no existe.")