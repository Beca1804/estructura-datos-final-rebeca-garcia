#De Manera optimizada

def countUniqueElements(nums):
    # Creamos un conjunto para almacenar solo elementos únicos
    unique_elements = set()

    # Recorremos la lista e insertamos cada número en el conjunto
    for num in nums:
        unique_elements.add(num)

    # Retornamos la cantidad de elementos únicos
    return len(unique_elements)

#Ahora lo pruebo
nums = [1, 2, 2, 3, 4, 4, 5]
print("Resultado:", countUniqueElements(nums))    #me tiene que dcar 5 :)



#Fuerza Bruta 
def countUniqueElementsBrute(nums):
    count = 0  # Inicializamos contador de elementos únicos

    for i in range(len(nums)):  # Recorremos cada elemento
        is_unique = True  # Suponemos que el elemento actual es único

        for j in range(len(nums)):  # Lo comparamos con todos los demás
            if i != j and nums[i] == nums[j]:  # Si hay duplicado (en diferente posición)
                is_unique = False  # Ya no es único
                break  # Terminamos búsqueda

        if is_unique:
            count += 1  # Si se mantuvo único, sumamos al contador

    return count  # Regresamos cuántos únicos hay


print(countUniqueElementsBrute([1, 2, 2, 3, 4, 4, 5]))  
