#Version optimizada

class Solution:
    def isPalindrome(self, x):
        # Primero reviso si el número es negativo. Si es negativo, no puede ser palíndromo
        # Ejemplo: -121 al revés sería 121-, y eso no es lo mismo → devuelvo False
        # También, si termina en 0 (como 10, 100, etc.), pero no es 0, tampoco puede ser palíndromo
        # Porque al reversarlo empezaría con 0 y los números no pueden comenzar con 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Voy a crear una variable que guarde la mitad invertida del número
        # La idea es compararla con la otra mitad del número
        half = 0

        # Mientras el número original sea más grande que el invertido que estoy armando
        # Significa que todavía no llego a la mitad
        while x > half:
            # Tomo el último dígito del número (x % 10) y lo agrego a 'half'
            # Por ejemplo, si x = 123, el último dígito es 3, entonces half = 0*10 + 3 = 3
            half = (half * 10) + (x % 10)

            # Después elimino ese último dígito de x, dividiendo entre 10 y quedándome con la parte entera
            # En el ejemplo: x = 123 → x //= 10 → x = 12
            x //= 10

        # Cuando salgo del ciclo, puede haber dos casos:
        # 1. El número tiene cantidad par de dígitos → x y half deben ser exactamente iguales
        # 2. El número tiene cantidad impar de dígitos → el del medio no importa, así que lo saco con half // 10

        # Ejemplo impar: 12321 → después del ciclo: x = 12, half = 123 → 123 // 10 = 12 → x == 12 
        return x == half or x == half // 10

# Pruebo la función con el número 121
# Espero que me diga True porque 121 es igual al revés
print(Solution().isPalindrome(121))



#fuerza bruta o como yo lo haria mas sencillo
class Solution:
    def isPalindrome(self, x):
        x_str = str(x)              # Convierte el número a texto, por ejemplo: 121 -> "121"
        return x_str == x_str[::-1] # Compara el texto original con su reverso  [::-1] es un truquito xd para invertir un string.
    #¿El texto original es igual al texto invertido?”



# Y lo pruebo
print(Solution().isPalindrome(121))   # True
print(Solution().isPalindrome(123))   # False
print(Solution().isPalindrome(-121))  # False
