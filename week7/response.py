import validators
def main():
    response = input("What's your email address? ")
    print(validate(response))

def validate(s):
    # if matches := re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", s):
    if validators.email(s):
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == "__main__":
    main()
