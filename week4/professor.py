import random

def main():
    point = 0
    level = get_level()
    for i in range(10):
        x, y = generate_integer(level)
        resp = x + y
        for p in range(3):
            try:
                resp_user = int(input(f"{x} + {y} = "))
                if resp == resp_user:
                    point += 1
                    correct = True
                    break
                else:
                    correct = False
                    print("EEE")
            except ValueError:
                print("EEE")
        if correct == False:
            print(f"{x} + {y} = {resp}")
        else:
            continue
    print(f"Pontos: {point}")

def get_level():
    while True:
        try:
            level = int(input("Level: " ))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        return x, y
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        return x, y
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
        return x, y
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
