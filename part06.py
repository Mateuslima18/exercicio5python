# Função para verificar se os lados formam um triângulo  
def verifica_triangulo(lado1, lado2, lado3):  
    return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)  

# Função para determinar o tipo do triângulo  
def tipo_triangulo(lado1, lado2, lado3):  
    if lado1 == lado2 == lado3:  
        return "Equilátero"  
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:  
        return "Isósceles"  
    else:  
        return "Escaleno"  

# Entrada do usuário  
try:  
    lado1 = float(input("Digite o comprimento do primeiro lado: "))  
    lado2 = float(input("Digite o comprimento do segundo lado: "))  
    lado3 = float(input("Digite o comprimento do terceiro lado: "))  
    
    # Verifica se forma um triângulo  
    if verifica_triangulo(lado1, lado2, lado3):  
        tipo = tipo_triangulo(lado1, lado2, lado3)  
        print(f"Os lados formam um triângulo {tipo}.")  
    else:  
        print("Os lados não podem formar um triângulo.")  
except ValueError:  
    print("Por favor, insira valores numéricos válidos.")   