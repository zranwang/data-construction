class Node(object):
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next       
class LinkList(object):
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.root=Node()
        self.tailNode=None
        self.length=0
    def append(self,value=None):
        if self.length>self.maxSize:
            raise Exception('the link is full')
        node=Node(value)
        tailNode=self.tailNode
        if self.tailNode==None:
            self.root.next=node
            self.tailNode=node
        else:
            tailNode.next=node
            self.tailNode=node
        self.length+=1
    def appendLeft(self,value):
        if self.length>self.maxSize:
            raise Exception('the link is full')
        node=Node(value)
        if self.tailNode==None:
            self.root.next=node
            self.tailNode=node
        else:
            headNode=self.root.next
            self.root.next=node
            node.next=headNode
        self.length+=1
    def iter_node(self):
        curnode=self.root.next
        while curnode is not self.tailNode:
            yield curnode
            curnode=curnode.next
        if curnode is None:
            yield curnode
    def removeNode(self,value):
        preNode=self.root
        for curnode in self.iter_node():
            if value is curnode.value:
                preNode.next=curnode.next
                if curnode is self.tailNode:
                    self.tailNode=preNode
                del curnode
                self.length-=1
                return 1
            else:
                preNode=curnode
        return -1
    def findNode(self,value):
        index=0
        for node in self.iter_node():
            if node.value is value:
                return index
            index +=1
    def reverse(self):
        headNode=self.root.next
        preNode=None
        curNode=self.root.next
        while curNode:
            nextNode=curNode.next
            curNode.next=preNode
            preNode=curNode
            curNode=nextNode
        self.root.next=curNode
        self.tailNode=headNode