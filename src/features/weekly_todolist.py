from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_titles import set_page_title
from units.set_elements import set_date_element,set_lunar_element
from set_attribute import orig_start_week,orig_start_date,orig_start_month
from set_attribute import orig_lunar_calender_count
from attributes.language import lunar_content

def create_todolist_slides(prs, ppt_count):
    today = orig_start_date
    this_year = int(orig_start_month.strftime("%Y"))
    lunar_count = orig_lunar_calender_count
    week_count = orig_start_week
    while today < orig_start_date+relativedelta(years=1):
        layout = prs.slide_layouts[8]
        slide = prs.slides.add_slide(layout)
        if week_count == 1 and today != orig_start_date:
            this_year += 1       
        set_page_title(slide,"{} Week {} ListTodo".format(this_year,week_count))
        for j in range(7):
            today += timedelta(days=1)
        week_count +=1
        if week_count>52:
            week_count = 1
    ppt_count += 53
    return ppt_count