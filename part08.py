# Solicita ao usuário que insira o nome de usuário  
usuario = input("Digite o nome de usuário: ")  

# Solicita ao usuário que insira a senha  
senha = input("Digite a senha: ")  

# Verifica se o nome de usuário e a senha estão corretos  
if usuario == "admin" and senha == "12345":  
    print("Acesso concedido")  
else:  
    print("Acesso negado")  