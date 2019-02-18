class Array (object):
    def __init__(self,size=32):
        self._size=size
        self._items=[None]*size
    def __getitem__(self,index):
        if index==None:
           raise Exception("invalid index",index) 
        return self._items[index]
    def __setitem__(self,index,value):
        if index is None:
            raise Exception("invalid index",index)
        self._items[index]=value
    def __len__(self):
        return self._size
    def clear(self,value=None):
        for i in range(self._size):
            self._items[i]=value
    def __iter__(self):
        for item in self._items:
            yield item
class FullError(Exception):
    pass
class ArrayQueue(object):
    def __init__(self,size):
        self._queue=Array(size)
        self._maxsize=size
        self.tail=0
        self.head=0
    def push(self,value):
        if len(self)>=self._maxsize:
            FullError("queue full")
        self._queue[self.tail%self._maxsize]=value
        self.head+=1
    def pop(self):
        if len(self)==0:
            FullError("not data to pop")
        value=self._queue[(self.tail)%self._maxsize]
        self.tail+=1
        return value
    def __len__(self):
        return self.head-self.tail
    def iter(self):
        for i in range(len(self)):
            yield self._queue[(i+self.head)%self._maxsize]    