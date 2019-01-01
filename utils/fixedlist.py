from utils.db import get_redis


class FixedList():
    def __init__(self, name='none', maximum_item_count: int=10):
        self.max_items = maximum_item_count
        self.name = name

    def append(self, *items):
        get_redis().rpush(self.name + ':list', *items)

        if self.len() >= self.max_items:
            get_redis().lpop(self.name + ':list')

    def len(self):
        return get_redis().llen(self.name + ':list')

    def sum(self):
        a = list()
        b = get_redis().lrange(self.name + ':list', 0, 20)
        for c in b:
            a.append(float(c))
        return sum(a)/len(a)
