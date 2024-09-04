#'inversao_string.py'

# Função para inverter uma string manualmente
def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Solicita ao usuário para inserir uma string
string = input("Informe uma string: ")

# Exibe a string invertida
print(f"String invertida: {inverter_string(string)}")
