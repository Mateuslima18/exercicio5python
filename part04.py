# Solicita ao usuário para inserir três números  
numero1 = float(input("Digite o primeiro número: "))  
numero2 = float(input("Digite o segundo número: "))  
numero3 = float(input("Digite o terceiro número: "))  

# Encontra o maior número  
maior_numero = max(numero1, numero2, numero3)  

# Exibe o resultado  
print(f"O maior número entre {numero1}, {numero2} e {numero3} é: {maior_numero}") 