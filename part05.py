# Função para classificar a idade  
def classificar_idade(idade):  
    if 0 <= idade <= 12:  
        return "Criança"  
    elif 13 <= idade <= 19:  
        return "Adolescente"  
    elif 20 <= idade <= 59:  
        return "Adulto"  
    elif idade >= 60:  
        return "Idoso"  
    else:  
        return "Idade inválida" 
    # Solicitar a idade do usuário  
try:  
    idade_usuario = int(input("Digite a sua idade: "))  
    classificacao = classificar_idade(idade_usuario)  
    print(f"A sua classificação é: {classificacao}")  
except ValueError:  
    print("Por favor, digite um número válido para a idade.")