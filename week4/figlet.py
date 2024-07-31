from pyfiglet import Figlet
import sys
figlet = Figlet()

if len(sys.argv) != 3:
    sys.exit(1)

else:
    if sys.argv[1] in ("-f", "--font"):
        if sys.argv[2] not in figlet.getFonts():
            sys.exit(1)
        else:
            f = input('input: ')
            r = figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(f))
    else:
        sys.exit(1)

