# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo


numero_1 = int(input("Digite um numero inteiro: "))
numero_2 = int(input("Digite um numero inteiro: "))
numero_3 = float(input("Digite um numero real: "))

calculo_1 = (numero_1 * 2) + numero_2 /2
calculo_2 = (numero_1 * 3) + numero_3
calculo_3 = numero_3 ** 3


print(f"numero: {calculo_1}, {calculo_2}, {calculo_3}")
# print(f"numero : {calculo_1}")
# print(f"numero : {calculo_2}")
# print(f"numero : {calculo_3}")