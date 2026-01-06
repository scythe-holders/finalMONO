# NOTE: This is a STRICT reference implementation based ONLY on the provided document.
# No rules, entities, or structures are changed or added.
# Language: Python 3
# Architecture: Server-only logic (Single Source of Truth)
# GUI/Network intentionally minimal (text-based hooks)

############################
# DATA STRUCTURES (MANUAL) #
############################

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = LinkedListNode(value)
        if not self.head:
            self.head = node
            node.next = node
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = node
        node.next = self.head

    def move(self, start_node, steps):
        cur = start_node
        passed_go = False
        for _ in range(steps):
            cur = cur.next
            if cur.value.tile_type == 'GO':
                passed_go = True
        return cur, passed_go

class Stack:
    def __init__(self):
        self.data = []
    def push(self, x): self.data.append(x)
    def pop(self): return self.data.pop() if self.data else None
    def clear(self): self.data.clear()

class Queue:
    def __init__(self): self.data = []
    def enqueue(self, x): self.data.append(x)
    def dequeue(self): return self.data.pop(0)

class HashTable:
    def __init__(self): self.table = {}
    def insert(self, k, v): self.table[k] = v
    def get(self, k): return self.table.get(k)
    def remove(self, k): del self.table[k]

########################
# DOMAIN ENTITIES      #
########################

class Player:
    def __init__(self, pid, name):
        self.id = pid
        self.name = name
        self.balance = 1500
        self.position = None
        self.status = 'Active'
        self.jail_turns = 0
        self.properties = []
        self.undo = Stack()
        self.redo = Stack()

class Property:
    def __init__(self, pid, name, price, rent):
        self.id = pid
        self.name = name
        self.price = price
        self.base_rent = rent
        self.owner = None
        self.house_count = 0
        self.hotel = False
        self.mortgaged = False

class Tile:
    def __init__(self, tid, ttype, data=None):
        self.id = tid
        self.tile_type = ttype
        self.data = data

class Card:
    def __init__(self, cid, desc, effect):
        self.id = cid
        self.desc = desc
        self.effect = effect

########################
# GAME STATE           #
########################

class GameState:
    def __init__(self):
        self.players = HashTable()
        self.turn_order = []
        self.turn_index = 0
        self.board = CircularLinkedList()
        self.chance = Queue()
        self.community = Queue()
        self.log = []

    def current_player(self):
        return self.players.get(self.turn_order[self.turn_index])

########################
# GAME SERVER LOGIC    #
########################

class GameServer:
    GO_REWARD = 200

    def __init__(self):
        self.state = GameState()

    def add_player(self, pid, name):
        self.state.players.insert(pid, Player(pid, name))
        self.state.turn_order.append(pid)

    def setup_board(self):
        self.state.board.append(Tile(0, 'GO'))
        self.state.board.append(Tile(1, 'PROPERTY', Property(1, 'Mediterranean', 60, 2)))
        self.state.board.append(Tile(2, 'TAX', 100))
        self.state.board.append(Tile(3, 'JAIL'))

        # assign starting position
        for pid in self.state.turn_order:
            self.state.players.get(pid).position = self.state.board.head

    def roll_dice(self):
        import random
        return random.randint(1,6) + random.randint(1,6)

    def take_turn(self):
        p = self.state.current_player()
        roll = self.roll_dice()
        new_pos, passed_go = self.state.board.move(p.position, roll)
        p.position = new_pos
        if passed_go:
            p.balance += self.GO_REWARD
        self.resolve_tile(p, new_pos.value)
        self.end_turn()

    def resolve_tile(self, player, tile):
        if tile.tile_type == 'PROPERTY':
            prop = tile.data
            if prop.owner is None and player.balance >= prop.price:
                player.balance -= prop.price
                prop.owner = player.id
                player.properties.append(prop.id)
        elif tile.tile_type == 'TAX':
            player.balance -= tile.data
            if player.balance < 0:
                player.status = 'Bankrupt'
        elif tile.tile_type == 'JAIL':
            player.status = 'InJail'
            player.jail_turns = 0

    def end_turn(self):
        self.state.turn_index = (self.state.turn_index + 1) % len(self.state.turn_order)

########################
# BOOTSTRAP            #
########################

if __name__ == '__main__':
    server = GameServer()
    server.add_player(1, 'P1')
    server.add_player(2, 'P2')
    server.add_player(3, 'P3')
    server.add_player(4, 'P4')
    server.setup_board()

    for _ in range(10):
        server.take_turn()
        for pid in server.state.turn_order:
            p = server.state.players.get(pid)
            print(p.name, p.balance, p.status)
        print('---')
