from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_titles import set_page_title
from units.set_elements import set_date_element,set_lunar_element
from set_attribute import orig_start_date, orig_start_month, orig_start_day
from set_attribute import orig_lunar_diary_count
from attributes.language import lunar_content

def create_finances_slides(prs, ppt_count):
    lunar_count = orig_lunar_diary_count
    today = orig_start_month
    today2 = orig_start_month
    day = orig_start_date
    this_month = orig_start_month
    for i in range(12):
        layout = prs.slide_layouts[5]
        slide = prs.slides.add_slide(layout)
        set_page_title(slide,"{} {} Finances".format(this_month.strftime("%Y"),this_month.strftime("%B")))
        height = Pt(20)
        width = Pt(20)
        side_top = Pt(103)
        side_left = Pt(32)
        for j in range(31):
            if j < calendar.monthrange(this_month.year,this_month.month)[1]:
                set_date_element(slide,today2.strftime("%#d"),side_left, side_top, width, height)
                set_date_element(slide,today2.strftime("%a")[0],side_left+width, side_top, width, height)
                today2 += timedelta(days=1)
            else:
                set_date_element(slide,"/",side_left, side_top, width, height)
                set_date_element(slide,"/",side_left+width, side_top, width, height)
            side_top += height
        top = Pt(703)
        left = Pt(282)
        height = Pt(20)
        width = Pt(20)
        for j in range(31):
            if j < calendar.monthrange(this_month.year,this_month.month)[1]:
                set_date_element(slide,str(j+1),left, top, width, height)
            else:
                set_date_element(slide,"/",left, top, width, height)
            left += width
        this_month += relativedelta(months=1)
    ppt_count += 12
    return ppt_count