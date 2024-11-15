# Etapa 1: Configuração inicial
# Aqui definimos a meta de consumo sustentável e inicializamos variáveis para os cálculos
print("Bem-vindo ao sistema de monitoramento de energia limpa!")
meta = 150  # Meta de consumo sustentável em kWh
n = int(input("Informe a quantidade de dias monitorados: "))  # Número de dias a monitorar

# Variáveis para controle
soma_consumo = 0  # Soma total do consumo
dias_meta_cumprida = 0  # Dias que cumpriram a meta
dias_meta_nao_cumprida = 0  # Dias que não cumpriram a meta
maior_consumo = -float('inf')  # Inicialmente, o menor possível
menor_consumo = float('inf')  # Inicialmente, o maior possível
dia_maior_consumo = 0
dia_menor_consumo = 0

# Etapa 2: Coleta de Dados e Processamento
# Nesta etapa, o programa solicita os consumos diários e faz as análises básicas
print("\n--- Coleta de Dados ---")
for dia in range(1, n + 1):
    consumo = int(input(f"Informe o consumo de energia (kWh) do dia {dia}: "))
    soma_consumo += consumo

    # Verificação da meta
    if consumo >= meta:
        dias_meta_cumprida += 1
    else:
        dias_meta_nao_cumprida += 1

    # Identificação do maior e menor consumo
    if consumo > maior_consumo:
        maior_consumo = consumo
        dia_maior_consumo = dia
    if consumo < menor_consumo:
        menor_consumo = consumo
        dia_menor_consumo = dia

# Etapa 3: Análise Adicional
# Realiza cálculos complementares como média de consumo
print("\n--- Análise Adicional ---")
media_consumo = soma_consumo / n

# Etapa 4: Relatório de Resultados
# Exibe o relatório final com os dados analisados
print("\n--- Relatório de Resultados ---")
if dias_meta_cumprida == n:
    print("Parabéns! Todos os dias cumpriram a meta de consumo sustentável.")
elif dias_meta_cumprida == 0:
    print("Infelizmente, nenhum dia cumpriu a meta de consumo sustentável.")
else:
    print(f"{dias_meta_cumprida} dias cumpriram a meta e {dias_meta_nao_cumprida} dias não cumpriram a meta.")

print(f"A média de consumo foi de {media_consumo:.2f} kWh.")
print(f"O maior consumo foi de {maior_consumo} kWh (dia {dia_maior_consumo}).")
print(f"O menor consumo foi de {menor_consumo} kWh (dia {dia_menor_consumo}).")


