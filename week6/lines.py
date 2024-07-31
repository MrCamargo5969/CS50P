import sys
import os

valido = [".py"]

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
        num = count_lines(sys.argv[1])
        print(num)
        sys.exit(0)

def extension(arq, val):
    _, ext = os.path.splitext(arq)
    if ext.lower() not in val:
        print('Not a Python file')
        sys.exit(1)
    else:
        return arq

def exist(arq):
    if os.path.exists(arq) != True:
        print('File does not exist')
        sys.exit(1)
    else:
        return arq

def count_lines(arq):
    with open(arq, 'r') as file:
        line = [linha.strip() for linha in file]
        num = len(line) - (sum(1 for linha in line if not linha) + sum(1 for linha in line if linha.startswith("#")))
        return num

if __name__ == "__main__":
    main()

