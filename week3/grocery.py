def main():
    try:
        l = []
        c ={}
        while True:
            g = input().upper()
            if g == "":
                break
            else:
                l.append(g)

    except EOFError:
        for i in l:
            c[i] =c.get(i, 0) + 1
        for i in sorted(c.keys()):
            print(f"{c[i]} {i}")

main()

