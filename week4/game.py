import random as r
import sys
def main():
    while True:
        x = input("Level: ")
        if x.isdigit():
            x = int(x)
            if 0 < x <= 100:
                break
            else:
                continue
        else:
            continue
    n = r.randint(1, x)
    print(n)
    while True:
        y = input("Guess: ")
        if y.isdigit():
            y = int(y)
            if y == n:
                print("Just right!")
                sys.exit()
            elif y > n:
                print("Too large!")
                continue
            elif y < n:
                print("Too small!")
                continue
        else:
            continue
main()
