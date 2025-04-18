import streamlit as st
import google.generativeai as genai
import os

# Configurar la API de Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Título de la aplicación
st.title("Generador de Personajes de Anime con IA")

# Descripción de la app
st.write("""
Esta aplicación permite generar descripciones detalladas de personajes de anime de manera rápida y sencilla. 
Solo necesitas ingresar el nombre, edad, personalidad y rol de tu personaje, y la IA generará una descripción única y creativa.
""")

# Sección "Cómo funciona"
st.subheader("¿Cómo funciona?")
st.write("""
1. **Introduce los detalles del personaje**: Escribe el nombre, edad, personalidad y rol de tu personaje.
2. **Haz clic en 'Generar descripción'**: La IA procesará los datos e generará una descripción detallada.
3. **Revisa la descripción**: Obtendrás una descripción única, que incluye aspectos físicos, personalidad, motivaciones y relaciones con otros personajes.

**Características clave**:
- Generación automática de descripciones.
- Respuestas creativas y únicas basadas en IA.
- Ideal para creadores de anime, guionistas y diseñadores de personajes.
""")

# Entrada de usuario
nombre = st.text_input("Nombre del personaje")
edad = st.text_input("Edad")
personalidad = st.text_area("Personalidad del personaje")
rol = st.text_input("Rol del personaje en la historia")

# Botón de acción para generar la descripción
if st.button("Generar descripción"):
    if nombre and edad and personalidad and rol:
        # Prompt para generar la descripción
        prompt = (
            f"Crea una descripción detallada y original para un personaje de anime llamado {nombre}, "
            f"de {edad} años. Este personaje tiene una personalidad {personalidad} y cumple el rol de {rol}. "
            f"Incluye aspectos físicos, estilo, motivaciones, historia personal y relaciones con otros personajes."
        )
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        # Mostrar la descripción generada
        st.subheader("Descripción generada:")
        st.write(response.text)
    else:
        st.warning("Por favor, completa todos los campos antes de generar la descripción.")
