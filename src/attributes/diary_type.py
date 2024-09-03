def get_diary_type_info(diary_type):
    select_diary_type = {
        "todo": {
            "template_num": 16,
        },
        "timeline": {
            "template_num": 17,
        },
        "both": {
            "template_num": 18,
        }
    }
    return select_diary_type.get(diary_type, select_diary_type["todo"])