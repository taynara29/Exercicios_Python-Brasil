# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
import calendar
import numpy as np


hora = int(input("digite o valor da sua hora de trabalho: "))
ano =  int(input("Digite o ano vigente: "))
mes =  int(input("digite o mes vigente "))

# último dia do mês
ultimo_dia_mes = calendar.monthrange (ano,mes)[1]

# Crie as datas de início e término
data_inicio = f'{ano}-{mes:02d}-01'  # Primeiro dia do mês
data_fim = f'{ano}-{mes:02d}-{ultimo_dia_mes}'  # Último dia do mês

# Calcule os dias úteis entre as datas
dias_uteis = np.busday_count(data_inicio, data_fim)

salario = hora * 22

print(salario)


