def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calcular el área actual
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        # Mover el puntero de la línea más baja
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
# Ejemplo 1
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))  # Salida esperada: 49

# Ejemplo 2
height = [1,1]
print(maxArea(height))  # Salida esperada: 1
