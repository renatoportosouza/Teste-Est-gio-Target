#'faturamento_diario.py'

# Importa o módulo para trabalhar com JSON
import json 

# Carrega os dados do arquivo JSON
with open('faturamento.json'
          ) as f:
    data = json.load(f)

# Extrai os valores de faturamento de cada dia
valores = [item['valor'] for item in data]

# Calcula o maior e o menor valor de faturamento
maior_valor = max(valores)
menor_valor = min(valores)

# Calcula a média, ignorando os dias sem venda
media = sum(valores) / len(list(filter(lambda x: x > 0, valores)))

# Conta os dias com faturamento acima da média
acima_media = sum(1 for x in valores if x > media)

# Imprime os resultados
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
print(f"Dias acima da média: {acima_media}")
