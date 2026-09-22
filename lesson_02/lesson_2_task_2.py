def is_year_leap(year: int) -> bool:
    return year % 4 == 0


years_to_check = [2020, 2021, 2022, 2023, 2024]


for year in years_to_check:
    result = is_year_leap(year)
    print(f"год {year}: {result}")
