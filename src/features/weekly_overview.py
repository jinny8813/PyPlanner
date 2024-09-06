from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from units.set_titles import set_page_title
from units.set_elements import set_date_element
from set_attribute import orig_start_week,orig_start_date,orig_start_month,orig_week_list

def create_overview_slides(prs, ppt_count):
    today = today2 = orig_start_date
    this_year = int(orig_start_month.strftime("%Y"))
    week_count = orig_start_week
    while today < orig_start_date+relativedelta(years=1):
        layout = prs.slide_layouts[12]
        slide = prs.slides.add_slide(layout)
        if week_count == 1 and today != orig_start_date:
            this_year += 1       
        set_page_title(slide,"{} Week {} Overview".format(this_year,week_count))
        for i in range(7):
            today += timedelta(days=1)
        side_top = Pt(443)
        space = Pt(160)
        height = Pt(20)
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