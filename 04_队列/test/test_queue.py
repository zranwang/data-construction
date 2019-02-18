class Node(object):
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
class LinkList(object):
    def __init__(self,maxsize=None):
        self._maxsize=maxsize
        self.root=Node()
        self.tailNode=None
        self._size=0
    def append(self,value):
        if len(self)>=self._maxsize:
            raise Exception("linklist is full")
        tailNode=self.tailNode
        curNode=Node(value)
        if self.tailNode is None:
            self.root.next=curNode
        else:
            tailNode.next=curNode
        curNode.next=tailNode
        self.tailNode=curNode
        self._size+=1
    def appendLeft(self,value):
        if len(self)>=self._maxsize:
            raise Exception("linklist is full")
        headNode=self.root.next
        curNode=Node(value)
        self.root.next=curNode
        curNode.next=headNode  
        if headNode is None:
            self.tailNode=curNode
        self._size+=1
    def popleft(self):
        if self._size is 0:
            raise Exception("linklist is empty")
        headNode=self.root.next
        self.root.next=headNode.next
        self._size-=1
        value=headNode.value
        del headNode
        return value
    def __len__(self):
        return self._size
    def iterNode(self):
        node=self.root.next
        while node is not self.tailNode:
            yield node
            node=node.next
        yield node
    def __iter__(self):
        for i in self.iterNode():
            yield i.value
    def remove(self,value):
        prevNode=self.root
        for curNode in self.iterNode():
            if curNode.value is value:
                prevNode.next=curNode.next
                self._size-=1
                del curNode
                return 1
            prevNode=curNode
        return -1
    def clear(self):
        for node in self.iterNode():
            del node
        self._size=0
        self.tailNode=None
    def find(self,value):
        index=0
        for curNode in self.iterNode():
            if curNode.value is value:
                return index
            index +=1
        return -1

class Queue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_link_list = LinkList(maxsize)

    def __len__(self):
        return len(self._item_link_list)

    def push(self, value):    # O(1)
        """ 队尾添加元素 """
        return self._item_link_list.append(value)

    def pop(self):
        """队列头部删除元素"""
        if len(self) <= 0:
            raise Exception('empty queue')
        return self._item_link_list.popleft()

def test_queue():
    q = Queue(4)
    q.push(0)
    q.push(1)
    q.push(2)

    assert len(q) == 3

    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2
test_queue()