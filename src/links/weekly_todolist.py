from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from units.set_elements import set_date_element,set_lunar_element
from units.link_elements import link_date_element
from units.weekday import date_type,day_type
from set_attribute import user_choice
from set_attribute import orig_start_date,orig_start_month
from set_attribute import orig_lunar_calender_count
from attributes.language import lunar_content

def link_todolist_to_diary(prs,m_type_count,w_type_count,diary_page):
    today = orig_start_date
    diary = orig_start_month
    lunar_count = orig_lunar_calender_count
    for slide in prs.slides:
        current_page = prs.slides.index(slide)
        if current_page>=6+13*m_type_count+54*w_type_count:
            break
        if current_page<6+13*m_type_count+54*(w_type_count-1)+1:
            continue
        top = Pt(83)
        left = Pt(152)
        height = Pt(20)
        width = Pt(120)
        min_width = Pt(20)
        for j in range(7):
            day_details = day_type(today)
            date_details = date_type(today)
            set_date_element(slide,today.strftime("%A"),left, top, width, height, None,day_details[2])
            if today>=diary and today<diary+relativedelta(years=1):
                if user_choice["language"] == "holiday":
                    link_date_element(prs,slide,today.strftime("%#d"),left, top+height, min_width, height,None,diary_page,date_details[2])
                else:
                    link_date_element(prs,slide,today.strftime("%#d"),left, top+height, min_width, height,None,diary_page)
                diary_page +=1
            else:
                if user_choice["language"] == "holiday":
                    set_date_element(slide,today.strftime("%#d"),left, top+height, min_width, height,None,date_details[2])
                else:
                    set_date_element(slide,today.strftime("%#d"),left, top+height, min_width, height)
            if orig_lunar_calender_count != None:
                if user_choice["language"] == "holiday":    
                    set_lunar_element(slide,f"{lunar_content[lunar_count]}\n{date_details[1]}",left+min_width*0.6, top+height*1.12, min_width, height,date_details[2])
                else:
                    set_lunar_element(slide,lunar_content[lunar_count],left+min_width*0.6, top+height*1.12, min_width, height)
                lunar_count += 1
            today += timedelta(days=1)
            left += width