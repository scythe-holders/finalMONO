# boardgui.py
from dearpygui import dearpygui as dpg

def create_board(parent, width=650, height=650):
    TILE_SIZE = 60
    BOARD_ORIGIN_X = 20
    BOARD_ORIGIN_Y = 20

    TILES = [
        "GO","Property","Tax","Jail","tax",
        "Reading RR","chest","Vermont","Connecticut","Jail",
        "St. Charles","Electric","States","Virginia","Penn RR",
        "chest","St. James","chest","Tennessee","New York",
        "Property","Kentucky","Property","Indiana","Illinois",
        "B&O RR","Atlantic","Ventnor","Water Works","Marvin Gardens",
        "Go To Jail","Property","North chest","Tax","Pennsylvania",
        "Short Line","chest","Park Place","Tax","Property"
    ]

    PLAYERS = [
        {"name": "P1", "pos": 0},
        {"name": "P2", "pos": 5},
        {"name": "P3", "pos": 12},
        {"name": "P4", "pos": 20},
    ]

    def tile_at(row, col):
        if row == 10: return 10 - col
        if col == 10: return 10 + (10 - row)
        if row == 0:  return 20 + col
        if col == 0:  return 30 + row
        return None

    with dpg.child_window(parent=parent, width=width, height=height):
        with dpg.drawlist(width=width, height=height):
            for r in range(11):
                for c in range(11):
                    idx = tile_at(r, c)
                    if idx is None:
                        continue

                    x1 = BOARD_ORIGIN_X + c * TILE_SIZE
                    y1 = BOARD_ORIGIN_Y + r * TILE_SIZE
                    x2 = x1 + TILE_SIZE
                    y2 = y1 + TILE_SIZE

                    dpg.draw_rectangle((x1, y1), (x2, y2),
                        color=(255, 255, 255, 255),
                        fill=(40, 40, 40, 255)
                    )

                    dpg.draw_text((x1 + 5, y1 + 5), TILES[idx], size=10)
