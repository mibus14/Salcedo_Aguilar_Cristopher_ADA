def generate_pascals_triangle(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)  # Cada fila comienza y termina con 1
        for j in range(1, i):  # Calcula los valores intermedios de la fila
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


# Ejemplos de uso
print(generate_pascals_triangle(5))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(generate_pascals_triangle(1))  # Output: [[1]]
