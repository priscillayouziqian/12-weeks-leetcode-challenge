# 155 min stack
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Only push to min_stack if it's empty or the new value is less than or equal to the current minimum, [-1] means last element
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            # Pop from the main stack
            val = self.stack.pop()
            # If the popped value is the current minimum, pop it from the min_stack as well
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


# 705 design hash set
class MyHashSet:
    # using build in set
    def __init__(self):
        self.hashSet = set()
    
    def add(self, key: int) -> None:
        self.hashSet.add(key)
    
    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashSet


# 706 design hash map
class MyHashMap:
    def __init__(self):
        self.hashMap = {}

    def put(self, key: int, value: int) -> None:
        # inserts a (key, value) pair into hashmap
        self.hashMap[key] = value

    def get(self, key: int) -> int:
        # search for key, return value to the key, otherwise, return -1
        if key in self.hashMap:
            return self.hashMap[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hashMap:
            # remove both key and value
            del self.hashMap[key]