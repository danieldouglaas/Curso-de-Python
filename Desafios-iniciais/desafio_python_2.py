valores = input().split() 

participantes = int(valores[0])
hot_dogs = int(valores[1])

media = participantes / hot_dogs

print(f'{media:.2f}')