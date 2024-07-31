def main():
    try:
        l = []
        s = "Adieu, adieu, to"
        while True:
            a = input()
            if a == "":
                break
            else:
                l.append(a)
    except EOFError:
        print("error")

    for e, i in enumerate(l):
        if len(l) > 2:
            if e == len(l) - 1:
                s = f"{s} and {i}"
            else:
                s = f"{s} {i},"
        elif len(l) == 2:
            if e == len(l) - 1:
                s = f"{s} and {i}"
            else:
                s = f"{s} {i}"
        else:
            s = f"{s} {i}"
    print(s)


main()
