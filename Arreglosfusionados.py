import time

def ordenar_arreglo(arr):
    return sorted(arr)

def fusionar_arreglos(nums1, nums2):
    nums1 = ordenar_arreglo(nums1)
    nums2 = ordenar_arreglo(nums2)
    return sorted(nums1 + nums2)

def encontrar_mediana(nums1, nums2):
    fusionado = fusionar_arreglos(nums1, nums2)
    total_len = len(fusionado)
    if total_len % 2 == 1:
        return fusionado[total_len // 2]
    else:
        return (fusionado[total_len // 2 - 1] + fusionado[total_len // 2]) / 2

# Ejemplos de prueba
nums1_1 = [1, 3]
nums2_1 = [2]
nums1_2 = [1, 2]
nums2_2 = [3, 4]

# Medir el tiempo de ejecución
start_time = time.time()
print(f"Mediana del primer ejemplo: {encontrar_mediana(nums1_1, nums2_1)}")
print(f"Mediana del segundo ejemplo: {encontrar_mediana(nums1_2, nums2_2)}")
end_time = time.time()

print(f"Tiempo total de ejecución: {end_time - start_time:.5f} segundos")
