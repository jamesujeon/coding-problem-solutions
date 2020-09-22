# 문제 링크: https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.buckets = [{}] * capacity

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self.get_hash(key)]
        bucket[key] = value

    def get(self, key: int) -> int:
        bucket = self.buckets[self.get_hash(key)]
        return bucket[key] if key in bucket else -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[self.get_hash(key)]
        if key in bucket:
            del bucket[key]

    def get_hash(self, key: int) -> int:
        return key % self.capacity


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)