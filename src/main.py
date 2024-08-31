import os
from pptx import Presentation

from features.book_cover import create_front_cover_slides, create_back_cover_slides
from features.chapter_page import create_calendar_slides
from features.main_calendar import create_main_calendar_slides

my_index_list = []
ppt_count = 0

os.chdir(r'src')
prs = Presentation('assets/layout-2425-light-chinese.pptx')

ppt_count = create_front_cover_slides(prs, my_index_list, ppt_count, ["The Blueprint","2025 Journal"], ["2025 Journal","封面"])

ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Calendar"], ["Monthly | Calendar","月行事曆"])
ppt_count = create_main_calendar_slides(prs, ppt_count)

ppt_count = create_back_cover_slides(prs, my_index_list, ppt_count, ["The Blueprint","封底"])

print(my_index_list)
print(ppt_count)

prs.save(f'prep.pptx')
