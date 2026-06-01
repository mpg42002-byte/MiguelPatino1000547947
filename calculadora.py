# calculadora.py
# Proyecto: Calculadora simple
# Estudiante: Miguel Angel Patino Garcia
# Documento: 1000547947
# Actividad Guía 5 - CI/CD con GitHub Actions

def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números. Lanza error si el divisor es cero."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def potencia(base, exponente):
    """Calcula la potencia de un número."""
    return base ** exponente

def modulo(a, b):
    """Calcula el módulo (residuo) de la división."""
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a % b

# Programa principal
if __name__ == "__main__":
    print("=== Calculadora Simple ===")
    print(f"5 + 3 = {sumar(5, 3)}")
    print(f"10 - 4 = {restar(10, 4)}")
    print(f"6 x 7 = {multiplicar(6, 7)}")
    print(f"15 / 3 = {dividir(15, 3)}")
    print(f"2 ^ 8 = {potencia(2, 8)}")
    print(f"10 % 3 = {modulo(10, 3)}")
    print("Calculadora funcionando correctamente!")