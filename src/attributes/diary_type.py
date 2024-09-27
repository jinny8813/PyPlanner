def get_diary_type_info(diary_type):
    select_diary_type = {
        "miniA": {
            "template_num": 18,
            "selected_w_types": ["Timeline", "AnyNotes", "Budget", "Health"],
            "selected_c_types": ["Calendar", "Project", "Health"]
        },
        "miniB": {
            "template_num": 18,
            "selected_w_types": ["ListTodo", "Grid", "Budget", "Energy"],
            "selected_c_types": ["Calendar", "Tracker", "Energy"]
        },
        "miniC": {
            "template_num": 18,
            "selected_w_types": ["ListTodo", "Timeline", "Grid"],
            "selected_c_types": ["Calendar", "MiniPlanner"]
        },
        "plentifulAll": {
            "template_num": 18,
            "selected_w_types": ["ListTodo", "Timeline", "Grid", "AnyNotes", "Overview", "Budget", "Health", "Energy"],
            "selected_c_types": ["Calendar","MiniPlanner", "Project", "Tracker", "Gallery", "Finances", "Health", "Energy"]
        },
        "pinkoi": {
            "template_num": 18,
            "selected_w_types": ["ListTodo", "Grid", "AnyNotes", "Overview", "Budget", "Health", "Energy"],
            "selected_c_types": ["Calendar","MiniPlanner", "Project", "Tracker", "Gallery", "Finances", "Health", "Energy"]
        }
    }
    return select_diary_type.get(diary_type, select_diary_type["miniA"])