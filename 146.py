from collections import OrderedDict
#OrderedDict会根据放入元素的先后顺序进行排序。
class LRUCache:
    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.lrucache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lrucache:
            # 说明在缓存中,重新移动字典的尾部
            self.lrucache.move_to_end(key)
        return self.lrucache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.lrucache:
            #若存在则删除
            del self.lrucache[key]
        # 在字典尾部添加
        self.lrucache[key] = value
        if len(self.lrucache) > self.maxsize:
            # 弹出字典的头部(因为存储空间不够了)
            self.lrucache.popitem(last = False)
