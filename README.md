# Calculadora Interactiva en Python

Una calculadora de consola simple y robusta que permite realizar operaciones matemáticas básicas con validación de entradas y manejo de errores.

## Descripción

Este proyecto implementa una calculadora interactiva en Python que permite al usuario realizar operaciones matemáticas básicas (suma, resta, multiplicación y división) de manera continua hasta que decida salir. El programa incluye validación de datos y manejo adecuado de errores.

## Características

- **Operaciones matemáticas básicas:**
  - Suma
  - Resta
  - Multiplicación
  - División (con protección contra división por cero)

- **Validación de entradas:**
  - Verifica que los valores ingresados sean numéricos
  - Manejo de errores para entradas inválidas
  - Protección contra división por cero

- **Interfaz interactiva:**
  - Permite realizar múltiples operaciones consecutivas
  - Menú intuitivo de selección de operaciones
  - Opción para continuar o salir después de cada cálculo

## Estructura del Proyecto

```
M-dulo-7-Calculadora/
│
├── Operaciones.py    # Módulo con las funciones matemáticas básicas
├── main              # Programa principal de la calculadora
├── README.md         # Documentación del proyecto
└── LICENSE           # Licencia del proyecto
```

## Archivos Principales

### [Operaciones.py](Operaciones.py)
Módulo que contiene las funciones matemáticas básicas:
- `sumar(a, b)`: Suma dos números
- `restar(a, b)`: Resta dos números
- `multiplicar(a, b)`: Multiplica dos números
- `dividir(a, b)`: Divide dos números con validación de división por cero

### [main](main)
Programa principal que:
- Implementa la interfaz de usuario interactiva
- Solicita y valida las entradas del usuario
- Ejecuta las operaciones matemáticas
- Maneja errores de manera apropiada

## Requisitos

- Python 3.6 o superior

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/demetriogUIP/M-dulo-7-Calculadora.git
cd M-dulo-7-Calculadora
```

## Uso

Para ejecutar la calculadora, simplemente ejecuta el archivo principal:

```bash
python main
```

### Ejemplo de uso:

```
Calculadora
PorFavor ingresa el primer valor: 10
PorFavor ingresa el segundo valor: 5
Introduce la opción deseada (1, 2, 3 o 4): 1

El resultado de 10.0 + 5.0 es: 15.0
¿Deseas realizar otra operación? (s/n): n
```

### Opciones de operaciones:

- **1**: Suma
- **2**: Resta
- **3**: Multiplicación
- **4**: División

## Manejo de Errores

El programa incluye manejo robusto de errores:

1. **Entradas no numéricas**: Si el usuario ingresa texto en lugar de números, el programa solicita nuevamente el valor sin cerrarse.

2. **División por cero**: Si el usuario intenta dividir por cero, el programa muestra un mensaje de error apropiado y permite continuar.

3. **Opciones inválidas**: Si se selecciona una opción que no existe (diferente de 1, 2, 3 o 4), se muestra un error y se solicita nuevamente la operación.

## Pruebas

Ambos módulos incluyen bloques de prueba que se pueden ejecutar directamente:

```bash
# Probar el módulo de operaciones
python Operaciones.py

# Probar el programa principal
python main
```

## Contribuciones

### Validación de datos - John Roa
- Implementé la validación de entradas numéricas en `main`, evitando que el programa falle cuando el usuario escribe letras u otros símbolos.
- Añadí el manejo de errores al ejecutar las operaciones, incluyendo el control de la división entre cero utilizando la excepción lanzada por `Operaciones.dividir`.
- Incorporé un bucle principal que permite al usuario realizar varias operaciones consecutivas y finalizar la calculadora solo cuando así lo indique.

## Autores

- Equipo de desarrollo UIP - Programación 3
