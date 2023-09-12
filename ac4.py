def calcular_parcelamento(divida):
    opcoes_parcelamento = [1, 3, 6, 9, 12]
    percentual_juros = [0, 10, 15, 20, 25]

    relatorio = []

    for parcelas in opcoes_parcelamento:
        percentual = percentual_juros[opcoes_parcelamento.index(parcelas)]
        valor_juros = (divida * percentual) / 100
        valor_total_divida = divida + valor_juros
        valor_parcela = valor_total_divida / parcelas

        relatorio.append(
            (parcelas, percentual, valor_juros, valor_total_divida, valor_parcela)
        )

    return relatorio


divida = float(input("Digite o valor da dívida: "))


opcoes = calcular_parcelamento(divida)


print("\nOpções de Parcelamento:")
print("Parcelas | Juros (%) | Valor dos Juros | Valor Total | Valor da Parcela")
print("-" * 70)
for parcelas, percentual, valor_juros, valor_total, valor_parcela in opcoes:
    print(f"{parcelas:8} | {percentual:10}% | R${valor_juros:.2f} | R${valor_total:.2f} | R${valor_parcela:.2f}")



intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while True:

    numero = int(input("Digite um número (ou um número negativo para encerrar): "))


    if numero < 0:
        break


    if 0 <= numero <= 25:
        intervalo_0_25 += 1
    elif 26 <= numero <= 50:
        intervalo_26_50 += 1
    elif 51 <= numero <= 75:
        intervalo_51_75 += 1
    elif 76 <= numero <= 100:
        intervalo_76_100 += 1


print("Quantidade de números nos intervalos:")
print("[0-25]:", intervalo_0_25)
print("[26-50]:", intervalo_26_50)
print("[51-75]:", intervalo_51_75)
print("[76-100]:", intervalo_76_100)

