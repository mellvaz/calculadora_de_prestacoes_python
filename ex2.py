#Elabore um programa que utilize uma função com o nome pagamento para determinar o valor a ser pago por uma prestação de uma conta.
#O progrmama deve solicitar ao usuario o valor da prestacao e o n° de dias em atraso e passar estes valores para a funçao pagamento, que calculará o valor a ser pago e devolverá esse valor ao pograma que o chamar
#o programa deve exibir o valor a ser pago na tela
# apos a execucao o programa devera voltar a pedir outro valor de prestacao e assim continuar ate que seja informado um valor igual a zero para a prestacao
#neste momento o programa deverá ser encerrado, exibindo o relatorio do dia, que contera a qt. e o valor total de prestaçes pagas no dia. O calculo do valor a ser pago é:
# Sem atraso, cobrar o valor a prestação
# Com atraso, cobrar 3% de multa, mais 0,1% de juros por dia.
def pagamento( valor, dias): 
        if dias == 0:
            return valor
        else:
            multa = valor * 0.03
            juros = valor * (dias * 0.001)
            return valor + multa + juros

qt = 0
valorTotal = 0.0
valor = float(input("\nDigite o valor da prestação ou 0 para o Relatório do dia: "))

while valor != 0:
    dias= int(input("Dias em atraso: "))
    valorPago = pagamento(valor, dias)
    print (f"\nValor a ser pago: R$ {valorPago:.2f}\n")
    qt += 1
    valorTotal += valorPago
    valor = float(input("\nDigite o valor da prestação ou 0 para o Relatório do dia: "))
print("\n--- RELATÓRIO DO DIA ---")
print(f"Quantidade de prestações pagas: {qt}\nValor total de prestações: {valorTotal:.2f}")