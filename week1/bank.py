def main():
    x = str(input("Greeting: "))
    print(f"${value(x)}")

def value(n):
    if n == "Hello" or n == "hello" or n == " Hello " or n == "Hello, Newman":
        return 0
    else:
        match n[0]:
            case "h" | "H" :
                return 20
            case _:
                return 100

if __name__ == '__main__':
    main()
