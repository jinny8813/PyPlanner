from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_elements import set_lunar_element
from units.link_elements import link_date_element
from set_attribute import orig_start_month,orig_start_day
from set_attribute import orig_lunar_diary_count
from attributes.language import lunar_content

def link_calendar_to_diary(prs,diary_page):
    today = orig_start_month
    this_month = orig_start_month
    lunar_count = orig_lunar_diary_count
    for slide in prs.slides:
        current_page = prs.slides.index(slide)
        if current_page>=6+12+1:
            break
        if current_page<6+1:
            continue
        top = Pt(103)
        left = Pt(152)
        height = Pt(20)
        width = Pt(20)
        for j in range(calendar.monthrange(this_month.year,this_month.month)[1]):
            if j == 0:
                if orig_start_day == "Monday":
                    left = left + width*6 * this_month.weekday()
                else:
                    left = left + width*6 * (this_month.weekday()+1)
            if left > Pt(872):
                top += height*5
                left = Pt(152)
                if j == 0:
                    top -= height*5
            link_date_element(prs,slide,today.strftime("%#d"),left, top, width, height,None,diary_page)
            if orig_lunar_diary_count != None:
                set_lunar_element(slide,lunar_content[lunar_count],left+width, top+height*0.12, width, height)
                lunar_count += 1
            left += width*6
            today += timedelta(days=1)
            diary_page += 1
        this_month += relativedelta(months=1)