import re
import sys


def main():
    um = input("Speak: ")
    num = count(um)
    print(num)


def count(s):
    total = 0
    if count := re.findall(r'\b(um)\b', s, re.I):
        for i in count:
            total += 1
        return total
    else:
        return 0

if __name__ == "__main__":
    main()
