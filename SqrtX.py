
#Manera Optimizada

def roundedSqrt(x):
    # Si x es 0 o 1, su raíz cuadrada redondeada es el mismo número
    if x < 2:
        return x

    # Definimos los límites iniciales de la búsqueda binaria
    left = 1                   # Límite inferior
    right = x // 2 + 1         # Límite superior. No puede ser mayor a x // 2 + 1
    ans = 1                    # Variable que almacenará la raíz más cercana

    # Comenzamos la búsqueda binaria
    while left <= right:
        mid = (left + right) // 2  # Calculamos el punto medio
        square = mid * mid         # Elevamos mid al cuadrado sin usar funciones

        if square == x:
            # Si encontramos una raíz exacta, la devolvemos de inmediato
            return mid
        elif square < x:
            # Si el cuadrado es menor que x, nos movemos hacia la derecha
            ans = mid              # Guardamos este valor como posible respuesta
            left = mid + 1         # Aumentamos el límite inferior
        else:
            # Si el cuadrado es mayor que x, reducimos el límite superior
            right = mid - 1

    # Después del ciclo, comparamos cuál de los dos valores está más cerca de la raíz
    if abs(ans * ans - x) <= abs((ans + 1) * (ans + 1) - x):
        return ans             # Si ans está más cerca, lo devolvemos
    else:
        return ans + 1         # Si ans+1 está más cerca, lo devolvemos


print(roundedSqrt(4))    



#Fuerza Bruta

def roundedSqrtBrute(x):
    i = 0

    while i * i <= x:
        i += 1

    before = i - 1
    after = i

    # Decidimos cuál está más cerca
    if abs(before * before - x) <= abs(after * after - x):
        return before
    else:
        return after

print(roundedSqrt(8))   



