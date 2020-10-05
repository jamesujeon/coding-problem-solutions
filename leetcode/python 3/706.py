# 문제 링크: https://leetcode.com/problems/design-hashmap/

class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self, capacity: int = 10000):
        self.capacity = capacity
        self.buckets = [None] * capacity

    def put(self, key: int, value: int) -> None:
        hash_key = self.get_hash(key)
        prev_bucket = bucket = self.buckets[hash_key]
        while bucket:
            if bucket.key == key:
                bucket.value = value
                return
            prev_bucket, bucket = bucket, bucket.next

        if prev_bucket:
            prev_bucket.next = Node(key, value)
        else:
            self.buckets[hash_key] = Node(key, value)

    def get(self, key: int) -> int:
        bucket = self.buckets[self.get_hash(key)]
        while bucket:
            if bucket.key == key:
                return bucket.value
            bucket = bucket.next
        return -1

    def remove(self, key: int) -> None:
        hash_key = self.get_hash(key)
        bucket = self.buckets[hash_key]
        if not bucket:
            return

        if bucket.key == key:
            self.buckets[hash_key] = bucket.next
        else:
            prev_bucket, bucket = bucket, bucket.next
            while bucket:
                if bucket.key == key:
                    prev_bucket.next = bucket.next
                    return
                prev_bucket, bucket = bucket, bucket.next

    def get_hash(self, key: int) -> int:
        return key % self.capacity


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)