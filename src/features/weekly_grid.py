from datetime import timedelta
from dateutil.relativedelta import relativedelta

from units.set_titles import set_page_title
from set_attribute import orig_start_week,orig_start_date,orig_start_month

def create_grid_slides(prs, ppt_count):
    today = orig_start_date
    this_year = int(orig_start_month.strftime("%Y"))
    week_count = orig_start_week
    while today < orig_start_date+relativedelta(years=1):
        layout = prs.slide_layouts[10]
        slide = prs.slides.add_slide(layout)
        if week_count == 1 and today != orig_start_date:
            this_year += 1        
        set_page_title(slide,"{} Week {} Grid".format(this_year,week_count))
        for j in range(7):
            today += timedelta(days=1)
        week_count +=1
        if week_count>52:
            week_count = 1
    ppt_count += 53
    return ppt_count