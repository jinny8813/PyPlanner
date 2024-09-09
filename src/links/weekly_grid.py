from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import calendar

from units.link_elements import link_date_element_grid
from units.set_elements import set_date_element,set_lunar_element,set_date_element_grid
from units.weekday import date_type,day_type
from set_attribute import user_choice
from set_attribute import orig_start_date,orig_start_month
from set_attribute import orig_lunar_calender_count
from attributes.language import lunar_content

def link_grid_to_diary(prs,m_type_count,w_type_count,diary_page):
    today = orig_start_date
    lunar_count = orig_lunar_calender_count
    diary = orig_start_month
    for slide in prs.slides:
        current_page = prs.slides.index(slide)
        if current_page>=6+13*m_type_count+54*w_type_count:
            break
        if current_page<6+13*m_type_count+54*(w_type_count-1)+1:
            continue
        top = Pt(88)
        left = Pt(272)
        height = Pt(40)
        width = Pt(40)
        min_width = Pt(20)
        min_height = Pt(20)
        down_top = Pt(408)
        space = Pt(240)
        for j in range(7):
            date_details = date_type(today)
            if j<3:
                if today>=diary and today<diary+relativedelta(years=1):
                    if user_choice["language"] == "holiday":
                        link_date_element_grid(prs,slide,today.strftime("%#d"),left, top, width, height,diary_page,date_details[2])
                    else:
                        link_date_element_grid(prs,slide,today.strftime("%#d"),left, top, width, height,diary_page)
                    diary_page +=1
                else:
                    if user_choice["language"] == "holiday":
                        set_date_element_grid(slide,today.strftime("%#d"),left, top, width, height,date_details[2])
                    else:
                        set_date_element_grid(slide,today.strftime("%#d"),left, top, width, height)
                if orig_lunar_calender_count != None:
                    if user_choice["language"] == "holiday":
                        set_lunar_element(slide,f"{lunar_content[lunar_count]} {date_details[1]}",left+width, top+min_height*0.18, min_width, min_height,date_details[2])
                    else:
                        set_lunar_element(slide,f"{lunar_content[lunar_count]} {date_details[1]}",left+width, top+min_height*0.18, min_width, min_height)
                    lunar_count += 1
                if user_choice["language"] == "holiday":
                    set_date_element(slide,today.strftime("%a"),left, top+height*0.75, width, min_height,None,date_details[2])
                else:
                    set_date_element(slide,today.strftime("%a"),left, top+height*0.75, width, min_height)
            else:
                if today>=diary and today<diary+relativedelta(years=1):
                    if user_choice["language"] == "holiday":
                        link_date_element_grid(prs,slide,today.strftime("%#d"),left, down_top, width, height,diary_page,date_details[2])
                    else:
                        link_date_element_grid(prs,slide,today.strftime("%#d"),left, down_top, width, height,diary_page)
                    diary_page +=1
                else:
                    if user_choice["language"] == "holiday":
                        set_date_element_grid(slide,today.strftime("%#d"),left, down_top, width, height,date_details[2])
                    else:
                        set_date_element_grid(slide,today.strftime("%#d"),left, down_top, width, height)
                if orig_lunar_calender_count != None:
                    if user_choice["language"] == "holiday":
                        set_lunar_element(slide,f"{lunar_content[lunar_count]} {date_details[1]}",left+width, down_top+min_height*0.18, min_width, min_height,date_details[2])
                    else:
                        set_lunar_element(slide,f"{lunar_content[lunar_count]} {date_details[1]}",left+width, down_top+min_height*0.18, min_width, min_height)
                    lunar_count += 1
                if user_choice["language"] == "holiday":
                    set_date_element(slide,today.strftime("%a"),left, down_top+height*0.75, width, min_height,None,date_details[2])
                else:
                    set_date_element(slide,today.strftime("%a"),left, down_top+height*0.75, width, min_height)
            today += timedelta(days=1)
            if j==2:
                left -= space*3
            else:
                left += space