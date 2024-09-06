from pptx.util import Pt

from units.link_elements import link_top_nav
from set_attribute import orig_selected_w_types,orig_selected_m_types

def link_top_nav_weekly(prs):
    space = Pt(28)
    top = Pt(56)
    left = Pt(1024) - space * len(orig_selected_w_types) - Pt(42)
    width = height = Pt(18)
    for slide in prs.slides:
        current_page = prs.slides.index(slide)
        if current_page>=6+len(orig_selected_m_types)*13+len(orig_selected_w_types)*54:
            break
        if current_page<6+len(orig_selected_m_types)*13 or (current_page-6-len(orig_selected_m_types)*13)%54 == 0:
            continue
        for index, element in enumerate(orig_selected_w_types):
            link_top_nav(prs,slide,element[0],left+index*space, top, width, height, (current_page-6-len(orig_selected_m_types)*13)%54+index*54+6+len(orig_selected_m_types)*13)