# 문제 링크: https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        self.capacity = 1000
        self.hash_buckets = {}

    def add(self, key: int) -> None:
        if self.contains(key):
            return

        hash_key = self.get_hash(key)
        if hash_key not in self.hash_buckets:
            self.hash_buckets[hash_key] = []
        self.hash_buckets[hash_key].append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return

        hash_key = self.get_hash(key)
        self.hash_buckets[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = self.get_hash(key)
        return hash_key in self.hash_buckets and key in self.hash_buckets[hash_key]
    
    def get_hash(self, key: int) -> int:
        return key % self.capacity


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)