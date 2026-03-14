número = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

print(número)

for nota in notas:
    quantidade = número // nota
    número = número % nota
    print(f"{quantidade} nota(s) de R$ {nota},00")
