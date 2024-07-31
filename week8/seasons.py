from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth_date = input('Date of Birth: ')
    try:
        year, month, day = check_birthday(birth_date)
    except:
        sys.exit('Invalid Date')
    date_of_birth = date(int(year), int(month), int(day))
    date_of_today = date.today()
    diff = date_of_today - date_of_birth
    total_minutes = diff.days * 24 * 60
    output = p.number_to_words(total_minutes, andword="")
    print(f'{output.capitalize()} minutes')

def check_birthday(birth_date):
    if re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', birth_date):
        year, month, day = birth_date.split('-')
        return year, month, day

if __name__ == "__main__":
    main()

# class AgeCalculator:
#     def __init__(self, birth_date):
#         self.birth_date = birth_date

#     def calculate_age_in_minutes(self):
#         age_in_days = (date.today() - self.birth_date).days
#         age_in_minutes = age_in_days * 24 * 60
#         return age_in_minutes

# def main():
#     try:
#         birth_date = input('Date of Birth: ')
#         print(birth_date)
#         age_in_words = check_birthdate(birth_date)
#         print(f'{age_in_words} minutes')
#     except ValueError:
#         print("Invalid date.")
#         sys.exit(1)

# def check_birthdate(birth_date):
#         birth_date = date.fromisoformat(birth_date)
#         calculator = AgeCalculator(birth_date)
#         age_in_minutes = calculator.calculate_age_in_minutes()
#         p = inflect.engine()
#         age_in_words = p.number_to_words(age_in_minutes, andword="")

#         return age_in_words.capitalize()

# if __name__ == "__main__":
#     main()
