def main():
    while True:
        try:
            a = input("fração: ")
            r = gauge(convert(a))
            if r == "E" or r == "F" or r[2] == "%":
                print(r)
                break
            else:
                continue
        except:
            continue
        # except ValueError:
        #     print("Valor invalido")
        #     continue
        # except ZeroDivisionError:
        #     print("Zero invalido")
        #     continue
def convert(c):
    x, y = map(int, c.split("/"))
    if x < y or x == y:
        d = x/y * 100
        return d
    else:
        raise ZeroDivisionError

def gauge(p):
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return f"{round(p)}%"

if __name__ == "__main__":
    main()
