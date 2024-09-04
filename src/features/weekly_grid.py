from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_titles import set_page_title
from units.set_elements import set_date_element,set_lunar_element,set_date_element_grid
from set_attribute import orig_start_week,orig_start_date,orig_start_month
from set_attribute import orig_lunar_calender_count
from attributes.language import lunar_content

def create_grid_slides(prs, ppt_count):
    today = orig_start_date
    this_year = int(orig_start_month.strftime("%Y"))
    lunar_count = orig_lunar_calender_count
    week_count = orig_start_week
    while today < orig_start_date+relativedelta(years=1):
        layout = prs.slide_layouts[10]
        slide = prs.slides.add_slide(layout)
        if week_count == 1 and today != orig_start_date:
            this_year += 1        
        set_page_title(slide,"{} Week {} Grid".format(this_year,week_count))
        top = Pt(88)
        left = Pt(272)
        height = Pt(40)
        width = Pt(40)
        min_width = Pt(20)
        min_height = Pt(20)
        down_top = Pt(408)
        space = Pt(240)
        for j in range(7):
            if j<3:
                set_date_element_grid(slide,today.strftime("%#d"),left, top, width, height)
                if orig_lunar_calender_count != None:
                    set_lunar_element(slide,lunar_content[lunar_count],left+width, top+min_height*0.18, min_width, min_height)
                    lunar_count += 1
                set_date_element(slide,today.strftime("%a"),left, top+height*0.75, width, min_height)
            else:
                set_date_element_grid(slide,today.strftime("%#d"),left, down_top, width, height)
                if orig_lunar_calender_count != None:
                    set_lunar_element(slide,lunar_content[lunar_count],left+width, down_top+min_height*0.18, min_width, min_height)
                    lunar_count += 1
                set_date_element(slide,today.strftime("%a"),left, down_top+height*0.75, width, min_height)
            today += timedelta(days=1)
            if j==2:
                left -= space*3
            else:
                left += space
        week_count +=1
        if week_count>52:
            week_count = 1
    ppt_count += 53
    return ppt_count