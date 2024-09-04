from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_titles import set_page_title
from units.set_elements import set_date_element,set_small_calendar
from set_attribute import orig_start_month,orig_week_list

def create_tracker_slides(prs, ppt_count):
    today = orig_start_month
    this_month = orig_start_month
    for i in range(12):
        layout = prs.slide_layouts[3]
        slide = prs.slides.add_slide(layout)
        set_page_title(slide,"{} {} Tracker".format(this_month.strftime("%Y"),this_month.strftime("%B")))
        top = Pt(483)
        left = Pt(192)
        height = Pt(20)
        width = Pt(20)
        for j in range(32):
            if j < calendar.monthrange(this_month.year,this_month.month)[1]:
                set_date_element(slide,today.strftime("%#d"),left, top, width, height)
                set_date_element(slide,today.strftime("%a")[0],left, top+height, width, height)
                today += timedelta(days=1)
            else:
                set_date_element(slide,"/",left, top, width, height)
                set_date_element(slide,"/",left, top+height, width, height)
            left += width
        for c in range(6):
            if c < 3:
                small_top = Pt(123)
            else:
                small_top = Pt(303)
            if c%3 == 1:
                small_left = Pt(52)
            elif c%3 == 2:
                small_left = Pt(372)
            else:
                small_left = Pt(692)
            set_small_calendar(slide,this_month,small_left, small_top,orig_week_list)
        this_month += relativedelta(months=1)
    ppt_count += 12
    return ppt_count