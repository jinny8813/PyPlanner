from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from units.set_titles import set_page_title
from units.set_elements import set_date_element
from set_attribute import orig_start_week,orig_start_date,orig_start_month

def create_energy_slides(prs, ppt_count):
    today = today2 = orig_start_date
    this_year = int(orig_start_month.strftime("%Y"))
    week_count = orig_start_week
    while today < orig_start_date+relativedelta(years=1):
        layout = prs.slide_layouts[15]
        slide = prs.slides.add_slide(layout)
        if week_count == 1 and today != orig_start_date:
            this_year += 1        
        set_page_title(slide,"{} Week {} Energy".format(this_year,week_count))
        for j in range(7):
            today += timedelta(days=1)
        height = Pt(20)
        side_left = Pt(32)
        side_top = Pt(443)
        for j in range(7):
            set_date_element(slide,today2.strftime("%#d"),side_left, side_top, height, height)
            set_date_element(slide,today2.strftime("%a")[0],side_left+height, side_top, height, height)
            side_top += height
            today2 += timedelta(days=1)
        week_count +=1
        if week_count>52:
            week_count = 1
    ppt_count += 53
    return ppt_count