from attributes.background_color import get_bg_color_info
from attributes.start_date_day import get_start_day_info

user_choice = {"start_day": "monday",
               "bg_color": "light"}

start_day_info = get_start_day_info(user_choice["start_day"])
orig_week_list = start_day_info["week_list"]
orig_start_month = start_day_info["start_month"]
orig_start_date = start_day_info["start_date"]
orig_start_day = start_day_info["start_day"]
orig_lunar_calender_count = start_day_info["lunar_calender_count"]
orig_lunar_diary_count = start_day_info["lunar_diary_count"]
orig_start_week = start_day_info["start_week"]
orig_week_number = start_day_info["week_number"]

bg_color_info = get_bg_color_info(user_choice["bg_color"])
orig_font_color_section = bg_color_info["font_color_section"]
orig_font_color_page_title = bg_color_info["font_color_page_title"]
orig_font_color_C = bg_color_info["font_color_C"]
orig_nav_bg_color = bg_color_info["nav_bg_color"]
orig_nav_bg_font_color = bg_color_info["nav_bg_font_color"]