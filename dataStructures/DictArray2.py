class DictArray:
    def __init__(self):
        self._items = [] # list of (key, value)

    def set(self, key: str, value):
        for i, (k, _) in enumerate(self._items):
            if k == key:
                self._items[i] = (key, value)
                return
        self._items.append((key, value))

    def get(self, key: str):
        for k, v in self._items:
            if k == key:
                return v
        raise KeyError(key)

    def has(self, key: str) -> bool:
        return any(k == key for k, _ in self._items)
    def __repr__(self):
        text=""
        for i in self._items :
            text+=f"{i}"
            text+="\t"
        return text    
# arian=DictArray()    