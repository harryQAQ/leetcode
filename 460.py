class LFUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict, defaultdict
        self.freq = defaultdict(OrderedDict)
        self.key_to_freq = {}
        self.capacity = capacity
        self.min_freq = 0
    

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        key_freq = self.key_to_freq[key]
        res = self.freq[key_freq].pop(key)
        if not self.freq[key_freq] and 

    def put(self, key: int, value: int) -> None:
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)