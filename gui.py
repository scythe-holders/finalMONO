from dearpygui import dearpygui as dpg

BOARD_TILES = [
    "GO", "Mediterranean", "Community", "Baltic", "Tax",
    "Reading RR", "Chance", "Vermont", "Connecticut", "Jail",
    "St. Charles", "Electric", "States", "Virginia", "Penn RR",
    "Community", "St. James", "Chance", "Tennessee", "New York"
]

PLAYERS = [
    {"name": "P1", "money": 1500, "pos": 0, "status": "Active"},
    {"name": "P2", "money": 1500, "pos": 0, "status": "Active"},
    {"name": "P3", "money": 1500, "pos": 0, "status": "Active"},
    {"name": "P4", "money": 1500, "pos": 0, "status": "Active"},
]

def tile_label(index):
    players_here = [p["name"] for p in PLAYERS if p["pos"] == index]
    marker = " ".join(players_here)
    return f"{BOARD_TILES[index]}\n{marker}"

dpg.create_context()
dpg.create_viewport(title="Monopoly Board", width=1000, height=700)

with dpg.window(label="Monopoly Game", width=980, height=680):
    with dpg.group(horizontal=True):

        # -------- BOARD --------
        with dpg.child_window(width=650, height=650):
            dpg.add_text("Board")

            with dpg.table():  # ✅ NO borders argument
                for _ in range(5):
                    dpg.add_table_column()

                idx = 0
                for _ in range(5):
                    with dpg.table_row():
                        for _ in range(5):
                            if idx < len(BOARD_TILES):
                                dpg.add_text(tile_label(idx))
                                idx += 1
                            else:
                                dpg.add_text("")

        # -------- SIDE PANEL --------
        with dpg.child_window(width=300, height=650):
            dpg.add_text("Game Status")
            dpg.add_separator()
            dpg.add_text("Current Turn: Player 1")
            dpg.add_text("Phase: ROLL")

            dpg.add_separator()
            dpg.add_text("Players")
            for p in PLAYERS:
                dpg.add_text(f"{p['name']} | ${p['money']} | {p['status']}")

            dpg.add_separator()
            dpg.add_text("Controls")
            dpg.add_button(label="Roll Dice")
            dpg.add_button(label="Buy Property")
            dpg.add_button(label="End Turn")
            dpg.add_button(label="Undo")
            dpg.add_button(label="Redo")

            dpg.add_separator()
            dpg.add_text("Event Log")
            with dpg.child_window(height=150):
                dpg.add_text("Game Started")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
