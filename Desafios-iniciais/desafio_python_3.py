valores = input().split()

tempo = int (valores[0])
velocidade_md = int (valores[1])
distancia = (velocidade_md * tempo)

KML = 12

litros = ( distancia / KML)

print(f'{litros:.3f}')
