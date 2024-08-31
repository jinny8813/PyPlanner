from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from units.set_titles import set_page_title
from units.set_elements import set_date_element
from set_attribute import orig_start_date, orig_start_month

def create_main_calendar_slides(prs, ppt_index_count):
    today = orig_start_date
    this_month = orig_start_month
    for i in range(12):
        layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(layout)
        set_page_title(slide,"{} {} Calendar".format(this_month.strftime("%Y"),this_month.strftime("%B")))
        top = Pt(83)
        left = Pt(152)
        height = Pt(20)
        width = Pt(120)
        for j in range(7):
            set_date_element(slide,today.strftime("%A"),left+width*j, top, width, height)
            today += timedelta(days=1)
        this_month += relativedelta(months=1)
    ppt_index_count += 12
    return ppt_index_count