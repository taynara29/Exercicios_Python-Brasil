QUANTIDADE_NOTAS = 3

# Declaração de um vetor
notas = []
soma = 0

# Adicionando valores ao vetor notas
for indice in range( QUANTIDADE_NOTAS ):
    notas.append( float(input(f'Digite nota { indice + 1 }: ')) )
    soma += notas[ indice ]


media = soma / QUANTIDADE_NOTAS

print(f"Média: {media:.2f}")