import sys
import os
import csv
from tabulate import tabulate

valido = [".csv"]

def main():
    if len(sys.argv) <= 1:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(sys.argv) >= 3:
        print('Too many command-line arguments')
        sys.exit(1)
    else:
        extension(sys.argv[1], valido)
        exist(sys.argv[1])
        print(csv_to_asc2_table(sys.argv[1]))
        sys.exit(0)
# Valida a extensão
def extension(arq, val):
    _, ext = os.path.splitext(arq)
    if ext.lower() not in val:
        print('Not a Python file')
        sys.exit(1)
    else:
        return arq
# Verifica se existe
def exist(arq):
    if os.path.exists(arq) != True:
        print('File does not exist')
        sys.exit(1)
    else:
        return arq
# Transforma em uma tabela ASCII
def csv_to_asc2_table(arq):
    # Abre o arquivo CSV em modo de leitura
    with open(arq, 'r') as file:
        reader = csv.reader(file)
        table = list(reader)
    head = table[0]
    data = table[1:]

    return tabulate(data, headers=head, tablefmt='grid')

if __name__ == "__main__":
    main()
