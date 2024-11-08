def converter_nota_para_conceito(nota):  
    if 90 <= nota <= 100:  
        return 'A'  
    elif 80 <= nota < 90:  
        return 'B'  
    elif 70 <= nota < 80:  
        return 'C'  
    elif 60 <= nota < 70:  
        return 'D'  
    elif 0 <= nota < 60:  
        return 'F'  
    else:  
        return 'Nota inválida'  

# Solicita ao usuário que insira a nota  
try:  
    nota_usuario = float(input("Digite a nota (0 a 100): "))  
    conceito = converter_nota_para_conceito(nota_usuario)  
    print(f"A nota {nota_usuario} corresponde ao conceito: {conceito}")  
except ValueError:  
    print("Por favor, insira um número válido.")  