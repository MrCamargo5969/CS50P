# Plates
def main():
    plate = input("Plate: ")
    if is_valid(plate) is True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) == 2:
        if s[:2].isalpha():
            return True
        else:
            return False

    elif 1 < len(s) < 7:
        if s[:2].isalpha():
            if s[2:].isalpha():
                return True
            else:
            # Verifica se o primeiro numero é diferente de zero
                if s[s.index(next(filter(str.isdigit, s[2:])))] != '0':
                    # Verifica se após um numéro terá uma sequência de numeros
                    if any(char.isdigit() and char for char in s[2:]) and not all(char.isdigit() for char in s[s.index(next(filter(str.isdigit, s[2:]))):]):
                        return False
                    else:
                        return True
                else:
                    return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
