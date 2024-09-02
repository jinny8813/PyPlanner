from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_titles import set_page_title
from units.set_elements import set_date_element,set_lunar_element
from set_attribute import orig_start_week,orig_start_date
from set_attribute import orig_lunar_calender_count
from attributes.language import lunar_content

def create_timeline_slides(prs, ppt_count):
    today = orig_start_date
    this_year = int(today.strftime("%Y"))
    lunar_count = orig_lunar_calender_count
    week_count = orig_start_week
    while today < orig_start_date+relativedelta(years=1):
        layout = prs.slide_layouts[9]
        slide = prs.slides.add_slide(layout)
        if week_count == 1 and orig_start_week !=1:
            this_year += 1        
        set_page_title(slide,"{} Week {} Timeline".format(this_year,week_count))
        top = Pt(83)
        left = Pt(152)
        height = Pt(20)
        width = Pt(120)
        min_width = Pt(20)
        for j in range(7):
            set_date_element(slide,today.strftime("%A"),left, top, width, height)
            set_date_element(slide,today.strftime("%#d"),left, top+height, min_width, height)
            if orig_lunar_calender_count != None:
                set_lunar_element(slide,lunar_content[lunar_count],left+min_width, top+height*1.12, min_width, height)
                lunar_count += 1
            today += timedelta(days=1)
            left += width
        week_count +=1
    ppt_count += 53
    return ppt_count