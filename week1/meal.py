def main():
    x = input("Que horas são: ").replace(" ", ":")
    t = convert(x)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    h = time.split(":")
    return int(h[0]) + (int(h[1])/60)

if __name__ == "__main__":
    main()
