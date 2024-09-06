from pptx.util import Pt

from units.link_elements import link_top_nav
from set_attribute import orig_selected_m_types

def link_top_nav_monthly(prs):
    space = Pt(28)
    top = Pt(56)
    left = Pt(1024) - space * len(orig_selected_m_types) - Pt(42)
    width = height = Pt(18)
    for slide in prs.slides:
        current_page = prs.slides.index(slide)
        if current_page>=6+len(orig_selected_m_types)*13:
            break
        if current_page<6+1 or (current_page-6)%13 == 0:
            continue
        for index, element in enumerate(orig_selected_m_types):
            link_top_nav(prs,slide,element[0],left+index*space, top, width, height, (current_page-6)%13+index*13+6)