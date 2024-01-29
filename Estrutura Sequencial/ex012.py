# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58


altura = float(input("Digite sua altura: "))

peso_ideal = (72.7 * altura) - 58

# round funcão Arredondando números em Python. Podemos tambem usar :.2f ao imprimir o resultado
# peso_ideal = round(peso_ideal, 2)

print(f"Seu peso ideal e: {peso_ideal:.2f}")

