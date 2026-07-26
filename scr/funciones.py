import re
import unicodedata
import pandas as pd
def limpiar_comentario(comentario):
    
    if pd.isna(comentario):
        return ""
    
    #convertir a minuscula
    comentario=str(comentario).lower()

    #quitar numeros re: regular expresion, sub: sustituir, \d: numeros 0-9, +: 1 o mas veces
    comentario=re.sub(r'\d+','',comentario)

    #Quitar signos raros, símbolos y puntuación
    comentario=re.sub(r'[^a-záéíóúñ\s]','',comentario)

    #eliminar espacio en blanco, strip elimina al inicio y fin
    comentario=re.sub(r'\s+',' ',comentario).strip()

    #Eliminar tildes (Normalización Unicode)
    # Descompone caracteres especiales y conserva solo los caracteres base (letras sin tilde)
    #Divide una letra como la á en dos elementos independientes: la letra a y un símbolo invisible que representa la tilde
    comentario = unicodedata.normalize('NFKD', comentario)
    #Convierte el texto a formato ASCII. Como el formato ASCII no acepta símbolos como las tildes invisibles ni la ñ, 
    #el parámetro 'ignore' los borra de inmediato, dejando únicamente la letra base a
    #.decode('utf-8'): Regresa el texto filtrado a su formato normal de Python para que puedas seguir procesándolo.
    comentario = comentario.encode('ascii', 'ignore').decode('utf-8')
    
    return comentario

def quitar_stop_words(comentario,stopwords):
    if pd.isna(comentario):
        return ""
        #separar las palabras del comentario
    palabras=comentario.split()
        #quitar palabras de stopwords
    palabras_limpias=[palabra for palabra in palabras if palabra not in stopwords]
    comentario=" ".join(palabras_limpias)
    return comentario