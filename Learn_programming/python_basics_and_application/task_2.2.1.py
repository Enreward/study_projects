from datetime import date, datetime, timedelta

if __name__ == '__main__':
    year, month, day = map(int, input().strip().split(' '))
    days = int(input())
    input_date = date(year, month, day)
    new_date = input_date + timedelta(days=days)
    print(new_date.year, new_date.month, new_date.day)
