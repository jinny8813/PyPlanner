from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_titles import set_page_title
from units.set_elements import set_date_element,set_lunar_element
from set_attribute import orig_start_week,orig_start_date,orig_start_month,orig_week_list
from set_attribute import orig_lunar_calender_count
from attributes.language import lunar_content

def create_overview_slides(prs, ppt_count):
    today = today2 = orig_start_date
    this_year = int(orig_start_month.strftime("%Y"))
    lunar_count = orig_lunar_calender_count
    week_count = orig_start_week
    while today < orig_start_date+relativedelta(years=1):
        layout = prs.slide_layouts[12]
        slide = prs.slides.add_slide(layout)
        if week_count == 1 and today != orig_start_date:
            this_year += 1       
        set_page_title(slide,"{} Week {} Overview".format(this_year,week_count))
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
        side_top = Pt(443)
        space = Pt(160)
        for i in range(7):
            side_left = Pt(272)
            for j in range(3):
                set_date_element(slide,today2.strftime("%#d"),side_left, side_top, height, height)
                set_date_element(slide,today2.strftime("%a")[0],side_left+height, side_top, height, height)
                side_left += space
            today2 += timedelta(days=1)
            side_top += height
        down_top = Pt(423)
        dwon_left = Pt(132)
        for k in orig_week_list:
            set_date_element(slide,k,dwon_left, down_top, height, height)
            dwon_left += height
        week_count +=1
        if week_count>52:
            week_count = 1
    ppt_count += 53
    return ppt_count