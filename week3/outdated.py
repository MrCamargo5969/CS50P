import re
def main():
    i = {"january":"01", "february":"02", "march":"03", "april":"04",
          "may":"05", "june":"06", "july":"07", "august":"08",
          "september":"09", "october":"10", "november":"11", "december":"12"}
    while True:
        date = input("Digite uma data: ").lower().replace('"',"").strip()

        if re.match(r'^\d{1,2}\/\d{1,2}\/\d{4}$', date): #Verifica se a entrada é do formato "digito/digito/digito"
            d = re.split(r'[\/\s]+', date)
            if int(d[0]) in range(1,13) and int(d[1]) in range(1,30) and int(d[2]) in range(1,9999):
                print(f"{int(d[2]):04d}-{int(d[0]):02d}-{int(d[1]):02d}")
                break

        elif re.match(r'^\w+\s\d{1,2},\s\d{4}$', date): #Verifica se a entrada é do formato "alpha digito, digito"
            d = re.split(r'[\/\s]+', date.replace(",",""))
            if d[1].isdigit() and int(d[1]) in range(1,30) and int(d[2]) in range(1,9999):
                print(f"{int(d[2]):04d}-{i[d[0]]}-{int(d[1]):02d}")
                break

        else:
            continue

main()
