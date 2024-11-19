def numOfSubarrays(arr, k, threshold):
    # Inicializar variables
    count = 0
    target = k * threshold  # Umbral en términos de suma
    current_sum = sum(arr[:k])  # Suma inicial de los primeros k elementos

    # Verificar la primera ventana
    if current_sum >= target:
        count += 1

    # Desplazar la ventana a lo largo del arreglo
    for i in range(k, len(arr)):
        # Actualizar la suma de la ventana
        current_sum += arr[i] - arr[i - k]
        # Verificar si la nueva ventana cumple la condición
        if current_sum >= target:
            count += 1

    return count


# Ejemplo de uso
arr1, k1, threshold1 = [2, 2, 2, 2, 5, 5, 5, 8], 3, 4
arr2, k2, threshold2 = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5

print(numOfSubarrays(arr1, k1, threshold1))  # Salida: 3
print(numOfSubarrays(arr2, k2, threshold2))  # Salida: 6

