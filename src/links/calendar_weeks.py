from pptx.util import Pt

from units.set_elements import set_date_element
from units.link_elements import link_calendar_weeks
from set_attribute import orig_week_number
from set_attribute import orig_selected_w_types,orig_selected_m_types

def link_calendar_to_weeks(prs,diary_page):
    week_count = 0
    verify_num = 0
    for slide in prs.slides:
        current_page = prs.slides.index(slide)
        if current_page>=6+12+1:
            break
        if current_page<6+1:
            continue
        top = Pt(103)
        left = Pt(32)
        height = Pt(20)
        width = Pt(120)
        min_top = Pt(123)
        min_height = Pt(20)
        min_width = Pt(15)
        for num in orig_week_number[current_page-6-1]:
            set_date_element(slide,f"Week {num}",left, top, width, height)
            if verify_num == num or verify_num==53:
                week_count -=1
            min_left = Pt(89)-len(orig_selected_w_types)*min_width*0.5
            for index, name in enumerate(orig_selected_w_types):
                link_calendar_weeks(prs,slide,name[0],min_left, min_top, min_height, min_width, 54*index+week_count+6+len(orig_selected_m_types)*13+1)
                min_left += min_width
            top += Pt(100)
            min_top += Pt(100)
            week_count +=1
            verify_num = num