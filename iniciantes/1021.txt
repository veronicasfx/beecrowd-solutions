valor = float(input())
valor_centavos = int(round(valor * 100))

reais = valor_centavos // 100
notas = [100, 50, 20, 10, 5, 2]
moedas_centavos = [50, 25, 10, 5, 1]

print("NOTAS:")

for nota in notas:
    quantidade = reais // nota
    reais = reais % nota
    print(f'{quantidade} nota(s) de R$ {nota}.00')

centavos = valor_centavos % 100

print("MOEDAS:")
moeda_1_real = reais
print(f'{moeda_1_real} moeda(s) de R$ 1.00')

for moeda in moedas_centavos:
    quantidade = centavos // moeda
    centavos = centavos % moeda
    print(f'{quantidade} moeda(s) de R$ {moeda/100:.2f}')
