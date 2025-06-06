#Fuerza Bruta

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Si la lista está vacía, regresamos una cadena vacía
        if not strs:
            return ""
        
        # Tomamos el primer string como referencia
        prefijo = strs[0]
        
        # Comparamos el prefijo con cada string de la lista
        for s in strs[1:]:
            # Mientras el string actual no comience con el prefijo
            while not s.startswith(prefijo):
                # Quitamos el último carácter del prefijo
                prefijo = prefijo[:-1]
                
                # Si eliminamos todo el prefijo y no hay coincidencias
                if not prefijo:
                    return ""
        
        # Retornamos el prefijo común encontrado
        return prefijo

# Ejemplo Usandolo:
sol = Solution()
entrada = ["flower", "flow", "flight"]
print("Prefijo común más largo:", sol.longestCommonPrefix(entrada))





#Version Optimizada

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Si no hay palabras en la lista, regresamos ""
        if not strs:
            return ""

        # Recorremos letra por letra usando zip, que empareja los caracteres
        for i, letra in enumerate(zip(*strs)):
            # Convertimos la tupla en conjunto para ver si todas son iguales
            if len(set(letra)) > 1:
                # Si hay diferencia, retornamos hasta la posición i
                return strs[0][:i]

        # Si todas coinciden, regresamos el primer string completo
        return strs[0]

# Ejemplo de uso
sol = Solution()
entrada = ["flower", "flow", "flight"]
print("Prefijo común más largo (opt):", sol.longestCommonPrefix(entrada))


#sol es la instancia de la clase solution
#entrada lista de cadenas que le paso para que busque el prefijo común
#longestCommonPrefix Es el metodo que cree dentro de esa clase