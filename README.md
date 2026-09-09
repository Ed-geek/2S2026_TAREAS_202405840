Universidad San Carlos de Guatemala
Facultad de Ingeniería
Escuela de Ingeniería en Ciencias y Sistemas
Laboratorio - Lenguajes Formales y de Programación - Sección B+
Segundo Semestre 2026

Estudiante: Angel Eduardo Balcárcel Cálderón
Carnet: 202405840
Fecha de entrega: 08/09/2026


📖 Descripción del Proyecto

Este proyecto consiste en la implementación de un analizador léxico funcional que reconoce los tokens de un lenguaje simplificado, utilizando un Autómata Finito Determinista (AFD) como modelo de reconocimiento.

El programa está desarrollado en Python 3 con Programación Orientada a Objetos (POO) y es capaz de:

Leer un archivo de código fuente.

Recorrer el texto carácter por carácter simulando el AFD.

Generar una tabla de tokens con tipo, valor, línea y columna.

Reportar errores léxicos con ubicación exacta.

Manejar espacios, saltos de línea y excepciones de lectura.


Tarea 3/
├── token.py                # Clase Token
├── lexer.py                # Clase Lexer (analizador léxico)
├── main.py                 # Programa principal
├── codigo_valido.txt       # Archivo de prueba (código válido)
├── codigo_errores.txt      # Archivo de prueba (con errores léxicos)
└── README.md               # Este archivo


Ejecución:
Linux: python3 main.py
Windows: python main.py


Ejemplo de entrada y salida:

=== ANALIZADOR LÉXICO ===
Ingrese el nombre del archivo de código: codigo_valido.txt

--- TABLA DE TOKENS ---
Tipo                 Valor                Línea  Columna 
PALABRA_RESERVADA    int                  1      1       
IDENTIFICADOR        suma                 1      5       
SIMBOLO              (                    1      9       
PALABRA_RESERVADA    int                  1      10      
IDENTIFICADOR        a                    1      14      
SIMBOLO              ,                    1      15      
PALABRA_RESERVADA    int                  1      17      
IDENTIFICADOR        b                    1      21      
SIMBOLO              )                    1      22      
SIMBOLO              {                    1      24      
PALABRA_RESERVADA    int                  2      5       
IDENTIFICADOR        resultado            2      9       
OPERADOR             =                    2      19      
IDENTIFICADOR        a                    2      21      
OPERADOR             +                    2      23      
IDENTIFICADOR        b                    2      25      
SIMBOLO              ;                    2      26      
PALABRA_RESERVADA    if                   3      5       
SIMBOLO              (                    3      8       
IDENTIFICADOR        resultado            3      9       
OPERADOR             >                    3      19      
NUMERO               10                   3      21      
SIMBOLO              )                    3      23      
SIMBOLO              {                    3      25      
PALABRA_RESERVADA    return               4      9       
IDENTIFICADOR        resultado            4      16      
SIMBOLO              ;                    4      25      
SIMBOLO              }                    5      5       
PALABRA_RESERVADA    else                 5      7       
SIMBOLO              {                    5      12      
PALABRA_RESERVADA    return               6      9       
NUMERO               0                    6      16      
SIMBOLO              ;                    6      17      
SIMBOLO              }                    7      5       
SIMBOLO              }                    8      1       
PALABRA_RESERVADA    while                9      1       
SIMBOLO              (                    9      7       
IDENTIFICADOR        x                    9      8       
OPERADOR             <                    9      10      
NUMERO               100                  9      12      
SIMBOLO              )                    9      15      
SIMBOLO              {                    9      17      
IDENTIFICADOR        x                    10     5       
OPERADOR             =                    10     7       
IDENTIFICADOR        x                    10     9       
OPERADOR             +                    10     11      
NUMERO               1                    10     13      
SIMBOLO              ;                    10     14      
SIMBOLO              }                    11     1       

✅ No se encontraron errores léxicos.


📌 Conclusiones
El analizador léxico implementado reconoce correctamente las 5 categorías de tokens exigidas: palabras reservadas, identificadores, números, operadores y símbolos.

El uso de un AFD como modelo de reconocimiento permite un control preciso de los estados y transiciones.

El reporte de errores léxicos con línea y columna facilita la depuración del código fuente.

La Programación Orientada a Objetos (clases Token y Lexer) proporciona una estructura clara y modular.

Se manejaron espacios, saltos de línea y excepciones de lectura de archivos de forma adecuada.

El proyecto cumple con todos los requisitos establecidos en la rúbrica y está listo para su entrega.
