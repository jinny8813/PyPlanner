def get_diary_type_info(diary_type):
    select_diary_type = {
        "minitodo": {
            "template_num": None,
            "selected_w_types": ["TodoList", "Grid"]
        },
        "minitimeline": {
            "template_num": None,
            "selected_w_types": ["Timeline", "Grid"]
        },
        "mediumtodo": {
            "template_num": 16,
            "selected_w_types": ["TodoList", "Grid", "AnyNotes", "Budget", "Health", "Energy"]
        },
        "mediumtimeline": {
            "template_num": 17,
            "selected_w_types": ["Timeline", "Grid", "AnyNotes", "Budget", "Health", "Energy"]
        },
        "plentifulboth": {
            "template_num": 18,
            "selected_w_types": ["TodoList", "Timeline", "Grid", "AnyNotes", "Overview", "Budget", "Health", "Energy"]
        }
    }
    return select_diary_type.get(diary_type, select_diary_type["minitodo"])