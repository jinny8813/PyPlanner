import os
from pptx import Presentation

from set_attribute import orig_selected_w_types

from features.book_cover import create_front_cover_slides, create_back_cover_slides, create_index_slides
from features.chapter_page import create_calendar_slides, create_section_slides
from features.yearly_overview import create_yaag_slides,create_gc_slides
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
from features.weekly_grid import create_grid_slides
from features.weekly_anynotes import create_anynotes_slides
from features.weekly_overview import create_overview_slides
from features.weekly_budget import create_budget_slides
from features.weekly_health import create_health_slides as create_w_health_slides
from features.weekly_energy import create_energy_slides as create_w_energy_slides
from features.diary import create_diary_slides
from features.lifestyle import create_collection_slides,create_notebook_slides
from features.stickers import create_stickers_slides

my_index_list = []
ppt_count = 0

os.chdir(r'src')
prs = Presentation('assets/layout-2425-light-chinese.pptx')

ppt_count = create_front_cover_slides(prs, my_index_list, ppt_count, ["The Blueprint","2025 Journal"], ["2025 Journal","封面"])
ppt_count = create_index_slides(prs, my_index_list, ppt_count, "Index", ["Index","索引"])

ppt_count = create_section_slides(prs, my_index_list, ppt_count, "Journal", ["Journal","手帳年曆"],1)
ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","2025 Overview"], ["Yearly | Overview","年曆總覽"])
ppt_count = create_yaag_slides(prs, ppt_count)
ppt_count = create_gc_slides(prs, ppt_count)

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
print(2)
# ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","TodoList"], ["Weekly | TodoList","週待辦清單"])
# ppt_count = create_todolist_slides(prs, ppt_count)
# ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Timeline"], ["Weekly | Timeline","週時間軸"])
# ppt_count = create_timeline_slides(prs, ppt_count)
# ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Grid"], ["Weekly | Grid","週八分格"])
# ppt_count = create_grid_slides(prs, ppt_count)
# ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","AnyNotes"], ["Weekly | AnyNotes","週札記"])
# ppt_count = create_anynotes_slides(prs, ppt_count)
# ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Overview"], ["Weekly | Overview","週總覽"])
# ppt_count = create_overview_slides(prs, ppt_count)
# ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Budget"], ["Weekly | Budget","週記帳"])
# ppt_count = create_budget_slides(prs, ppt_count)
# ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Health"], ["Weekly | Health","週健康"])
# ppt_count = create_w_health_slides(prs, ppt_count)
# ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Energy"], ["Weekly | Energy","週能量"])
# ppt_count = create_w_energy_slides(prs, ppt_count)
slide_functions = {
    "TodoList": create_todolist_slides,
    "Timeline": create_timeline_slides,
    "Grid": create_grid_slides,
    "AnyNotes": create_anynotes_slides,
    "Overview": create_overview_slides,
    "Budget": create_budget_slides,
    "Health": create_w_health_slides,
    "Energy": create_w_energy_slides
}
journal_types = [
    ("TodoList", "Weekly | TodoList", "週待辦清單"),
    ("Timeline", "Weekly | Timeline", "週時間軸"),
    ("Grid", "Weekly | Grid", "週八分格"),
    ("AnyNotes", "Weekly | AnyNotes", "週札記"),
    ("Overview", "Weekly | Overview", "週總覽"),
    ("Budget", "Weekly | Budget", "週記帳"),
    ("Health", "Weekly | Health", "週健康"),
    ("Energy", "Weekly | Energy", "週能量")
]
for j_type, title_en, title_zh in journal_types:
    if j_type in orig_selected_w_types:
        print(f"Before create_calendar_slides: ppt_count = {ppt_count}")
        ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal", j_type], [title_en, title_zh])
        print(f"After create_calendar_slides: ppt_count = {ppt_count}")
        print(f"Before {j_type} slide function: ppt_count = {ppt_count}")
        ppt_count = slide_functions[j_type](prs, ppt_count)
        print(f"After {j_type} slide function: ppt_count = {ppt_count}")

ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Diary"], ["Daily | Diary","日記"])
ppt_count = create_diary_slides(prs, ppt_count)

ppt_count = create_section_slides(prs, my_index_list, ppt_count, "Lifestyle", ["Lifestyle","生活風格"],2)
ppt_count = create_collection_slides(prs, my_index_list, ppt_count)
ppt_count = create_notebook_slides(prs, my_index_list, ppt_count)

ppt_count = create_section_slides(prs, my_index_list, ppt_count, "Stickers", ["Stickers","貼紙合集"],3)
ppt_count = create_stickers_slides(prs, my_index_list, ppt_count)

ppt_count = create_back_cover_slides(prs, my_index_list, ppt_count, ["The Blueprint","封底"])

print(my_index_list)
print(ppt_count)

prs.save(f'prep.pptx')
