#VERSION OPTIMIZADA

def firstNonRepeatingChar(s):
    from collections import Counter

    # Contamos cada letra usando Counter
    count = Counter(s)

    # Buscamos la primera letra que solo aparece una vez
    for char in s:
        if count[char] == 1:
            return char
    return None

# Ejemplo
print("Primera no repetida:", firstNonRepeatingChar("aabccdbe"))  



#FUERZA BRUTAA

def firstNonRepeatingCharBrute(s):
    for i in range(len(s)):  # Recorremos cada letra

        if s.count(s[i]) == 1:  # Si solo aparece una vez en todo el string
            return s[i]  # Es la primera no repetida

    return None  # Si no hay ninguna, devolvemos None

print(firstNonRepeatingCharBrute("aabccdbe"))