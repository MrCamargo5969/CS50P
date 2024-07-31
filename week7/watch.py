import re
import sys

def main():
    id_link = parse(input("HTML: "))
    print(f'-> {id_link}')
    sys.exit(0)

def parse(s):
    if matches := re.search(r'(?<=\W)(http://www.)?youtube\.com/embed/([a-zA-Z0-9_-]+)(?=\W)', s):
        link_return = f'https://youtu.be/{matches.group(2)}'
        return link_return
    else:
        return None

if __name__ == "__main__":
    main()
