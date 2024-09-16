from datetime import date,datetime

def get_start_day_info(start_day):
    select_start_day = {
        "monday": {
            "week_list": ['M','T','W','T','F','S','S'],
            "start_time": datetime(2025, 1, 1, 5, 0),
            "start_time_2": datetime(2024, 12, 30, 5, 0),
            "start_month": date(2025, 1, 1),
            "start_date": date(2024, 12, 30),
            "start_day": "Monday",
            "lunar_calender_count": 365,
            "lunar_diary_count": 367,
            "start_week": 1,
            "week_number":[
                    [1, 2, 3, 4, 5],
                    [5, 6, 7, 8, 9],
                    [9, 10, 11, 12, 13, 14],
                    [14, 15, 16, 17, 18],
                    [18, 19, 20, 21, 22],
                    [22, 23, 24, 25, 26, 27],
                    [27, 28, 29, 30, 31],
                    [31, 32, 33, 34, 35],
                    [36, 37, 38, 39, 40],
                    [40, 41, 42, 43, 44],
                    [44, 45, 46, 47, 48],
                    [49, 50, 51, 52, 53]]
        },
        "sunday": {
            "week_list": ['S','M','T','W','T','F','S'],
            "start_time": datetime(2025, 1, 1, 5, 0),
            "start_time_2": datetime(2024, 12, 29, 5, 0),
            "start_month": date(2025, 1, 1),
            "start_date": date(2024, 12, 29),
            "start_day": "Sunday",
            "lunar_calender_count": 364,
            "lunar_diary_count": 367,
            "start_week": 1,
            "week_number":[
                    [1, 2, 3, 4, 5],
                    [5, 6, 7, 8, 9],
                    [9, 10, 11, 12, 13, 14],
                    [14, 15, 16, 17, 18],
                    [18, 19, 20, 21, 22],
                    [23, 24, 25, 26, 27],
                    [27, 28, 29, 30, 31],
                    [31, 32, 33, 34, 35, 36],
                    [36, 37, 38, 39, 40],
                    [40, 41, 42, 43, 44],
                    [44, 45, 46, 47, 48, 49],
                    [49, 50, 51, 52, 53]]
        },
        "monday202401": {
            "week_list": ['M','T','W','T','F','S','S'],
            "start_time": datetime(2024, 1, 1, 5, 0),
            "start_time_2": datetime(2024, 1, 1, 5, 0),
            "start_month": date(2024, 1, 1),
            "start_date": date(2024, 1, 1),
            "start_day": "Monday",
            "lunar_calender_count": 1,
            "lunar_diary_count": 1,
            "start_week": 1,
            "week_number":[
                    [1, 2, 3, 4, 5],
                    [5, 6, 7, 8, 9],
                    [9, 10, 11, 12, 13],
                    [14, 15, 16, 17, 18],
                    [18, 19, 20, 21, 22],
                    [22, 23, 24, 25, 26],
                    [27, 28, 29, 30, 31],
                    [31, 32, 33, 34, 35],
                    [35, 36, 37, 38, 39, 40],
                    [40, 41, 42, 43, 44],
                    [44, 45, 46, 47, 48],
                    [48, 49, 50, 51, 52, 53]]
        },
    }
    return select_start_day[start_day]