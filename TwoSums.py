#Fuerza Bruta
from typing import List  # Importamos List para indicar tipos en la función

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Recorremos cada índice i en la lista nums
        for i in range(len(nums)):
            # Para cada i, recorremos los índices j que están después de i
            for j in range(i + 1, len(nums)):
                # Verificamos si la suma de nums[i] + nums[j] es igual al target
                if nums[j] == target - nums[i]:
                    # Si sí, devolvemos los índices i y j como resultado
                    return [i, j]

# Creamos una instancia de la clase Solution
solu = Solution()
# Lista de números de ejemplo
nums = [3, 8, 12, 15, 7]
# Valor objetivo que queremos obtener con la suma de dos números
target = 19
# Ejecutamos el método twoSum con los datos de ejemplo
result = solu.twoSum(nums, target)
# Imprimimos los índices encontrados
print("Índices encontrados (fuerza bruta):", result)






#Manera Optimizada
from typing import List  # Importamos List para indicar tipos en la función

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}  # Creamos un diccionario vacío para guardar valores y sus índices

        # Recorremos la lista con índice i y valor num usando enumerate
        for i, num in enumerate(nums):
            # Calculamos el complemento que necesitamos para llegar al target
            complemento = target - num

            # Verificamos si el complemento ya está guardado en el diccionario
            if complemento in mapa:
                # Si está, devolvemos el índice del complemento y el índice actual i
                return [mapa[complemento], i]

            # Si no está, guardamos el número actual como clave y su índice como valor
            mapa[num] = i

# Creamos una instancia de la clase Solution
solu = Solution()
# Lista de números de ejemplo
nums = [3, 8, 12, 15, 7]
# Valor objetivo que queremos obtener con la suma de dos números
target = 19
# Ejecutamos el método twoSum con los datos de ejemplo
result = solu.twoSum(nums, target)
# Imprimimos los índices encontrados
print("Índices encontrados (con hash map):", result)




