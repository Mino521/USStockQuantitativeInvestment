def check_continue_year(years, start_year, end_year):
    for year in range(start_year, end_year):
        if year not in years:
            return 0
    return 1


def check_quarter(days):
    if days < 100:
        return 1
    elif days < 190:
        return 2
    elif days < 280:
        return 3
    else:
        return 4