from flask import Flask, request, jsonify
import openai
import os
import streamlit as st
app= Flask (__name__)

# Configuramos las claves de API de OpenAI
openai.api_key = 'claveopenai'
os.environ['OPENAI_API_KEY'] = 'claveopenai'

# Defino las categorías para la clasificación
categorias = ["deportes", "politica", "religion"]

# Función para clasificar el texto
def clasificar_texto(texto):
    # Prepara la solicitud a la API utilizando el endpoint de chat
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Clasifica el siguiente texto en una de las siguientes categorías: {', '.join(categorias)}:\n\n{texto}"},
        ]
    )

# Interfaz de usuario con Streamlit
st.title("Clasificador de Temas de Texto")

# Entrada de texto
texto_a_clasificar = st.text_area("Introduce el texto que deseas clasificar:")

# Botón para realizar la clasificación
if st.button("Clasificar"):
    with st.spinner("Clasificando..."):
        # Llama a la función para clasificar el texto
        categoria_resultante, probabilidad_resultante = clasificar_texto(texto_a_clasificar)

    # Muestra el resultado
    st.success(f"La categoría del texto es: {categoria_resultante}")

    #Muestra el mensaje en caso de error en la categoria.
#return jsonify({"code": texto_a_clasificar, "response": "No puedo generar una etiqueta porque solo tengo el entrenamiento en deportes, politíca y religión"})

#respuesta al texto ingresado
#@app.route('/classify', methods=['POST'])
#def classify():
#data = request.json
#code = data.get('code')
#text = data.get('value')

#if code in None or text is None:
    #return jsonify({"error":"Valor no establecido"}), 400



#Configuracion del puerto
if __name__== '__main__':
    app.run(port=8008)

