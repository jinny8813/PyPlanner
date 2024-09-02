import os
from pptx import Presentation

from features.book_cover import create_front_cover_slides, create_back_cover_slides, create_index_slides
from features.chapter_page import create_calendar_slides
from features.main_calendar import create_main_calendar_slides
from features.monthly_miniplanner import create_miniplanner_slides
from features.monthly_project import create_project_slides
from features.monthly_tracker import create_tracker_slides
from features.monthly_gallery import create_gallery_slides
from features.monthly_finances import create_finances_slides
from features.monthly_health import create_health_slides
from features.monthly_energy import create_energy_slides
from features.weekly_todolist import create_todolist_slides
from features.weekly_timeline import create_timeline_slides

my_index_list = []
ppt_count = 0

os.chdir(r'src')
prs = Presentation('assets/layout-2425-light-chinese.pptx')

ppt_count = create_front_cover_slides(prs, my_index_list, ppt_count, ["The Blueprint","2025 Journal"], ["2025 Journal","封面"])
ppt_count = create_index_slides(prs, my_index_list, ppt_count, "Index", ["Index","索引"])

ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Calendar"], ["Monthly | Calendar","月行事曆"])
ppt_count = create_main_calendar_slides(prs, ppt_count)

ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","MiniPlanner"], ["Monthly | MiniPlanner","月迷你規劃"])
ppt_count = create_miniplanner_slides(prs, ppt_count)
ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Project"], ["Monthly | Project","月專案管理"])
ppt_count = create_project_slides(prs, ppt_count)
ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Tracker"], ["Monthly | Tracker","月習慣追蹤"])
ppt_count = create_tracker_slides(prs, ppt_count)
ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Gallery"], ["Monthly | Gallery","月相片畫廊"])
ppt_count = create_gallery_slides(prs, ppt_count)
ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Finances"], ["Monthly | Finances","月財務管理"])
ppt_count = create_finances_slides(prs, ppt_count)
ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Health"], ["Monthly | Health","月健康管理"])
ppt_count = create_health_slides(prs, ppt_count)
ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Energy"], ["Monthly | Energy","月能量管理"])
ppt_count = create_energy_slides(prs, ppt_count)

ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","TodoList"], ["Weekly | TodoList","週待辦清單"])
ppt_count = create_todolist_slides(prs, ppt_count)
ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Timeline"], ["Weekly | Timeline","週時間軸"])
ppt_count = create_timeline_slides(prs, ppt_count)

ppt_count = create_back_cover_slides(prs, my_index_list, ppt_count, ["The Blueprint","封底"])

print(my_index_list)
print(ppt_count)

prs.save(f'prep.pptx')
