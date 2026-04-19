from collections import OrderedDict  # 相当于dict+双向链表
from typing import Optional


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last=False)  # last=False代表移动到最前面
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)
        if len(self.cache) > self.capacity:
            self.cache.popitem()


class Node:
    # 提高访问属性的速度，并节省内存
    __slots__ = 'prev', 'next', 'key', 'value'  # __slots__会限制类的属性只有这四个，减少额外开销

    def __init__(self, key: int=0, value: int=0) -> None:
        self.key = key
        self.value = value


class LRUCacheH:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.dummy = Node()  # 哨兵节点，用于连接头和尾，形成一个环形双向链表
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

    def remove(self, x: Node) -> None:
        """从双向链表中删去一个节点"""
        x.prev.next = x.next
        x.next.prev = x.prev

    def put_front(self, x: Node) -> None:
        """在双向链表的头部加一个节点"""
        x.prev = self.dummy
        x.next = x.prev.next
        x.prev.next = x
        x.next.prev = x

    def get_node(self, key: int) -> Optional[Node]:
        """获取key对应的节点,同时把该节点移动到最前面"""
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self.remove(node)
        self.put_front(node)
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        self.key_to_node[key] = node = Node(key, value)
        self.put_front(node)
        if len(self.key_to_node) > self.capacity:
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)
