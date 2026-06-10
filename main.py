import os

def limpar_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def mensagem_erro():
    print("ERRO: Você digitou um valor inválido!")

def continuar():
    input("\nAperte ENTER para continuar")
    
def mostrar_menu():
    print("""
    \033[1;37;41m-= 1 -=\033[m Converter Para Binário
          
    \033[1;37;43m-= 2 -=\033[m Converter Para Octal
          
    \033[1;37;42m-= 3 -=\033[m Converter Para Hexadecimal
          
    \033[1;37;45m-= 4 -=\033[m SAIR
    """)

def input_opcao():
    while True:
        try:
            opcao = int(input("O que deseja fazer: "))
            if 1 <= opcao <= 4:
                return opcao
            else:
                print("A opção precisa ser entre 1 e 4")
        except ValueError:
            mensagem_erro()
            print("A opção precisa ser um número.")

def input_numero():
    while True:
        try:
            num = int(input("Digite um número decimal positivo e inteiro: "))
            if num >= 0:
                return num
            else:
                print("O número precisa ser positivo e inteiro.")
        except ValueError:
            mensagem_erro()
            print("Digite um número positivo e inteiro.")

def transformar(decimal, opcao):
    lista_digitos = []
    if decimal == 0:
        return "0"
    match opcao:
        case 1:
            divisor = 2
        case 2:
            divisor = 8
        case 3:
            hexadecimais = "ABCDEF"
            divisor = 16
    while decimal > 0:
        digito = decimal % divisor
        if opcao == 3 and digito > 9:
            digito = hexadecimais[digito - 10]
        lista_digitos.append(digito)
        decimal //= divisor
    return "".join(map(str, reversed(lista_digitos)))

def mostrar_resultado(num, resultado):
    print(f"\nO número digitado: \033[1;37;41m {num} \033[m")
    print(f"É igual a: \033[1;37;42m {resultado} \033[m")

def main():
    while True:
        limpar_terminal()
        mostrar_menu()
        opcao = input_opcao()
        if opcao == 4:
            print("SAINDO...")
            break
        else:
            num = input_numero()
            resultado = transformar(num, opcao)
            mostrar_resultado(num, resultado)
            continuar()

if __name__ == "__main__":
    main()
    