# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário


while True:
    try:
       lado = float(input("Digite o valor do quadrado: "))
       area = lado * lado
       dobro = area * 2
   
       break
    except:
      print(f"digite um numero")


print(dobro)
