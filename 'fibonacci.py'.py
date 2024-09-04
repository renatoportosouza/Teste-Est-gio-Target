#'fibonacci.py'

# Função recursiva para calcular o n-ésimo número de Fibonacci
def fibonacci(n): 
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# Solicita ao usuário para inserir um número
num = int(input("Digite um número: ")) 
fib = fibonacci(num)

# Verifica se o número pertence à sequência de Fibonacci e exibe a mensagem correspondente
if num in [fibonacci(i) for i in range(num+1)]:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")