from pptx.dml.color import RGBColor

def get_bg_color_info(bg_color):
    select_bg_color = {
        "light": {
            "font_color_section": RGBColor(51, 51, 51),
            "font_color_page_title": RGBColor(92, 92, 92),
            "font_color_element": RGBColor(133, 133, 133),
            "font_color_little": RGBColor(221, 221, 221),
            "nav_bg_color": RGBColor(214, 214, 214),
            "nav_bg_font_color": RGBColor(92, 92, 92)
        },
        "dark": {
            "font_color_section": RGBColor(51, 51, 51),
            "font_color_page_title": RGBColor(235, 235, 235),
            "font_color_element": RGBColor(194, 194, 194),
            "font_color_little": RGBColor(92, 92, 92),
            "nav_bg_color": RGBColor(214, 214, 214),
            "nav_bg_font_color": RGBColor(92, 92, 92)
            }
        }
    return select_bg_color.get(bg_color, select_bg_color["light"])