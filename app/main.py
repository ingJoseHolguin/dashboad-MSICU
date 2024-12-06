import streamlit as st

st.set_page_config(page_title="Dashboard MSICU", layout="wide")
import streamlit as st

# Título de la aplicación
st.title("Herramienta de Dashboard SUS - Evaluación de Usabilidad")

# Introducción
st.markdown("""
Bienvenido a la **Herramienta de Dashboard SUS**, una plataforma interactiva diseñada para evaluar la usabilidad de sistemas, productos o servicios utilizando la **System Usability Scale (SUS)**. 

Con esta herramienta, puedes aplicar cuestionarios SUS a los usuarios y obtener resultados detallados que te ayudarán a medir tres aspectos clave de la usabilidad:

1. **Eficacia**: ¿Los usuarios pueden alcanzar con éxito sus objetivos?
2. **Eficiencia**: ¿Qué esfuerzo es necesario para alcanzar esos objetivos?
3. **Satisfacción**: ¿Qué tan satisfactorio fue el uso del sistema para los usuarios?

### ¿Cómo funciona?
La herramienta permite crear y administrar cuestionarios SUS fácilmente. Los usuarios responden a **10 afirmaciones** en una escala de Likert (1 a 5) y, al finalizar, se calcula automáticamente un puntaje SUS basado en la fórmula estándar. Los resultados se presentan en gráficos y tablas que te permiten interpretar rápidamente el desempeño de tu sistema, mostrando un puntaje global que te indica si la usabilidad del sistema es **Inaceptable**, **Marginal** o **Aceptable**.

### ¿Qué puedes hacer con los resultados?
- Visualizar las respuestas de los usuarios en tiempo real.
- Obtener una evaluación clara de la usabilidad de tu sistema.
- Identificar áreas de mejora en la experiencia del usuario.

¡Comienza ahora a evaluar la usabilidad de tus sistemas y optimiza la experiencia de tus usuarios con el SUS!
""")


# Título de la aplicación
st.title("Presentación del Sistema SUS (System Usability Scale)")

# Descripción del SUS
st.markdown("""
El **SUS** (System Usability Scale) es una herramienta rápida y sencilla para evaluar la usabilidad de sistemas, productos o tecnologías. Creada por **John Brooke** en 1986 en **Digital Equipment Corporation**, el SUS ha sido utilizado por más de 30 años para medir tres aspectos clave de la usabilidad:

1. **Eficacia**: ¿Los usuarios pueden alcanzar con éxito sus objetivos?
2. **Eficiencia**: ¿Cuánto esfuerzo es necesario para lograr estos objetivos?
3. **Satisfacción**: ¿El uso del sistema fue satisfactorio para los usuarios?

El SUS consta de **10 enunciados** en una escala de **Likert** (1 a 5), y los usuarios deben expresar su acuerdo o desacuerdo con cada afirmación. Los enunciados están divididos en cinco positivos (que se suman directamente) y cinco negativos (que requieren inversión en el puntaje). El cálculo del resultado final implica una fórmula simple en la que:

- Se suman las respuestas de los enunciados impares, restando 5.
- Se suman las respuestas de los enunciados pares y se restan de 25.
- El resultado de ambas operaciones se multiplica por 2.5 para obtener el puntaje final (que no es un porcentaje).

### Resultados y escalas de interpretación:
- **Inaceptable**: 0 a 50
- **Marginal**: 50 a 70
- **Aceptable**: 70 a 100

### Ventajas del SUS:
- **Versatilidad**: Se puede aplicar a cualquier sistema, producto o tecnología.
- **Bajo costo**: No requiere trabajo previo en la redacción de preguntas ni es costoso en cuanto a implementación y análisis.

### Desventajas del SUS:
- No proporciona explicaciones cualitativas de las respuestas.
- Los resultados dependen de la percepción subjetiva de los usuarios.

El SUS es una excelente herramienta para obtener una visión general de la usabilidad de un sistema, pero debe complementarse con métodos cualitativos para obtener un diagnóstico más profundo.
""")