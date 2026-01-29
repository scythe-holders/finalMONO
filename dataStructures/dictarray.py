class ArrayDict:
    def __init__(self, size=64):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update
                return

        bucket.append((key, value))  # insert new
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

        raise KeyError(key)

    def contains(self, key):
        index = self._hash(key)
        return any(k == key for k, _ in self.buckets[index])

    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]
    def  __repr__(self):
        x="this dict is {0}.".format(self.buckets)
        return x
ar1=ArrayDict()
ar1.set(50,30)
ar1.set("ali","reza")
print(ar1)