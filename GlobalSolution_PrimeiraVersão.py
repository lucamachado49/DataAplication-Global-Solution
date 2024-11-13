def monitorar_consumo():
    # Solicitar o número de dias de coleta
    n = int(input("Digite a quantidade de dias de coleta de dados de consumo de energia: "))

    # Inicializar variáveis
    soma_consumo = 0
    dias_meta_atingida = 0
    maior_consumo = None
    menor_consumo = None
    dia_maior_consumo = 0
    dia_menor_consumo = 0

    # Definir a meta de consumo sustentável
    meta = 150

    # Processar os dados de consumo dia a dia
    for dia in range(1, n + 1):
        consumo = int(input(f"Digite o consumo de energia do dia {dia} (em kWh): "))
        
        # Atualizar a soma do consumo
        soma_consumo += consumo

        # Verificar se a meta foi atingida
        if consumo >= meta:
            dias_meta_atingida += 1

        # Atualizar o maior consumo
        if maior_consumo is None or consumo > maior_consumo:
            maior_consumo = consumo
            dia_maior_consumo = dia

        # Atualizar o menor consumo
        if menor_consumo is None or consumo < menor_consumo:
            menor_consumo = consumo
            dia_menor_consumo = dia

    # Calcular a média de consumo
    media_consumo = soma_consumo / n

    # Exibir os resultados
    print("\n--- Análise de Consumo de Energia ---")
    print(f"Meta de consumo sustentável atingida em {dias_meta_atingida} dia(s).")
    print(f"Média de consumo ao longo dos {n} dias: {media_consumo:.2f} kWh.")
    print(f"Maior consumo registrado foi no dia {dia_maior_consumo}, com {maior_consumo} kWh.")
    print(f"Menor consumo registrado foi no dia {dia_menor_consumo}, com {menor_consumo} kWh.")

# Executar o programa
monitorar_consumo()

