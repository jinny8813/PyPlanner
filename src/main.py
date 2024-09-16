import os
from pptx import Presentation

from set_attribute import orig_selected_w_types,orig_selected_m_types,user_choice

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

from links.weekly_todolist import link_todolist_to_diary
from links.weekly_timeline import link_timeline_to_diary
from links.weekly_grid import link_grid_to_diary
from links.weekly_anynotes import link_anynotes_to_diary
from links.weekly_overview import link_overview_to_diary
from links.weekly_budget import link_budget_to_diary
from links.weekly_health import link_health_to_diary
from links.weekly_energy import link_energy_to_diary

from links.calendar_diary import link_calendar_to_diary
from links.calendar_weeks import link_calendar_to_weeks
from links.topnav_monthly import link_top_nav_monthly
from links.topnav_weekly import link_top_nav_weekly
from links.topnav_diary_weeks import link_top_nav_diary_weeks
from links.downnav import link_down_nav
from links.index import link_index

from links.gn_diary import link_gn_apple_diary,link_gn_google_diary
from links.gn_timeline import link_gn_apple_timeline,link_gn_google_timeline

monthly_types = [
    ("Calendar", "Monthly | Calendar", "月行事曆"),
    ("MiniPlanner", "Monthly | MiniPlanner", "月迷你規劃"),
    ("Project", "Monthly | Project", "月專案管理"),
    ("Tracker", "Monthly | Tracker", "月習慣追蹤"),
    ("Gallery", "Monthly | Gallery", "月相片畫廊"),
    ("Finances", "Monthly | Finances", "月財務管理"),
    ("Health", "Monthly | Health", "月健康管理"),
    ("Energy", "Monthly | Energy", "月能量管理")
]

weekly_types = [
    ("ListTodo", "Weekly | ListTodo", "週待辦清單"),
    ("Timeline", "Weekly | Timeline", "週時間軸"),
    ("Grid", "Weekly | Grid", "週八分格"),
    ("AnyNotes", "Weekly | AnyNotes", "週札記"),
    ("Overview", "Weekly | Overview", "週總覽"),
    ("Budget", "Weekly | Budget", "週記帳"),
    ("Health", "Weekly | Health", "週健康"),
    ("Energy", "Weekly | Energy", "週能量")
]

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

monthly_slide_functions = {
    "Calendar": create_main_calendar_slides,
    "MiniPlanner": create_miniplanner_slides,
    "Project": create_project_slides,
    "Tracker": create_tracker_slides,
    "Gallery": create_gallery_slides,
    "Finances": create_finances_slides,
    "Health": create_health_slides,
    "Energy": create_energy_slides
}

for m_type, title_en, title_zh in monthly_types:
    if m_type in orig_selected_m_types:
        ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal", m_type], [title_en, title_zh])
        ppt_count = monthly_slide_functions[m_type](prs, ppt_count)

weekly_slide_functions = {
    "ListTodo": create_todolist_slides,
    "Timeline": create_timeline_slides,
    "Grid": create_grid_slides,
    "AnyNotes": create_anynotes_slides,
    "Overview": create_overview_slides,
    "Budget": create_budget_slides,
    "Health": create_w_health_slides,
    "Energy": create_w_energy_slides
}

for w_types, title_en, title_zh in weekly_types:
    if w_types in orig_selected_w_types:
        ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal", w_types], [title_en, title_zh])
        ppt_count = weekly_slide_functions[w_types](prs, ppt_count)

ppt_count = create_calendar_slides(prs, my_index_list, ppt_count, ["Journal","Diary"], ["Daily | Diary","日記"])
ppt_count = create_diary_slides(prs, ppt_count)

ppt_count = create_section_slides(prs, my_index_list, ppt_count, "Lifestyle", ["Lifestyle","生活風格"],2)
ppt_count = create_collection_slides(prs, my_index_list, ppt_count)
ppt_count = create_notebook_slides(prs, my_index_list, ppt_count)

ppt_count = create_section_slides(prs, my_index_list, ppt_count, "Stickers", ["Stickers","貼紙合集"],3)
ppt_count = create_stickers_slides(prs, my_index_list, ppt_count)

ppt_count = create_back_cover_slides(prs, my_index_list, ppt_count, ["The Blueprint","封底"])

weekly_to_diary_functions = {
    "ListTodo": link_todolist_to_diary,
    "Timeline": link_timeline_to_diary,
    "Grid": link_grid_to_diary,
    "AnyNotes": link_anynotes_to_diary,
    "Overview": link_overview_to_diary,
    "Budget": link_budget_to_diary,
    "Health": link_health_to_diary,
    "Energy": link_energy_to_diary
}

for w_types, title_en, title_zh in weekly_types:
    if w_types in orig_selected_w_types:
        weekly_to_diary_functions[w_types](prs,len(orig_selected_m_types),orig_selected_w_types.index(w_types)+1,5+len(orig_selected_m_types)*13+len(orig_selected_w_types)*54+2)

link_calendar_to_diary(prs,5+len(orig_selected_m_types)*13+len(orig_selected_w_types)*54+2)
link_calendar_to_weeks(prs,5+len(orig_selected_m_types)*13+len(orig_selected_w_types)*54+2)
link_top_nav_monthly(prs)
link_top_nav_weekly(prs)
link_top_nav_diary_weeks(prs)
link_down_nav(prs,my_index_list)
link_index(prs,my_index_list)

if user_choice["outside_links"] != None:
    link_gn_apple_diary(prs)
    link_gn_google_diary(prs)
    link_gn_apple_timeline(prs,len(orig_selected_m_types),orig_selected_w_types.index("Timeline")+1)
    link_gn_google_timeline(prs,len(orig_selected_m_types),orig_selected_w_types.index("Timeline")+1)

print(my_index_list)
print(ppt_count)

prs.save(f"BluegaJournal-{user_choice['theme_colors']}-{user_choice['bg_color']}-{user_choice['start_day']}-{user_choice['diary_type']}-{user_choice['language']}-{user_choice['outside_links']}.pptx")
