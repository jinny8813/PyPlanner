from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_titles import set_page_title
from units.others import date_type
from set_attribute import orig_start_month
from set_attribute import orig_lunar_diary_count
from set_attribute import orig_template_num
from set_attribute import user_choice
from attributes.language import lunar_content

def create_diary_slides(prs, ppt_count):
    today = orig_start_month
    lunar_count = orig_lunar_diary_count
    while today < orig_start_month+relativedelta(years=1):
        layout = prs.slide_layouts[orig_template_num]
        slide = prs.slides.add_slide(layout)
        if orig_lunar_diary_count != None:
            if user_choice["language"] == "holiday":
                date_details = date_type(today)
                set_page_title(slide,today.strftime("%Y / %m / %d - %A"), f"{lunar_content[lunar_count]} {date_details[1]}",date_details[2])
            else:
                set_page_title(slide,today.strftime("%Y / %m / %d - %A"), lunar_content[lunar_count])
            lunar_count += 1
        else:
            set_page_title(slide,today.strftime("%Y / %m / %d - %A"))
        today += timedelta(days=1)
    ppt_count += (orig_start_month + relativedelta(months=12) - orig_start_month).days
    return ppt_count