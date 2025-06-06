#Manera Optimizada 
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Si la lista está vacía, no hay elementos únicos
        if not nums:
            return 0
        
        # 'i' es el índice para colocar el siguiente elemento único
        i = 0
        
        # Recorremos la lista desde el segundo elemento hasta el final
        for j in range(1, len(nums)):
            # Comparamos el elemento actual con el último elemento único encontrado
            if nums[j] != nums[i]:
                i += 1           # Avanzamos el índice de elementos únicos
                nums[i] = nums[j] # Guardamos el nuevo elemento único en la posición correcta
                
        # El número de elementos únicos es i+1 porque 'i' es índice (base 0)
        return i + 1
    
    # Ejemplo de uso e impresión
nums_opt = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
k_opt = sol.removeDuplicates(nums_opt)

print("Optimizado:")
print("k =", k_opt)
print("nums modificada:", nums_opt[:k_opt])  # Solo mostramos la parte válida de nums



#Fuerza Bruta
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Crear una lista vacía para guardar los elementos únicos
        únicos = []
        
        # Recorrer cada número en la lista original
        for num in nums:
            # Si el número no está en la lista de únicos, lo agregamos
            # Esto revisa si ya vimos ese número antes
            if num not in únicos:
                únicos.append(num)
        
        # Ahora modificamos la lista original 'nums' para que
        # los primeros elementos sean los únicos encontrados
        for i in range(len(únicos)):
            nums[i] = únicos[i]
        
        # Devolvemos la cantidad de elementos únicos encontrados
        return len(únicos)

nums_fuerza = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
k_fuerza = sol.removeDuplicates(nums_fuerza)

print("Fuerza bruta:")
print("k =", k_fuerza)
print("nums modificada:", nums_fuerza[:k_fuerza])  # Solo mostramos la parte válida
