import re
import sys

def main():
    input_ = input("Hours: ")
    time = convert(input_)
    print(time)

def convert(s):
    format_time = []
    if matches := re.findall(r'\b\sto\s', s, re.I):
        if matches := re.findall(r'(\b\d{1,2}):?(\d{1,2})?(\s{1}(AM|PM))?\b', s, re.I):
            for match in matches:
                hour = match[0]
                min = match[1] if match[1] else '00'
                am_pm = match[2]
                hour = int(hour)
                if len(min) == 1 or int(min) >= 60 or hour > 12:
                    raise ValueError("Invalido")
                if am_pm and am_pm.strip() in ['PM', 'pm'] and hour < 12:
                    hour += 12
                if am_pm and am_pm.strip() in ['AM', 'am'] and hour == 12:
                    hour = 0
                time = f'{hour:02}:{min}'
                format_time.append(time)

            time1, time2 = format_time[0], format_time[1]
            return f'{time1} to {time2}'
        else:
            raise ValueError("complicou")
    else:
        raise ValueError("complicou")

if __name__ == "__main__":
    main()
