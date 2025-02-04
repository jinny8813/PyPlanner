from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_titles import set_page_title
from units.set_elements import set_date_element
from units.weekday import date_type
from set_attribute import user_choice
from set_attribute import orig_start_month

def create_project_slides(prs, ppt_count):
    today = orig_start_month
    this_month = orig_start_month
    for i in range(12):
        layout = prs.slide_layouts[2]
        slide = prs.slides.add_slide(layout)
        set_page_title(slide,"{} {} Project".format(this_month.strftime("%Y"),this_month.strftime("%B")))
        top = Pt(483)
        left = Pt(192)
        height = Pt(20)
        width = Pt(20)
        for j in range(32):
            if j < calendar.monthrange(this_month.year,this_month.month)[1]:
                if user_choice["language"] == "holiday":
                    date_details = date_type(today)
                    set_date_element(slide,today.strftime("%#d"),left, top, width, height,None,date_details[2])
                    set_date_element(slide,today.strftime("%a")[0],left, top+height, width, height,None,date_details[2])
                else:
                    set_date_element(slide,today.strftime("%#d"),left, top, width, height)
                    set_date_element(slide,today.strftime("%a")[0],left, top+height, width, height)
                today += timedelta(days=1)
            else:
                set_date_element(slide,"/",left, top, width, height)
                set_date_element(slide,"/",left, top+height, width, height)
            left += width
        this_month += relativedelta(months=1)
    ppt_count += 12
    return ppt_count