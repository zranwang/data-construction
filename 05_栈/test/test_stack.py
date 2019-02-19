class Node(object):
    def __init__(self,value=None):
        self.next=None
        self.preNode=None
        self.value=value
class CircularDoubleLinkedList(object):
    def __init__(self,maxsize=None):
        node=Node()
        node.next=node
        node.preNode=node
        self.root=Node()
        self.maxSize=maxsize
        self.length=0
    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.preNode
    def append(self,value):
        if self.length>=self.maxSize:
            raise Exception("the doubleLinkedList is full")
        node=Node(value)
        headNode=self.root.next
        if headNode is None:
            self.root.next=node
            node.preNode=self.root
            self.root.preNode=node
            node.next=self.root
        else:
            self.root.preNode.next=node
            node.preNode=self.root.preNode
            node.next=self.root
            self.root.preNode=node
        self.length +=1
        """or writing as follows: 
        tailnode=self.root.preNode or self.root
        tailnode.next=node
        node.preNode=tailnode
        node.next=self.root
        self.root.preNode=node
        self.length +=1
        """
    def appendleft(self,value):
        if self.length>=self.maxSize:
            raise Exception("the doubleLinkedList is full")
        node=Node(value)
        headNode=self.root.next
        if headNode is None:
            self.root.next=node
            node.preNode=self.root
            self.root.preNode=node
            node.next=self.root
        else:
            node.next=headNode
            node.preNode=headNode.preNode
            headNode.preNode=node
            self.root.next=node
        self.length+=1
    def iter_node(self):
        node=self.root.next
        if node is self.root:
            return
        while node is not self.root:
            yield node
            node=node.next
    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    def remove(self,node):
        if node is self.root:
            raise Exception("can not delete root")
        node.preNode.next=node.next
        node.next.preNode=node.preNode
        del node
        self.length-=1
        return 1
    def iter_node_reverse(self):
        node=self.root.preNode
        if node is self.root:
            return
        while node is not self.root:
            yield node
            node=node.preNode
class Deque(CircularDoubleLinkedList):
    def popleft(self):
        if len(self) == 0:
            raise Exception('empty')
        headNode=self.root.next
        value=headNode.value
        self.remove(headNode)
        return value
    def pop(self):
        if len(self) == 0:
            raise Exception('empty')
        tailNode=self.root.preNode
        value=tailNode.value
        self.remove(tailNode)
        return value

class Stack(object):
    def __init__(self,maxsize=None):
        self.stack=Deque(maxsize)
    def pop(self):
        return self.stack.pop()
    def push(self,value):
        self.stack.append(value)
def test_stack():
    s = Stack(5)
    s.push(0)
    s.push(1)
    s.push(2)

    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0


if __name__ == '__main__':
    test_stack()