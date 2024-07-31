import re
import sys

def main():
    valid = validate(input("IPv4 Address: ").strip())
    if valid:
        print(valid)
        sys.exit(0)
    else:
        print(valid)
        sys.exit(1)


def validate(ip):
    if matches := re.search(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip):
        return True
    return False

...


if __name__ == "__main__":
    main()
