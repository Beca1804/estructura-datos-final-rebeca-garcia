#Manera Optimizada

class Solution:
    def isValid(self, s: str) -> bool:
        # Creamos un diccionario para relacionar cada paréntesis cerrado con su abierto correspondiente
        par = {')': '(', '}': '{', ']': '['}

        # Inicializamos una lista vacía que usaremos como pila para almacenar paréntesis abiertos
        stack = []

        # Recorremos cada carácter en la cadena de entrada
        for char in s:
            # Si el carácter es uno de los paréntesis cerrados
            if char in par:
                # Intentamos sacar el último paréntesis abierto de la pila, si está vacía usamos '#'
                top_element = stack.pop() if stack else '#'

                # Comprobamos si el paréntesis abierto esperado coincide con el que sacamos
                if par[char] != top_element:
                    # Si no coinciden, la cadena no es válida, retornamos False
                    return False
            else:
                # Si es un paréntesis abierto, lo añadimos a la pila para esperar su cierre
                stack.append(char)

        # Al final, si la pila está vacía significa que todos los paréntesis abiertos fueron cerrados correctamente
        # Retornamos True si está vacía, False si no
        return not stack


#lo probamos
sol = Solution()

# Casos válidos
print(sol.isValid("()"))       # True
print(sol.isValid("()[]{}"))   # True
print(sol.isValid("{[]}"))     # True

# Casos inválidos
print(sol.isValid("(]"))       # False
print(sol.isValid("([)]"))     # False
print(sol.isValid("((("))      # False




#Fuerza Bruta

class Solution:
    def isValid(self, s: str) -> bool:
        # Inicializamos una variable para almacenar la longitud anterior de la cadena
        prev_length = -1


        # Mientras la longitud de la cadena cambie (significa que se eliminaron pares)
        while prev_length != len(s):
            # Actualizamos la longitud previa a la actual
            prev_length = len(s)
            # Eliminamos todos los pares de paréntesis válidos de la cadena
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")


        # Si al final la cadena quedó vacía, todos los paréntesis eran válidos y cerrados correctamente
        return len(s) == 0

#Lo pruebo
        sol = Solution()

# Casos válidos
print(sol.isValid("()"))       # True
print(sol.isValid("()[]{}"))   # True
print(sol.isValid("{[]}"))     # True

# Casos inválidos
print(sol.isValid("(]"))       # False
print(sol.isValid("([)]"))     # False
print(sol.isValid("((("))      # False