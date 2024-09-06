from attributes.background_color import get_bg_color_info
from attributes.start_date_day import get_start_day_info
from attributes.theme_colors import get_theme_colors_info
from attributes.diary_type import get_diary_type_info

user_choice = {"start_day": "monday",
               "bg_color": "light",
               "language": "lunar",
               "theme_colors": "mint",
               "diary_type": "plentifulboth"}

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
orig_font_color_element = bg_color_info["font_color_element"]
orig_nav_bg_color = bg_color_info["nav_bg_color"]
orig_nav_bg_font_color = bg_color_info["nav_bg_font_color"]

if user_choice["language"] != "lunar":
    orig_lunar_calender_count = None
    orig_lunar_diary_count = None

theme_colors_info = get_theme_colors_info(user_choice["theme_colors"])
orig_theme_colors = theme_colors_info["colors"]

diary_type_info = get_diary_type_info(user_choice["diary_type"])
orig_template_num = diary_type_info["template_num"]
orig_selected_w_types = diary_type_info["selected_w_types"]
orig_selected_c_types = diary_type_info["selected_c_types"]