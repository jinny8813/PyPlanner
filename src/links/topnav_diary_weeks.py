from pptx.util import Pt
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from units.link_elements import link_top_nav
from set_attribute import orig_start_month,orig_start_day
from set_attribute import orig_selected_w_types,orig_selected_m_types

def link_top_nav_diary_weeks(prs):
    space = Pt(28)
    top = Pt(56)
    left = Pt(1024) - space * len(orig_selected_w_types) - Pt(42)
    width = height = Pt(18)
    date = orig_start_month
    year_count = (orig_start_month+relativedelta(years=1)-orig_start_month)
    for slide in prs.slides:
        current_page = prs.slides.index(slide)
        if orig_start_day == "Monday":
            week_num = int(date.strftime("%W"))+1
        else:
            week_num = int(date.strftime("%U"))+1
        if date.strftime("%Y") == "2024":
            week_num = week_num-1
        if current_page>=6+len(orig_selected_m_types)*13+len(orig_selected_w_types)*54+1+year_count.days:
            break
        if current_page<6+len(orig_selected_m_types)*13+len(orig_selected_w_types)*54+1:
            continue
        for index,element in enumerate(orig_selected_w_types):
            link_top_nav(prs,slide,element[0],left+index*space, top, width, height, week_num+index*54+6+len(orig_selected_m_types)*13)
        date += timedelta(days=1)