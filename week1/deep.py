x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").replace(" ", "")

match x:
    case "42" | "forty-two" | "fortytwo" | "FoRtyTwO" | "          42          ":
        print("Yes")
    case _:
        print("No")
