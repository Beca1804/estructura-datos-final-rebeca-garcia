#Versión óptima
def reverseStack(stack):
    # Usamos una pila auxiliar
    reversed_stack = []

    # Mientras haya elementos en la pila original, los pasamos a la nueva
    while stack:
        reversed_stack.append(stack.pop())

    return reversed_stack

# Ejemplo
original = [1, 2, 3, 4, 5]
print("Pila invertida:", reverseStack(original))  # [5, 4, 3, 2, 1]


#Fuerza Bruta

def reverseStackBrute(stack):
    reversed_stack = []  # Nueva pila vacía

    while stack:  # Mientras la pila original tenga elementos
        # insert(0, ...) este va colocar el elemento al principio del arreglo
        reversed_stack.insert(0, stack.pop())

    return reversed_stack  # Devolvemos la pila invertida

#print(reverseStackBrute([1, 2, 3, 4, 5]))  