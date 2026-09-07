# Análisis Estadístico de la Calidad Seminal

## Descripción

Este repositorio contiene el análisis estadístico de parámetros seminales obtenidos mediante espermogramas realizados en una población de pacientes atendidos en un instituto de reproducción humana del Caribe colombiano durante el período 2017–2025.

El estudio busca caracterizar la calidad seminal de la población analizada, identificar posibles tendencias temporales y explorar diferencias entre períodos, grupos y categorías diagnósticas mediante técnicas de estadística descriptiva e inferencial.

El análisis integra procedimientos de exploración y validación de datos, pruebas estadísticas, clasificación según criterios de referencia de la Organización Mundial de la Salud (OMS) y modelos de regresión para evaluar la relación entre el año de estudio y diferentes parámetros cuantitativos.

## Objetivos

### Objetivo general

Analizar la evolución de los parámetros del espermograma en una población de pacientes atendidos en un instituto de reproducción humana del Caribe colombiano durante el período 2017–2025, caracterizando su distribución, identificando tendencias temporales y explorando diferencias entre grupos y períodos.

### Objetivos específicos

- Explorar y caracterizar la base de datos de espermogramas.
- Evaluar la calidad y distribución de las variables disponibles.
- Analizar variables cualitativas mediante pruebas de asociación y bondad de ajuste.
- Analizar variables cuantitativas mediante estadística descriptiva y pruebas de comparación.
- Evaluar los supuestos estadísticos necesarios para la selección de las pruebas.
- Clasificar los registros según criterios de normalidad establecidos por la OMS.
- Analizar diferentes categorías diagnósticas relacionadas con alteraciones seminales.
- Evaluar la asociación entre el año de estudio y las categorías diagnósticas.
- Comparar los períodos prepandemia y postpandemia.
- Evaluar mediante modelos de regresión el efecto del año sobre diferentes parámetros seminales.

## Enfoque Estadístico

El análisis combina diferentes herramientas de estadística descriptiva e inferencial de acuerdo con la naturaleza de las variables y las características de los datos.

### Variables categóricas

Para las variables categóricas se emplean:

- Tablas de frecuencia.
- Distribuciones porcentuales.
- Pruebas de chi-cuadrado.
- Pruebas de independencia.
- Pruebas de bondad de ajuste.
- Simulación de Monte Carlo cuando los supuestos de las pruebas asintóticas no se cumplen.

Cuando es necesario, se consideran estrategias de agrupación de categorías para garantizar condiciones adecuadas para la inferencia estadística.

### Variables cuantitativas

Para las variables cuantitativas se utilizan:

- Media.
- Mediana.
- Desviación estándar.
- Varianza.
- Rango intercuartílico.
- Percentiles.
- Análisis de distribución.
- Evaluación de normalidad.
- Evaluación de homogeneidad de varianzas.
- Pruebas paramétricas.
- Pruebas no paramétricas.

La selección de cada procedimiento depende de las características de los datos y del cumplimiento de los supuestos estadísticos correspondientes.

## Clasificación de los Registros

Los resultados del espermograma se analizan considerando criterios de referencia establecidos por la Organización Mundial de la Salud (OMS).

A partir de estos criterios se construyen categorías que permiten realizar comparaciones estadísticas entre registros clasificados como:

- Normal.
- Anormal.

Adicionalmente, se consideran categorías diagnósticas específicas relacionadas con alteraciones de los parámetros seminales.

## Análisis Temporal

Uno de los componentes principales del estudio consiste en evaluar la evolución de los parámetros seminales durante el período 2017–2025.

El análisis temporal permite explorar:

- Cambios en las distribuciones de los parámetros.
- Variación de las medidas descriptivas.
- Tendencias en las categorías diagnósticas.
- Asociación entre año y diagnóstico.
- Evolución de los parámetros cuantitativos.

Para el análisis relacionado con la pandemia de COVID-19 se consideran dos períodos principales:

| Período | Años |
|---|---|
| Prepandemia | 2017–2019 |
| Postpandemia | 2021–2025 |

El año 2020 se excluye de esta comparación debido a las características atípicas asociadas al período inicial de la pandemia y las medidas de confinamiento.

## Modelos de Regresión

Para evaluar la relación entre el año de estudio y los parámetros cuantitativos se utilizan modelos de regresión lineal múltiple.

De manera general, el modelo considera:

- Año del estudio.
- Edad del paciente.
- Días de abstinencia.
- Parámetro seminal de interés.

El objetivo es evaluar el efecto independiente del año sobre los parámetros analizados, controlando por posibles variables de confusión disponibles en la base de datos.

Para las inferencias de los modelos se emplean errores estándar robustos HC3, buscando obtener estimaciones más confiables ante posibles problemas de heterocedasticidad.

## Consideraciones Éticas y de Privacidad

Los datos utilizados en este proyecto corresponden a registros relacionados con salud reproductiva.

Por razones de privacidad y protección de datos, no se incluyen datos personales o información que permita identificar directamente a los pacientes en este repositorio.

Los análisis presentados tienen un propósito académico y científico y deben interpretarse dentro del contexto de la población y período estudiados.


## Alcance del Proyecto

Este repositorio constituye una aplicación de estadística y ciencia de datos al estudio de la salud reproductiva masculina, integrando análisis descriptivo, inferencia estadística y modelado para estudiar la evolución de los parámetros seminales en una población del Caribe colombiano.

Los resultados deben interpretarse considerando el diseño del estudio, las características de la población analizada, la disponibilidad de información y las limitaciones inherentes a los datos observacionales.
