menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> """

# Initialize account balance
saldo = 0

# Set daily withdrawal limit
valor_limite_por_saque_diario = 500

# Initialize transaction history
extrato = ""

# Initialize the number of withdrawals made
numero_saques = 0

# Set the maximum number of daily withdrawals
QUANTIDADE_LIMITE_SAQUES_DIARIOS = 3

# Start an infinite loop to continuously prompt the user for an action
while True:

    # Display the menu and get the user's choice
    opcao = input(menu)

    # If the user chooses to deposit
    if opcao == "1":
        # Prompt the user to enter the deposit amount
        valor = float(input("Informe o valor do depósito: "))

        # Check if the deposit amount is valid
        if valor > 0:
            # Update the account balance
            saldo += valor
            # Record the deposit in the transaction history
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            # Inform the user that the operation failed due to an invalid amount
            print("Operação falhou! O valor informado é inválido.")

    # If the user chooses to withdraw
    elif opcao == "2":
        # Prompt the user to enter the withdrawal amount
        valor = float(input("Informe o valor do saque: "))

        # Check if the withdrawal amount exceeds the account balance
        excedeu_saldo = valor > saldo

        # Check if the withdrawal amount exceeds the daily limit
        excedeu_limite = valor > valor_limite_por_saque_diario

        # Check if the number of withdrawals exceeds the daily limit
        excedeu_saques = numero_saques >= QUANTIDADE_LIMITE_SAQUES_DIARIOS

        # Handle different failure cases
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite por saque diário.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        else:
            # Process the withdrawal
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    # If the user chooses to view the transaction history

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
