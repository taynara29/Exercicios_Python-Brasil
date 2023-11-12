#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('Digite nota 1 '))
nota2 = float(input('Digite nota 2 '))
nota3 = float(input('Digite nota 3 '))
nota4 = float(input('Digite nota 4 '))

soma = nota1 + nota2 + nota3 + nota4

media = soma / 4

print(f"Média: {media:.2f}")