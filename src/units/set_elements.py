from pptx.enum.text import PP_ALIGN
from pptx.util import Pt

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