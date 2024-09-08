from attributes.language import holidays_2025

def date_type(date):
    for holiday in holidays_2025:
        if date == holiday[0]:
            if date.weekday() >= 5:
                return [date, holiday[1], "red"]
            else:
                return holiday
    if date.weekday() >= 5:
        return [date, " ", "red"]
    return [date, " ", "black"]

def day_type(date):
    if date.weekday() >= 5:
        return [date, " ", "red"]
    return [date, " ", "black"]
