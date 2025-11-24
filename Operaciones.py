"""
Módulo: Operaciones
Descripción: Contiene las funciones básicas de una calculadora:
             sumar, restar, multiplicar y dividir.
"""


def sumar(a, b):
    """
    Suma dos números.

    Parámetros:
        a (float | int): Primer número.
        b (float | int): Segundo número.

    Retorna:
        float | int: Resultado de a + b.
    """
    # Realizar la operación de suma y retornar el resultado
    return a + b


def restar(a, b):
    """
    Resta dos números.

    Parámetros:
        a (float | int): Primer número.
        b (float | int): Segundo número.

    Retorna:
        float | int: Resultado de a - b.
    """
    # Realizar la operación de resta y retornar el resultado
    return a - b


def multiplicar(a, b):
    """
    Multiplica dos números.

    Parámetros:
        a (float | int): Primer número.
        b (float | int): Segundo número.

    Retorna:
        float | int: Resultado de a * b.
    """
    # Realizar la operación de multiplicación y retornar el resultado
    return a * b


def dividir(a, b):
    """
    Divide dos números.

    Parámetros:
        a (float | int): Numerador.
        b (float | int): Denominador.

    Retorna:
        float | int: Resultado de a / b.

    Lanza:
        ValueError: Si b es cero.
    """
    if b == 0:
        # Aquí manejamos el caso especial de división entre cero
        raise ValueError("Error: No se puede dividir entre cero.")
    return a / b


# Bloque de pruebas rápidas (solo se ejecuta si ejecutas este archivo directamente)
if __name__ == "__main__":
    print("Pruebas rápidas del módulo Operaciones:\n")

    # Definir valores de prueba
    x, y = 10, 5

    # Probar cada función con los valores definidos
    print(f"sumar({x}, {y}) = {sumar(x, y)}")
    print(f"restar({x}, {y}) = {restar(x, y)}")
    print(f"multiplicar({x}, {y}) = {multiplicar(x, y)}")

    # Probar la función de división, incluyendo caso de error
    try:
        print(f"dividir({x}, {y}) = {dividir(x, y)}")
        # Intentar dividir por cero para probar el manejo de errores
        print(f"dividir({x}, 0) = {dividir(x, 0)}")
    except ValueError as e:
        # Capturar y mostrar el error de división por cero
        print(e)
