from dearpygui import dearpygui as dpg
from boardgui import create_board

PLAYERS = [
    {"name": "P1", "money": 1500, "pos": 0, "status": "Active"},
    {"name": "P2", "money": 1500, "pos": 0, "status": "Active"},
    {"name": "P3", "money": 1500, "pos": 0, "status": "Active"},
    {"name": "P4", "money": 1500, "pos": 0, "status": "Active"},
]

def roll_dice():
    dpg.add_text("🎲 Rolled dice!")  


def buy_property():
    dpg.add_text("🏠 Buy property clicked")


def end_turn():
    dpg.add_text("➡ End turn")


def undo():
    dpg.add_text("↩ Undo")


def redo():
    dpg.add_text("↪ Redo")


dpg.create_context()
dpg.create_viewport(title="Monopoly", width=1200, height=900)

with dpg.window(label="Monopoly Game", tag="main_window", width=980, height=680):
    with dpg.group(horizontal=True):

        create_board(
            parent=dpg.last_item(),
            width=850,
            height=750
        )

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

            dpg.add_button(label="Roll Dice", callback=roll_dice)
            dpg.add_button(label="Buy Property", callback=buy_property)
            dpg.add_button(label="End Turn", callback=end_turn)
            dpg.add_button(label="Undo", callback=undo)
            dpg.add_button(label="Redo", callback=redo)

            dpg.add_separator()
            dpg.add_text("Event Log")
            with dpg.child_window(height=150):
                dpg.add_text("Game Started")

dpg.set_primary_window("main_window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
