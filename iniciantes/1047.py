hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

inicio_total = (hora_inicial * 60) + minuto_inicial
fim_total = (hora_final * 60) + minuto_final

if fim_total == inicio_total:
    duração = 1440


elif fim_total > inicio_total:
    duração = fim_total - inicio_total


else:
    duração = (1440 - inicio_total) + fim_total

horas = duração // 60
minutos = duração % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
