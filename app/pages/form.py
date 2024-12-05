import streamlit as st
import pandas as pd
import os

# Ruta al archivo CSV
FILE_PATH = "./app/data/responses.csv"

if not os.path.exists(FILE_PATH):
    df = pd.DataFrame(columns=[
        "Nombre", "Edad", "Género", "Ocupación", "Último nivel de estudios",
        "Respuesta1", "Respuesta2", "Respuesta3", "Respuesta4", "Respuesta5",
        "Respuesta6", "Respuesta7", "Respuesta8", "Respuesta9", "Respuesta10"
    ])
    df.to_csv(FILE_PATH, index=False)



st.title("Formulario de Evaluación SUS")
st.write("Aquí los usuarios pueden responder las preguntas.")

# Definir preguntas SUS
questions = [
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

# Formulario de preguntas
with st.form("sus_form"):
    name = st.text_input("Nombre:")
    age = st.number_input("Edad:", min_value=17, max_value=120, step=1)
    gender = st.selectbox("Género:", ["Masculino", "Femenino", "Otro"])
    occupation = st.selectbox(
        "Ocupación:",
        ["Sin Ocupacion", "Estudiante", "Empleado sector privado","Empleado sector Publico", "Independiente" ,"Empresario", "Jubilado" ]
    )

    # Último nivel de estudios
    education = st.selectbox(
        "Nivel_de_estudios:",
        ["Sin estudios", "Educacion Basica y Media", "Licenciatura", "Maestría", "Doctorado"]
    )

    st.write("**Responde las siguientes preguntas:**")
    responses = []
    for i, question in enumerate(questions, start=1):
        response = st.radio(
            f"{i}. {question}",
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: [
                "Totalmente en desacuerdo",
                "En desacuerdo",
                "Neutro",
                "De acuerdo",
                "Totalmente de acuerdo",
            ][x - 1],
            key=f"question_{i}",
        )
        responses.append(response)

    submitted = st.form_submit_button("Enviar Respuestas")


if submitted:
    # Calcular puntaje SUS
    odd_sum = sum(responses[i] for i in range(0, len(responses), 2)) - 5
    even_sum = sum(responses[i] for i in range(1, len(responses), 2))
    even_sum = 25 - even_sum
    sus_score = (odd_sum + even_sum) * 2.5

    # Guardar datos en un archivo CSV
    new_data = {
        "Nombre": name,
        "Edad": age,
        "Género": gender,
        "Ocupación": occupation,
        "nivel de estudios": education,
        **{f"Respuesta{i+1}": responses[i] for i in range(len(responses))},
        "SUS_Score": sus_score,
    }

    df = pd.read_csv(FILE_PATH)
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)

    # Mostrar mensaje de éxito
    st.success("¡Respuestas enviadas correctamente!")
    st.write(f"**Tu puntaje SUS es:** {sus_score:.2f}")