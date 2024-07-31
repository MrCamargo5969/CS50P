a = 50
print(f"Amount Due: {a}")
def main():
    while True:
        x = input("Insert Coin: ")
        if x.isdigit():
            x = int(x)
            if x not in [25, 10, 5]:
                print(f"Amount Due: {a}")
                continue
            d = count(x)
            if d >= 0:
                if d > 0:
                    print(f"Amount Due: {d}")
                else:
                    print(f"Change Owed: {-d}")
                    break
            else:
                print(f"Change Owed: {-d}")
                break
        else:
            continue

def count(b):
    global a
    a -= b
    return a
main()
