from pptx.enum.text import PP_ALIGN
from pptx.util import Pt
import calendar

from set_attribute import orig_font_color_element

def set_date_element(slide,date_value,left, top, width, height, lunar_text=None):
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

def set_lunar_element(slide,lunar_text,left, top, width, height):
    tb = slide.shapes.add_textbox(left, top, width, height)
    p = tb.text_frame.paragraphs[0]
    p.text = lunar_text
    p.font.size = Pt(8)
    p.font.name = "Arial"
    p.font.color.rgb = orig_font_color_element
    p.alignment = PP_ALIGN.CENTER

def set_small_calendar(slide,month_first_day,left, top,week_list):   
    o_left = left
    width = height = Pt(20)
    for e in week_list:
        set_date_element(slide,e,left, top, width, height)
        left += width
    top += height
    for j in range(calendar.monthrange(month_first_day.year,month_first_day.month)[1]):
        if j == 0:
            if week_list[0] == "M":
                left = o_left + width * month_first_day.weekday()
            else:
                left = o_left + width * (month_first_day.weekday()+1)
        if left > o_left + width *6:
            top += height
            left = o_left 
            if j == 0:
                top -= height
        set_date_element(slide,str(j+1),left, top, width, height)
        left += width