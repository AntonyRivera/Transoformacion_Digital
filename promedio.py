def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
        numeros (list): Lista de valores numéricos.

    Retorna:
        float: Promedio de los números de la lista.
    """
    return sum(numeros) / len(numeros)
# Ejemplo de uso
numeros = [10, 8, 7, 4, 9]
promedio = calcular_promedio(numeros)
print(f"El promedio es: {promedio}")