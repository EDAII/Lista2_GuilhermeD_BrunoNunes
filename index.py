import os
import sys
import sortfunctions as sortting
import numpy
import scrap as webscrape
import time
import matplotlib.pyplot as plt

csv_disciplines = webscrape.scrape()
code_list = numpy.array(csv_disciplines["Codigo"])
runtime = []


os.system('cls||clear')
print('\033[1m' + '==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
print('Estrutura de Dados 2 - Algoritmos de Ordenação n2\n')
print('\n==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
print("Dados Extraídos do matricula web")
print(csv_disciplines)
print('\n==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
print("Codigos desordenados:\n")
print(code_list)
print('\n==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n')
print('Selecione uma opção: ' + '\n')
print('[1] - Ordenar Codigos')
print('[0] - Sair')
print('')
print('\033[1m' + '==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==\n' + '\033[0m')
option = int(input('>>>'))

while option not in [0, 1]:
    option = int(input("Insira uma opção válida: "))


if option == 1:

    sorted_code = sortting.selectionSort(code_list)

    print("Codigos ordenados - Selection Sort:")
    print(sorted_code)

else:
    sys.exit()






