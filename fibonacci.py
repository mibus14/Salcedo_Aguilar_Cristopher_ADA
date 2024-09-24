def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Llamada a la función y mostrar resultado
n = 9
resultado = fibonacci(n)
print(f"El número Fibonacci en la posición {n} es {resultado}")
