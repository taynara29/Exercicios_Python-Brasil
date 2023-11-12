# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

while True:
    try:
        temperatura = float(input("Informe a temperatura em graus Fahrenheit: "))
        celsius = 5 * temperatura-32 / 9
        break
    except:
        print("Invalido. Por favor digite um numero!")

print(celsius)


