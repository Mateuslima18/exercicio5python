def calcular_imc(peso, altura):  
    # Calcula o IMC  
    imc = peso / (altura ** 2)  
    return imc  

def classificar_imc(imc):  
    # Classifica o IMC  
    if imc < 18.5:  
        return "Abaixo do peso"  
    elif 18.5 <= imc < 24.9:  
        return "Peso normal"  
    elif 25 <= imc < 29.9:  
        return "Sobrepeso"  
    elif 30 <= imc < 39.9:  
        return "Obesidade"  
    else:  
        return "Obesidade mórbida"  

# Solicita ao usuário seu peso e altura  
try:  
    peso = float(input("Digite seu peso em kg: "))  
    altura = float(input("Digite sua altura em metros: "))  
    
    # Calcula o IMC  
    imc = calcular_imc(peso, altura)  
    
    # Classifica e exibe o resultado  
    classificacao = classificar_imc(imc)  
    print(f"Seu IMC é: {imc:.2f}. Classificação: {classificacao}")  
except ValueError:  
    print("Por favor, insira valores numéricos válidos.")  