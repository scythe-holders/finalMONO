from dearpygui import dearpygui as dpg

# --- Circular Linked List Classes (your original) ---


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

# --- Tile Class ---


class Tile:
    def __init__(self, name, role=None, ownership=None, rect=None):
        self.name = name
        self.role = role  # e.g., "Property", "Tax", "Go", "Chance"
        self.ownership = ownership  # e.g., "P1", None
        self.players = []  # players currently on tile
        self.rect = rect  # (x1, y1, x2, y2) for rendering

# --- Board Class ---


class Board:
    TILE_SIZE = 60
    BOARD_ORIGIN_X = 20
    BOARD_ORIGIN_Y = 20

    TILE_NAMES = [
        "GO", "Mediterranean", "Community", "Baltic", "Income Tax",
        "Reading RR", "Chance", "Vermont", "Connecticut", "Jail",
        "St. Charles", "Electric", "States", "Virginia", "Penn RR",
        "Community", "St. James", "Chance", "Tennessee", "New York",
        "Free Parking", "Kentucky", "Chance", "Indiana", "Illinois",
        "B&O RR", "Atlantic", "Ventnor", "Water Works", "Marvin Gardens",
        "Go To Jail", "Pacific", "North Carolina", "Community", "Pennsylvania",
        "Short Line", "Chance", "Park Place", "Luxury Tax", "Boardwalk"
    ]

    TILE_ROLES = [  # simple example, same length as TILE_NAMES
        "Go", "Property", "Community", "Property", "Tax",
        "Railroad", "Chance", "Property", "Property", "Jail",
        "Property", "Utility", "Property", "Property", "Railroad",
        "Community", "Property", "Chance", "Property", "Property",
        "Free Parking", "Property", "Chance", "Property", "Property",
        "Railroad", "Property", "Property", "Utility", "Property",
        "Go To Jail", "Property", "Property", "Community", "Property",
        "Railroad", "Chance", "Property", "Tax", "Property"
    ]

    def __init__(self):
        self.tiles = CircularLinkedList()
        self._create_tiles()

    def tile_at(self, row, col):
        # bottom row (GO → Jail)
        if row == 10 and col != 0:
            return 10 - col

        # right column (Jail → Free Parking)
        if col == 10 and row != 10:
            return 10 + row

        # top row (Free Parking → Go To Jail)
        if row == 0 and col != 10:
            return 20 + col

        # left column (Go To Jail → GO)
        if col == 0 and row != 0:
            return 30 + (10 - row)

        # corners
        if row == 10 and col == 0:
            return 0        # GO
        if row == 10 and col == 10:
            return 10       # Jail
        if row == 0 and col == 10:
            return 20       # Free Parking
        if row == 0 and col == 0:
            return 30       # Go To Jail

        return None

    def _create_tiles(self):
        """Populate self.tiles as a circular linked list."""
        tiles_dict = {}
        # calculate positions for all tiles
        for r in range(11):
            for c in range(11):
                idx = self.tile_at(r, c)
                if idx is None:
                    continue
                x1 = self.BOARD_ORIGIN_X + c * self.TILE_SIZE
                y1 = self.BOARD_ORIGIN_Y + r * self.TILE_SIZE
                x2 = x1 + self.TILE_SIZE
                y2 = y1 + self.TILE_SIZE
                tile = Tile(
                    name=self.TILE_NAMES[idx],
                    role=self.TILE_ROLES[idx],
                    ownership=None,
                    rect=(x1, y1, x2, y2)
                )
                tiles_dict[idx] = tile

        # append tiles in order to circular linked list
        for i in range(len(self.TILE_NAMES)):
            self.tiles.append(tiles_dict[i])

    def draw(self, parent):
        """Draw all tiles in the DearPyGui drawlist."""
        with dpg.child_window(parent=parent, width=850, height=750):
            with dpg.drawlist(width=850, height=750, tag="board_drawlist"):
                current = self.tiles.head
                while True:
                    x1, y1, x2, y2 = current.data.rect
                    dpg.draw_rectangle(
                        (x1, y1), (x2, y2),
                        color=(255, 255, 255, 255),
                        fill=(40, 40, 40, 255)
                    )
                    dpg.draw_text(
                        (x1 + 5, y1 + 5),
                        current.data.name,
                        size=10
                    )
                    if current.data.players:
                        dpg.draw_text(
                            (x1 + 5, y1 + 25),
                            " ".join(current.data.players),
                            size=10,
                            color=(0, 255, 0, 255)
                        )

                    current = current.next
                    if current == self.tiles.head:
                        break
