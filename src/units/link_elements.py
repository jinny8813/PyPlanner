from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Pt

from set_attribute import orig_font_color_element,orig_nav_bg_color,orig_nav_bg_font_color

def link_date_element(prs,slide,date_value,left, top, width, height, lunar_text=None, link_to = None):
    tb = slide.shapes.add_textbox(left, top, width, height)
    p = tb.text_frame.paragraphs[0]
    p.text = date_value
    p.font.size = Pt(12)
    p.font.name = "Arial"
    p.font.color.rgb = orig_font_color_element
    p.alignment = PP_ALIGN.CENTER
    if lunar_text!= None:
        run = p.add_run()
        run.text = " " + lunar_text
        run.font.size = Pt(8)
    if link_to!= None:
        tb.click_action.target_slide = prs.slides[link_to]

def link_date_element_grid(prs,slide,date_value,left, top, width, height, link_to = None):
    tb = slide.shapes.add_textbox(left, top, width, height)
    p = tb.text_frame.paragraphs[0]
    p.text = date_value
    p.font.size = Pt(24)
    p.font.name = "Arial"
    p.font.color.rgb = orig_font_color_element
    p.alignment = PP_ALIGN.CENTER
    if link_to!= None:
        tb.click_action.target_slide = prs.slides[link_to]

def set_calendar_week_links(prs,slide,week_value,left, top, width, height, link_to):
    tb = slide.shapes.add_textbox(left, top, width, height)
    p = tb.text_frame.paragraphs[0]
    p.text = week_value
    p.font.size = Pt(10)
    p.font.name = "Arial"
    p.font.color.rgb = orig_font_color_element
    p.alignment = PP_ALIGN.CENTER
    tb.click_action.target_slide = prs.slides[link_to]
