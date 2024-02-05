def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) and month == 2:
        return 29
    return months[month - 1]


def day_of_year(year, month, day):
    february = 29 if is_year_leap(year) else 28
    months = [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day > months[month - 1] or day < 1:
        return None
    if month > 12 or month < 1:
        return None
    year = abs(year)
    total = 0
    for m in range(1, month):
        total = total + days_in_month(year, m)

    total = total + day
    return total


print(day_of_year(2000, 12, 31))
