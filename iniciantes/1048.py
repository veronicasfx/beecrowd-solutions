salario = float(input())

if salario <= 400.00:
    percentual = 15
    reajuste = salario * 0.15
    novo_salario = salario + reajuste


elif salario <= 800.00:
    percentual = 12
    reajuste = salario * 0.12
    novo_salario = salario + reajuste
    

elif salario <= 1200.00:
    percentual = 10
    reajuste = salario * 0.10
    novo_salario = salario + reajuste


elif salario <= 2000.00:
    percentual = 7
    reajuste = salario * 0.07
    novo_salario = salario + reajuste


else:
    percentual = 4
    reajuste = salario * 0.04
    novo_salario = salario + reajuste


print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")