from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.set_titles import set_page_title
from units.set_elements import set_date_element,set_lunar_element
from units.weekday import date_type,day_type
from set_attribute import orig_start_date, orig_start_month, orig_start_day
from set_attribute import orig_lunar_diary_count
from set_attribute import user_choice
from attributes.language import lunar_content

def create_miniplanner_slides(prs, ppt_count):
    lunar_count = orig_lunar_diary_count
    today = orig_start_month
    today2 = orig_start_month
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
                if user_choice["language"] == "holiday":
                    date_details = date_type(today2)
                    set_date_element(slide,today2.strftime("%#d"),side_left, side_top, width, height,None,date_details[2])
                    set_date_element(slide,today2.strftime("%a")[0],side_left+width, side_top, width, height,None,date_details[2])
                else:
                    set_date_element(slide,today2.strftime("%#d"),side_left, side_top, width, height)
                    set_date_element(slide,today2.strftime("%a")[0],side_left+width, side_top, width, height)
                today2 += timedelta(days=1)
            else:
                set_date_element(slide,"/",side_left, side_top, width, height)
                set_date_element(slide,"/",side_left+width, side_top, width, height)
            side_top += height
        mini_day_top = Pt(103)
        mini_day_left = Pt(212)
        mini_day_width = Pt(60)
        for j in range(7):
            if user_choice["language"] == "holiday":
                date_details = day_type(day)
                set_date_element(slide,day.strftime("%a"),mini_day_left+mini_day_width*j, mini_day_top, mini_day_width, height,None,date_details[2])
            else:
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
            if user_choice["language"] == "holiday":
                date_details = date_type(today)
                set_date_element(slide,today.strftime("%#d"),mini_left, mini_top, width, height,None,date_details[2])
            else:
                set_date_element(slide,today.strftime("%#d"),mini_left, mini_top, width, height)
            if orig_lunar_diary_count != None:
                if user_choice["language"] == "holiday":
                    date_details = date_type(today)
                    set_lunar_element(slide,f"{lunar_content[lunar_count]}\n{date_details[1]}",mini_left+width*0.6, mini_top+height*0.12, width, height,date_details[2])
                else:
                    set_lunar_element(slide,lunar_content[lunar_count],mini_left+width*0.6, mini_top+height*0.12, width, height)
                lunar_count += 1
            mini_left += width*3
            today += timedelta(days=1)
        this_month += relativedelta(months=1)
    ppt_count += 12
    return ppt_count