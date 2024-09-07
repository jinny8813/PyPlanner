from attributes.language import holidays_2025

def date_type(date):
    for holiday in holidays_2025:
        if date == holiday[0]:
            return holiday
    if date.weekday() >= 5:
        return [date, " ", "red"]
    return [date, " ", "black"]
