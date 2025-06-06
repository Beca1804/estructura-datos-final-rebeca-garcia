#Manera Optimizada:

# Definimos la clase Solution con el método óptimo
class Solution:
    def removeElement(self, nums, val):
       
        #Elimina in-place todas las ocurrencias de 'val' en la lista 'nums' y
        #retorna la cantidad de elementos restantes distintos de 'val'.
       
        # i indica la posición donde vamos a colocar el siguiente número válido
        i = 0
        
        # Recorremos toda la lista con j
        for j in range(len(nums)):
            # Si el valor actual no es el que queremos eliminar
            if nums[j] != val:
                # Copiamos ese valor a la posición i (la siguiente válida)
                nums[i] = nums[j]
                i += 1  # Avanzamos la posición válida
        # Al final, i es la cantidad de elementos diferentes a val
        return i


#Lo pruebo para ver si funciona

# Creamos una instancia de la clase Solution
sol = Solution()

# Ejemplo 1
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = sol.removeElement(nums1, val1)

print("Óptima Ejemplo 1:")
print("k =", k1)               




#Fuerza Bruta
# Definimos otra clase con la versión de fuerza bruta
class FuerzaBruta:
    def removeElement(self, nums, val):
        
        #Elimina in-place todas las ocurrencias de 'val' en la lista 'nums'
        #usando eliminación con pop() dentro de un while.
       
        i = 0
        while i < len(nums):
            # Si encontramos el valor a eliminar
            if nums[i] == val:
                nums.pop(i)  # Lo eliminamos
                # No incrementamos i porque la lista se recorre hacia adelante automáticamente
            else:
                i += 1  # Avanzamos solo si no eliminamos nada
        return len(nums)



# Instancia de la clase
fb = FuerzaBruta()

# Ejemplo 1
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = fb.removeElement(nums1, val1)

print("\nFuerza Bruta - Ejemplo 1:")
print("k =", k1)                         
print("nums modificados =", nums1)      

