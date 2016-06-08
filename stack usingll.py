def __init__(self, initdata):
        self.data = initdata
        self.next_node = None
 
class Stack (object):
    """ Implements a Stack using a Linked List"
    >>> s = Stack()
    >>> print(s)
    List for stack is: None
    >>> result = s.pop()
    Traceback (most recent call last):
    ...
    IndexError: Can't pop from empty stack.
    >>> s.push('a')
    >>> print(s)
    List for stack is: a -> None
    >>> s.length()
    1
    >>> s.pop()
    'a'
    >>> print(s)
    List for stack is: None
    >>> s.push('b')
    >>> print(s)
    List for stack is: b -> None
    >>> s.push('c')
    >>> print(s)
    List for stack is: c -> b -> None
    >>> s.length()
    2
    >>> s.peek()
    'c'
    >>> print(s)
    List for stack is: c -> b -> None
    >>> s.pop()
    'c'
    >>> print(s)
    List for stack is: b -> None
    """
 
    def __init__(self):
        self.head = None
 
    def push(self, item):
        """push a new item on to the stack"""
 
        temp = Node(item)
        temp.next_node = self.head
        self.head = temp
 
 
    def pop(self):
        """pop an item off the top of the stack, and return it
        If stack is empty you should raise an IndexError as per
        the comment below."""
 
        if self.isEmpty():
            raise IndexError("Can\'t pop from empty stack.")
        else:
            temp = self.head.data
            self.head = self.head.next_node
            return temp
 
        # use the following if stack is empty
        # raise IndexError("Can't pop from empty stack.")
 
    def peek(self):
        """pop an item on the top of the top of the stack, but don't remove it"""
 
 
 
        return   self.head.data
 
 
    def isEmpty(self):
        return self.head == None
 
    def length(self):
 
        count = 0
        a = self.head
        while a is not None:
            count+= 1
            a = a.next_node
 
        return count
 
 
    def __str__(self):
        b = []
        a = self.head
        while a is not None:
            b.append(str(a.data))
            a = a.next_node
 
 
        b.append('None')  
 
        return 'List for stack is: ' + (' -> '.join(b))
