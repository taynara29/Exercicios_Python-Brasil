# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura: "))

peso_ideal_f = (72.7 * altura) - 58
peso_ideal_m = (72.7 * altura) - 44.7


print(f"Seu peso ideal feminino: {peso_ideal_f:.2f}")
print(f"Seu peso ideal masculino: {peso_ideal_m:.2f}")
