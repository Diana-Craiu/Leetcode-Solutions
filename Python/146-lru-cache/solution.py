from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.keys=OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1 
        else:
            self.keys.move_to_end(key)
            return self.keys.get(key)

    def put(self, key: int, value: int) -> None:

        if key in self.keys:
            self.keys[key]=value
            self.keys.move_to_end(key)
        else:
            if len(self.keys) >= self.capacity:
                self.keys.popitem(last = False)
                self.keys[key]=value
                
            self.keys[key]=value
            self.keys.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)