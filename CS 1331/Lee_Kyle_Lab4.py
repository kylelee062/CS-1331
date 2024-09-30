class Age:
    def __init__(self, years, months, days):
        self.years = years
        self.months = months
        self.days = days

    def __str__(self):
        return f"{self.years} years, {self.months} months, {self.days} days"
    
    def __add__(self, other):
        total_years = self.years + other.years
        total_months = self.months + other.months
        total_days = self.days + other.days

        if total_days >= 30:
            total_months += total_days // 30
            total_days %= 30

        if total_months >= 12:
            total_years += total_months // 12
            total_months %= 12

        return Age(total_years, total_months, total_days)

age1 = Age(2, 3, 22)
age2 = Age(3, 4, 2)
age3 = Age(10, 8, 10)

print(age1 + age2)
print(age1 + age3)