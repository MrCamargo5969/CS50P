f = {
    "bajataco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "superburrito": 8.50,
    "superquesadilla": 9.50,
    "taco": 3.00,
    "tortillasalad": 8.00
}
total = 0
while True:
    try:
        t = input("O que deseja? -> ").lower().replace(" ", "")
        if t in f:
            total += f[t]
            print(f"Total: ${total:.2f}")
        elif t == "fim" or t == "sair":
            print(f"Total: ${total:.2f}")
            break
        else:
            continue
    except EOFError:
        print("\nFIM (EOF).")
        break
