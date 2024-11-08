def verificar_ano_bissexto(ano):  
    # Um ano é bissexto se:  
    # 1. Divisível por 4 e não divisível por 100, ou  
    # 2. Divisível por 400  
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):  
        return True  
    else:  
        return False  

# Solicita ao usuário que insira um ano  
try:  
    ano_usuario = int(input("Digite um ano: "))  
    
    # Verifica se o ano é bissexto  
    if verificar_ano_bissexto(ano_usuario):  
        print(f"O ano {ano_usuario} é bissexto.")  
    else:  
        print(f"O ano {ano_usuario} não é bissexto.")  
except ValueError:  
    print("Por favor, insira um ano válido (um número inteiro).")  