def mergeKLists(lists):
    import heapq

    # Crear una lista para el resultado
    merged_list = []

    # Crear un min-heap
    min_heap = []

    # Llenar el min-heap con el primer elemento de cada lista
    for i in range(len(lists)):
        if lists[i]:  # Solo añadir si la lista no está vacía
            heapq.heappush(min_heap, (lists[i][0], i, 0))  # (valor, índice de la lista, índice del elemento)

    # Mientras el min-heap no esté vacío
    while min_heap:
        # Extraer el elemento más pequeño
        value, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(value)  # Añadir el valor a la lista fusionada

        # Si hay más elementos en la misma lista, añadir el siguiente
        if element_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))

    return merged_list


# Ejemplos de uso
print(mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]]))  # Salida: [1, 1, 2, 3, 4, 4, 5, 6]
print(mergeKLists([]))  # Salida: []
print(mergeKLists([[]]))  # Salida: []
