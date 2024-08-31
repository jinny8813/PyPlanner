from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_titles import set_page_title
from units.set_elements import set_date_element,set_lunar_element
from set_attribute import orig_start_date, orig_start_month, orig_start_day
from set_attribute import orig_lunar_diary_count
from attributes.language import lunar_content

def create_miniplanner_slides(prs, ppt_count):
    lunar_count = orig_lunar_diary_count
    today = orig_start_month
    day = orig_start_date
    this_month = orig_start_month
    for i in range(12):
        layout = prs.slide_layouts[1]
        slide = prs.slides.add_slide(layout)
        set_page_title(slide,"{} {} MiniPlanner".format(this_month.strftime("%Y"),this_month.strftime("%B")))
        height = Pt(20)
        width = Pt(20)
        side_top = Pt(103)
        side_left = Pt(32)
        for j in range(31):
            if j < calendar.monthrange(this_month.year,this_month.month)[1]:
                set_date_element(slide,str(j+1),side_left, side_top, width, height)
            else:
                set_date_element(slide,"/",side_left, side_top, width, height)
            side_top += height
        mini_day_top = Pt(103)
        mini_day_left = Pt(212)
        mini_day_width = Pt(60)
        for j in range(7):
            set_date_element(slide,day.strftime("%a"),mini_day_left+mini_day_width*j, mini_day_top, mini_day_width, height)
            day += timedelta(days=1)
        mini_top = Pt(123)
        mini_left = Pt(212)
        for j in range(calendar.monthrange(this_month.year,this_month.month)[1]):
            if j == 0:
                if orig_start_day == "Monday":
                    mini_left = mini_left + width*3 * this_month.weekday()
                else:
                    mini_left = mini_left + width*3 * (this_month.weekday()+1)
            if mini_left > Pt(592):
                mini_top += height*5
                mini_left = Pt(212)
                if j == 0:
                    mini_top -= height*5
            set_date_element(slide,today.strftime("%#d"),mini_left, mini_top, width, height)
            if orig_lunar_diary_count != None:
                set_lunar_element(slide,lunar_content[lunar_count],mini_left+width, mini_top+height*0.12, width, height)
                lunar_count += 1
            mini_left += width*3
            today += timedelta(days=1)
        this_month += relativedelta(months=1)
    ppt_count += 12
    return ppt_count