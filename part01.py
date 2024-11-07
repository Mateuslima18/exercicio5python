# Função para verificar se um número é par ou ímpar  
def verificar_par_ou_impar(numero):  
    if numero % 2 == 0:  
        return "par"  
    else:  
        return "ímpar"  

# Solicitar ao usuário que insira um número  
numero_usuario = int(input("Digite um número: "))  

# Verificar e exibir o resultado  
resultado = verificar_par_ou_impar(numero_usuario)  
print(f"O número {numero_usuario} é {resultado}.")