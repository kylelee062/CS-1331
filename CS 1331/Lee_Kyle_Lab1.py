def isLeapYear(user_year):
    leap_year = True
    if (user_year % 4 == 0) and (user_year % 10 != 0) or (user_year % 400 == 0):
        print(f"{user_year} - leap year")
    else:
        print(f"{user_year} - is not leap year")
    return leap_year

year = int(input())
isLeapYear(year)