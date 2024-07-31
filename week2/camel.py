def main():
    x = input("camelCase: ")
    for c in x:
        if c.isupper():
            x = convert(x)
        else:
            continue
    print(f"snake_case: {x}")

def convert(n):
    for c in n:
        if c.isupper():
            n = n.replace(c, f"_{c.lower()}")
            return n
main()
