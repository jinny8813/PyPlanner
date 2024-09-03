from units.set_titles import set_chapter_title

def create_stickers_slides(prs, my_index_list, ppt_count):
    stickers_names = [["Calendar","日曆貼紙"], ["Label","標籤貼紙"], ["Rectangle","矩形貼紙"], ["SolidColor","純色貼紙"], ["Decoration","裝飾貼紙"], ["Others","其他貼紙"]]
    for i in stickers_names:
        layout = prs.slide_layouts[19]
        slide = prs.slides.add_slide(layout)
        set_chapter_title(slide,["Stickers",i[0]])
        my_index_list.append(["small",ppt_count,"Sticker | {}".format(i[0]),i[1]])
        ppt_count += 1
        layout = prs.slide_layouts[21]
        slide = prs.slides.add_slide(layout)
        ppt_count += 1
    return ppt_count