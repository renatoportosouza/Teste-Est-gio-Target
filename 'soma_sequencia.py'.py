#'soma_sequencia.py'

# Define as variáveis iniciais
INDICE = 13  # Este é o número até o qual vamos somar
SOMA = 0     # Inicializa a soma como 0
K = 0        # Inicializa o contador K como 0

# Enquanto K for menor que o INDICE, continue somando
while K < INDICE:
    K = K + 1          # Incrementa K em 1 a cada iteração
    SOMA = SOMA + K    # Adiciona o valor de K à soma total

# Exibe o resultado final
print(SOMA) # O valor final de SOMA será 91
