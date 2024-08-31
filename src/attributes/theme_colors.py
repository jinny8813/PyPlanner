def get_theme_colors_info(theme_colors):
    select_theme_colors = {
        "cust": {
            "name":"cust",
            "colors": [
                [184,201,167],
                [219,203,186],[232,228,218],[182,183,203],[175,157,186]]
        },
        "soda": {
            "name":"soda",
            "colors": [
                [182,193,199], [162,165,184], [150,145,168], [181,163,185],
                [207,189,201]]
        },
        "mint": {
            "name":"mint",
            "colors": [
                [217,209,170], [189,199,165], [157,183,154], [167,198,183],
                [189,207,207]]
        }
    }
    return select_theme_colors[theme_colors]