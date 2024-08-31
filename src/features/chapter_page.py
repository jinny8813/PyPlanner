from units.set_titles import set_chapter_title

def create_calendar_slides(prs, my_index_list, ppt_count, chapter_titles, slide_titles):
    layout = prs.slide_layouts[19]
    slide = prs.slides.add_slide(layout)
    set_chapter_title(slide,chapter_titles)
    my_index_list.append(["small",ppt_count,slide_titles[0],slide_titles[1]])
    ppt_count += 1
    return ppt_count