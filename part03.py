def calculadora():  
    # Solicita ao usuário dois números  
    num1 = float(input("Digite o primeiro número: "))  
    num2 = float(input("Digite o segundo número: "))  
    
    # Solicita ao usuário a operação  
    operacao = input("Digite a operação (+, -, *, /): ")  
    
    # Realiza a operação e exibe o resultado  
    if operacao == '+':  
        resultado = num1 + num2  
        print(f"{num1} + {num2} = {resultado}")  
    elif operacao == '-':  
        resultado = num1 - num2  
        print(f"{num1} - {num2} = {resultado}")  
    elif operacao == '*':  
        resultado = num1 * num2  
        print(f"{num1} * {num2} = {resultado}")  
    elif operacao == '/':  
        if num2 != 0:  
            resultado = num1 / num2  
            print(f"{num1} / {num2} = {resultado}")  
        else:  
            print("Erro: Divisão por zero não é permitida.")  
    else:  
        print("Operação inválida. Por favor, escolha entre +, -, * ou /.")  

# Chama a função da calculadora  
calculadora()