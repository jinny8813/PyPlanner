from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_titles import set_page_title
from units.set_elements import set_date_element,set_lunar_element
from units.weekday import date_type,day_type
from set_attribute import user_choice
from set_attribute import orig_start_month,orig_lunar_diary_count,orig_start_date,orig_start_day
from attributes.language import lunar_content

def create_gallery_slides(prs, ppt_count):
    lunar_count = orig_lunar_diary_count
    today = orig_start_month
    day = orig_start_date
    this_month = orig_start_month
    for i in range(12):
        layout = prs.slide_layouts[4]
        slide = prs.slides.add_slide(layout)
        set_page_title(slide,"{} {} Gallery".format(this_month.strftime("%Y"),this_month.strftime("%B")))
        height = Pt(20)
        width = Pt(20)
        day_top = Pt(93)
        day_left = Pt(92)
        day_width = Pt(120)
        for j in range(7):
            if user_choice["language"] == "holiday":
                date_details = day_type(day)
                set_date_element(slide,day.strftime("%A"),day_left+day_width*j, day_top, day_width, height,None,date_details[2])
            else:
                set_date_element(slide,day.strftime("%A"),day_left+day_width*j, day_top, day_width, height)
            day += timedelta(days=1)
        top = Pt(113)
        left = Pt(92)
        for j in range(calendar.monthrange(this_month.year,this_month.month)[1]):
            if j == 0:
                if orig_start_day == "Monday":
                    left = left + width*6 * this_month.weekday()
                else:
                    left = left + width*6 * (this_month.weekday()+1)
            if left > Pt(812):
                top += height*5
                left = Pt(92)
                if j == 0:
                    top -= height*5
            if user_choice["language"] == "holiday":
                date_details = date_type(today)
                set_date_element(slide,today.strftime("%#d"),left, top, width, height,None,date_details[2])
            else:
                set_date_element(slide,today.strftime("%#d"),left, top, width, height)
            if orig_lunar_diary_count != None:
                if user_choice["language"] == "holiday":
                    date_details = date_type(today)
                    set_lunar_element(slide,f"{lunar_content[lunar_count]}\n{date_details[1]}",left+width*0.6, top+height*0.12, width, height,date_details[2])
                else:
                    set_lunar_element(slide,lunar_content[lunar_count],left+width*0.6, top+height*0.12, width, height)
                lunar_count += 1
            left += width*6
            today += timedelta(days=1)
        this_month += relativedelta(months=1)
    ppt_count += 12
    return ppt_count