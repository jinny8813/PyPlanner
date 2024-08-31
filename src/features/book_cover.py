from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

from units.set_titles import set_chapter_title
from set_attribute import orig_theme_colors

def create_front_cover_slides(prs, my_index_list, ppt_index_count, chapter_titles, slide_titles):
    layout = prs.slide_layouts[19]
    slide = prs.slides.add_slide(layout)
    top = Pt(148)
    left = Pt(0)
    height = Pt(620)
    width = Pt(864)
    for i,row in enumerate(orig_theme_colors):
        rectangle = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,left,top,width,height)
        rectangle.fill.solid()
        rectangle.fill.fore_color.rgb = RGBColor(row[0], row[1], row[2])
        rectangle.line.color.rgb = RGBColor(row[0], row[1], row[2])
        left += width
        width = Pt(40)
    set_chapter_title(slide,chapter_titles)
    my_index_list.append(["cover",ppt_index_count,slide_titles[0],slide_titles[1]])
    return ppt_index_count