# TC3002B-Ev1-FaseB

## Descripción
En este repositorio se encuentra el código fuente de la Evidencia 1. Análisis de similitud empleando NLP.

Para la realización de esta evidencia se empleó el lenguaje de programación Python, en el cuál se desarrolló un algoritmo basado en n-gramas para calcular la similitud entre dos textos y de esta forma poder determinar si un texto contiene plagio de otro(s).

## Pre-requisitos
Para poder ejecutar el programa se necesita tener instalado Python 3.8 o una versión superior.

## Instalación

Para instalar las dependencias necesarias para ejecutar el programa, se tiene que ejecutar el siguiente comando en la terminal

<code>pip3 install -r requirements.txt</code>

Igualmente se tiene que ejecutar los siguientes comandos dentro de un ambiente de Python para descargar los recursos necesarios de nltk.

````python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
````

## Utilización

Para poder hacer uso del programa utilizando conjuntos de datos personalizados se tiene que hacer la siguiente modificiación en la estrucutra del proyecto.

En el caso de solamente querer tener un archivo de texto como referencia para comparar, se tiene que agregar este en archivo txt en una ubicación específica.

Por otro lado, si se desean agregar multiples archivos de texto para comparar, se tiene que agregar estos archivos en una carpeta específica.

Finalmente para agregar el o los archivos de texto de referencia, se tiene que modificar el archivo `Main.py` en la línea 50, en la cuál se tiene que cambiar el valor de la variable `reference_file_path` por la ruta del archivo o carpeta que se desea comparar.

### Actualmente 
```python
reference_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Data")
```

### Modificación
```python
reference_file_path = "ruta_del_archivo_o_carpeta"
```

Si se requiere modificar los archivos a evaluar se tiene que modificar de la siguiente manera.

### En el caso de querer evaluar solo un archivo

Se agrega el archivo en una ubicación específica

Se mofiica la línea 51 y 52 del archivo `Main.py` de la siguiente manera.

### Actualmente
```python
evaluate_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "TestData")
result = main.compare_folder(evaluate_file_path
```

### Modificación
```python
evaluate_file_path = "ruta_del_archivo"
result = main.compare(evaluate_file_path)
```

### En el caso de querer evaluar multiples archivos

Se agrega la carpeta con los archivos en una ubicación específica

Se mofiica la línea 51 y 52 del archivo `Main.py` de la siguiente manera.

### Actualmente
```python
evaluate_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "TestData")
result = main.compare_folder(evaluate_file_path)
```

### Modificación
```python
evaluate_file_path = "ruta_de_la_carpeta"
result = main.compare_folder(evaluate_file_path)
```

## Ejecución

Para ejecutar el programa se tiene que ejecutar el siguiente comando en la terminal

<code>python3 Main.py</code>

## Autores
- [José Ángel García Gómez](https://github.com/angel012912)
- [David Damian Galan](https://github.com/a01752785)
- [Luis Humberto Romero Pérez](https://github.com/LHumbertoRom)

