from units.set_titles import set_chapter_title

def create_collection_slides(prs, my_index_list, ppt_count):
    lifestyle_names = [["BookList","書單"], ["MovieList","片單"], ["MusicList","歌單"], ["Attractions","景點"], ["Portfolio","作品集"], ["Etc","其他"]]
    for i in lifestyle_names:
        layout = prs.slide_layouts[19]
        slide = prs.slides.add_slide(layout)
        set_chapter_title(slide,["lifestyle",i[0]])
        my_index_list.append(["small",ppt_count,"Collection | {}".format(i[0]),i[1]])
        ppt_count += 1
        for j in range(3):
            prs.slides._sldIdLst.insert(len(prs.slides), prs.slides._sldIdLst[0])
            ppt_count += 1
    return ppt_count

def create_notebook_slides(prs, my_index_list, ppt_count):
    notebook_names = [["A","筆記本 A"], ["B","筆記本 B"], ["C","筆記本 C"], ["D","筆記本 D"], ["E","筆記本 E"], ["Templates","筆記模板"]]
    for index,i in enumerate(notebook_names):
        layout = prs.slide_layouts[19]
        slide = prs.slides.add_slide(layout)
        set_chapter_title(slide,["lifestyle","Notebook {}".format(i[0])])
        my_index_list.append(["small",ppt_count,"Notebook | {}".format(i[0]),i[1]])
        ppt_count += 1
        if index == len(notebook_names)-1:
            for j in range(4):
                prs.slides._sldIdLst.insert(len(prs.slides), prs.slides._sldIdLst[0])
                ppt_count += 1
    return ppt_count