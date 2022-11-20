from test_framework import generic_test
from test_framework.test_failure import TestFailure
"""
Linked hashmap for LRU cache

Maintain doubly linked list of entries, with head of list being dummy and in front being LRU node to be evicted and tail being where to insert new
Maintain fixed max capacity size 

Maintain hashmap mapping isbn/key to linked list node desired value for easy deletion and lookup

Each lookup should move node towards dummy head (LRU)

Each insertion beyond capacity size should lead to LRU eviction before insertion at tail

O(1) lookup with hashmap
O(1) insertion with hashmap + linked list
O(1) erase
O(1) ordering
"""

class Node:
    def __init__(self, prev, next, data) -> None:
        self.prev = prev
        self.next = next
        self.data = data

    def __repr__(self) -> str:
        res = []
        node = self
        while node is not None:
            res.append(node.data)
            node = node.next
        return ' <=> '.join(map(str, res))

class LruCache:
    def __init__(self, capacity: int) -> None:
        self.lru_head = Node(prev=None, next=None, data='LRU')
        self.tail = self.lru_head
        self.capacity = capacity
        self.size = 0
        self.map = {}
        return
    
    def make_mru(self, node: Node):
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

    def delete(self, node: Node):
        if node is self.tail:
            self.tail = node.prev
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def lookup(self, isbn: int) -> int:
        if isbn not in self.map:
            return -1
        else:
            node = self.map[isbn]
            price = node.data
            # move to end / tail
            # splice out node (prev <-> node <-> next =>>> prev <-> next)
            self.delete(node)
            # move node to tail and make it new tail (tail.prev <-> tail =>>> tail.prev <-> tail <-> node)
            self.make_mru(node)
            return price

    def insert(self, isbn: int, price: int) -> None:
        if isbn not in self.map:
            # create node and insert, may require evicting if at capacity
            if self.capacity == self.size:
                # evict LRU first
                evict_isbn = next((i for i, n in self.map.items() if n is self.lru_head.next))
                self.erase(evict_isbn)
            # create node and insert at mru
            node = Node(prev=None, next=None, data=price)
            self.make_mru(node)
            self.map[isbn] = node
            self.size += 1
        else:
            # just make the associated node mru with no price adjustment
            node = self.map[isbn]
            # splice out node
            self.delete(node)
            # add at MRU
            self.make_mru(node)
        return

    def erase(self, isbn: int) -> bool:
        if isbn in self.map:
            node = self.map[isbn]
            self.delete(node)
            del self.map[isbn]
            self.size -= 1
            return True
        else:
            return False


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
