from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from units.set_elements import set_date_element
from units.link_elements import link_date_element
from set_attribute import orig_start_date,orig_start_month
from set_attribute import orig_lunar_calender_count
from attributes.language import lunar_content

def link_energy_to_diary(prs,m_type_count,w_type_count,diary_page):
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
        left = Pt(392)
        height = Pt(20)
        width = Pt(200)
        down_top = Pt(403)
        space = Pt(200)
        for j in range(7):
            if j<3:
                if orig_lunar_calender_count != None:                    
                    if today>=diary and today<diary+relativedelta(years=1):
                        link_date_element(prs,slide,today.strftime("%#m/%#d - %a"),left, top, width, height,lunar_content[lunar_count], diary_page)
                        diary_page +=1
                    else:
                        set_date_element(slide,today.strftime("%#m/%#d - %a"),left, top, width, height,lunar_content[lunar_count])
                    lunar_count += 1
                else:
                    if today>=diary and today<diary+relativedelta(years=1):
                        link_date_element(prs,slide,today.strftime("%#m/%#d - %a"),left, top, width, height,None, diary_page)
                        diary_page +=1
                    else:
                        set_date_element(slide,today.strftime("%#m/%#d - %a"),left, top, width, height)
            else:
                if orig_lunar_calender_count != None:                    
                    if today>=diary and today<diary+relativedelta(years=1):
                        link_date_element(prs,slide,today.strftime("%#m/%#d - %a"),left, down_top, width, height,lunar_content[lunar_count], diary_page)
                        diary_page +=1
                    else:
                        set_date_element(slide,today.strftime("%#m/%#d - %a"),left, down_top, width, height,lunar_content[lunar_count])
                    lunar_count += 1
                else:
                    if today>=diary and today<diary+relativedelta(years=1):
                        link_date_element(prs,slide,today.strftime("%#m/%#d - %a"),left, down_top, width, height,None, diary_page)
                        diary_page +=1
                    else:
                        set_date_element(slide,today.strftime("%#m/%#d - %a"),left, down_top, width, height)
            today += timedelta(days=1)
            if j==2:
                left -= space*3
            else:
                left += space