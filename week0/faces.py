def main():
    i = input()
    y = convert(i)
    print(y)

def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s
main()
