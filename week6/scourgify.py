import sys
import os
import csv

valid_extensions = [".csv"]

def main():
    testing(sys.argv)
    dados = convert(sys.argv[1])
    with open(sys.argv[2], 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

def convert(archive):
    with open(archive, 'r') as file:
        csv_ = list(csv.reader(file))

    header = ['first', 'last', 'house']
    dados = [header]
    for linha in csv_:
        if len(linha) >= 2:
            student = linha[0].split(',')
            if len(student) >= 2:
                dados.append([student[1].strip(), student[0], linha[1]])
    return dados


def check_extension(filename, valid_extensions):
    _, ext = os.path.splitext(filename)
    if ext.lower() not in valid_extensions:
        raise ValueError('Not a valid CSV file')
    return filename

def check_existence(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError('File does not exist')
    return filename

def testing(filename):
    if len(filename) <= 2:
        print('Too few command-line arguments')
        sys.exit(1)
    elif len(filename) >= 4:
        print('Too many command-line arguments')
        sys.exit(1)
    else:
        check_extension(filename[1], valid_extensions)
        check_extension(filename[2], valid_extensions)
        check_existence(filename[1])

if __name__ == "__main__":
    main()
