"""
Resolução do Desafio 01 do curso Python Developer da DIO.
O Objetivo é construir um mini sistema bancário inicial, utilizando
lógica simples e comandos básicos como loops e fluxos condicionais.
"""


menu = """
   ------- MENU ------

   Bem-vinde ao Banco DIO.
   Selecione uma opção:

   • [d] - Deposito
   • [s] - saque
   • [e] - extrato
   • [q] - sair
   
-> """

saldo_atual = 0
extrato = ""
saques_diarios = 0
limite_diario_valor_saque = 500

while True:
    perg = input(menu)

    if perg in "dseq":
        if perg == "q":
            print("Você saiu do sistema. Obrigado pela preferência.\n")
            break

        if perg == "d":
            valor_deposito = int(input("Valor de depósito: "))

            if valor_deposito > 0:
                saldo_atual += valor_deposito
                extrato += f"{'Depósito:':<12} +R${valor_deposito:.2f}\n"
                print(f"Valor de R${valor_deposito:.2f} depositados com sucesso.")
            else:
                print("Valor inválido! Tente novamente.")

        elif perg == "s":
            valor_saque = int(input("Valor do saque: "))

            if (valor_saque > limite_diario_valor_saque):
                print(f"Limite de saque atingido. Aumente seu limite ou saque um valor inferior a R${limite_diario_valor_saque:.2f}.")
            elif (saques_diarios > 3):
                print("Você atingiu o máximo de 3 saques diários. Tente novamente mais tarde ou aumente seu limite.")
            elif (valor_saque > saldo_atual):
                print("Saldo indisponível. Tente novamente.")
            elif (valor_saque < 0):
                print("Valor inválido! Tente novamente.")
            else:
                saldo_atual -= valor_saque
                extrato += f"{'Saque:':<12} -R${valor_saque:.2f}\n"
                print(f"Valor de R${valor_saque:.2f} sacados com sucesso.")

            saques_diarios += 1
        
        elif perg == "e":
            print("-------- EXTRATO --------\n")
            print("Não foram realizadas operações!" if not extrato else extrato)
            print(f"Saldo Atual: R${saldo_atual:.2f}")
            print("-------------------------\n")

    else:
        print("Comando inválido! Tente novamente.")


