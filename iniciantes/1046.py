hora_inicial, hora_final = map(int, input().split())

if hora_final > hora_inicial:
    hora = hora_final - hora_inicial
    print(f"O JOGO DUROU {hora} HORA(S)")
    
else:
    hora = (24 - hora_inicial) + hora_final
    print(f"O JOGO DUROU {hora} HORA(S)")