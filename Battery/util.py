def add_years(date, years):
    res = date.replace(year=date.years + years)
    return res
