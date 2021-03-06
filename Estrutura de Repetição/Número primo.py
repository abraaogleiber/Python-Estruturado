"""
Programa 063
Área de estudos.
data 25.11.2020     (Indefinida) Hs
@Autor: Abraão A. Silva
"""

# Entrada.
n = int(input('Digite um valor.: '))

dividido = int()    # Contador.
for item in range(1, n+1):  # Iteração por item. 
    if n % item == 0:   # Testa divisibilidade.
        dividido += 1   # Incremento.

# Condicional verifica a quantidade de valores divisíveis.
if dividido == 2:
    print(f'O número {n} é Primo.')
else:
    # Essa estrutura retorna na tela os valores pelo qual o número é divisível.
    print(f'O número {n} não é Primo, pois é divisível por: ', end='')
    for item in range(1, n+1):
        if n % item == 0:
            print(item, end=' ')

print('\n')     # Formatação para facilitar minha visualização pelo terminal.
