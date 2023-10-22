def imprimir_linhas(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

def contar_digitos(numero):
    return len(str(numero))

try:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

    resultado = num1 / num2
except ValueError:
    print("Erro: Você deve inserir números inteiros válidos.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print("O resultado da divisão é:", resultado)
finally:
    print("Quantidade de dígitos no primeiro número:", contar_digitos(num1))
    print("Quantidade de dígitos no segundo número:", contar_digitos(num2))

n = int(input("Digite um valor para n: "))
imprimir_linhas(n)
