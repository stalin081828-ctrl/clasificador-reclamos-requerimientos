# Clasificador de Reclamos y Requerimientos

## Descripción

Proyecto de Machine Learning para clasificar automáticamente comentarios de solicitudes de clientes en dos categorías:

- Reclamo
- Requerimiento

El modelo utiliza procesamiento de lenguaje natural (NLP) mediante TF-IDF y Regresión Logística para reemplazar un sistema tradicional basado en reglas.

---

## Objetivo del negocio

Automatizar la clasificación de comentarios de solicitudes ingresadas por distintos canales de la empresa, reduciendo errores de clasificación y mejorando la calidad de la información reportada a los entes regulatorios.

---

## Problema de negocio

Actualmente las solicitudes son clasificadas mediante reglas construidas manualmente.

El sistema asigna pesos a determinadas palabras asociadas a reclamos y requerimientos. Sin embargo, conforme cambia el lenguaje utilizado por los clientes, este enfoque pierde precisión

Se busca implementar un modelo de Machine Learning capaz de aprender patrones del texto y mantener un mejor desempeño frente a nuevos comentarios.

---

## Situación Actual (As Is)

- Clasificación basada en reglas duras ejecutada en script de SQL.
- Las reglas consisten en asignación manual de pesos a palabras.
- No existe mantenimiento.
- Disminución de precisión conforme evolucionan los comentarios de los clientes.
- El 95%  de los casos se clasifican correctamente

---

## Solución Propuesta (To Be)

Implementar un clasificador supervisado de texto utilizando técnicas de Procesamiento de Lenguaje Natural (NLP) y Machine Learning.

El modelo aprende automáticamente los patrones presentes en los comentarios y puede generalizar sobre nuevas solicitudes sin depender de reglas manuales.

---

## Modelo utilizado

- TF-IDF
- Logistic Regression

---

## Flujo del proyecto

1. Entendimiento del negocio
2. Comprensión de los datos
3. Análisis Exploratorio (EDA)
4. Preprocesamiento del texto
5. Definición de conjuntos Train, Test y Out Of Time (OOT)
6. Ingeniería de variables mediante TF-IDF
7. Entrenamiento del modelo
8. Validación
9. Evaluación Out Of Time
10. Simulación de producción

---

## Estructura del proyecto

```
clasificador-reclamos-requerimientos/

├── data/
├── notebooks/
├── modelos/
├── resultados/
├── src/
├── imagenes/
├── README.md
└── requirements.txt
```

---

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-Learn
- NLTK
- Matplotlib
- Joblib
- Jupyter Notebook

---
## Dataset

El dataset está compuesto por comentarios de clientes clasificados en dos categorías:

- Reclamo
- Requerimiento

| Característica | Valor |
|----------------|------:|
| Total de registros | 25,857 |
| Reclamos | 13,992 |
| Requerimientos | 11,865 |
| Idioma | Español |

### División de datos

| Conjunto | Descripción |
|----------|-------------|
| Train | Entrenamiento del modelo |
| Test | Evaluación del modelo |
| OOT | Simulación de producción con datos de un periodo posterior |

## Resultados Test
* General
  * Accuracy: 98.81%
  * Precision: 98.81%

* Por umbrales:
  * En 95.35% de los casos se obtiene un accuracy del 99.76%

## Resultados OOT
* General
  * Accuracy: 98.35%
  * Precision: 98.35%

* Por umbrales:
  * En 94.85% de los casos se obtiene un accuracy del 99.77%
## Conclusiones
* El modelo alcanzó una exactitud superior al 98% tanto en el conjunto Test como en la evaluación Out Of Time (OOT), mostrando un desempeño consistente sobre datos no utilizados durante el entrenamiento
* El modelo mejora la exactitud de clasificación en aproximadamente 4 puntos porcentuales respecto al método basado en reglas actualmente utilizado.
* Se recomienda utilizar este modelo como línea base (baseline), comparar su desempeño con algoritmos como SVM, Random Forest o XGBoost, y establecer un proceso periódico de reentrenamiento para mantener su desempeño conforme evolucionen los comentarios de los clientes.

## Consideraciones

* El objetivo del proyecto es demostrar la metodología de construcción de un clasificador de texto para diferenciar solicitudes de distinta naturaleza.
* Aunque el caso utiliza información del sector seguros de salud, el flujo de trabajo (preprocesamiento, TF-IDF, entrenamiento, validación y simulación de producción) es aplicable a problemas similares en banca, seguros y atención al cliente.
* Esta pendiente realizar la comparacion con otros modelos
