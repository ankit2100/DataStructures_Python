__author__ = 'ankit.b.patel'

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class Linkedlist:
    def __init__(self):
        self.head = Node(None)
    def AddNode(self,data):
        newnode = Node(data)
        currnode = self.head.next
        if currnode == None:
            currnode = self.head
        while currnode.next is not None:
            currnode = currnode.next

        currnode.next = newnode
        newnode.prev = currnode
    def Print(self):
        currnode = self.head.next
        while currnode:
            print currnode.data,
            currnode = currnode.next
    def Reverse(self):
        head = self.head
        currnode = self.head.next
        prevnode = None
        while currnode is not None:
            nextnode = currnode.next
            currnode.next = prevnode
            currnode.prev = nextnode
            prevnode = currnode
            currnode = nextnode
        prevnode.prev = self.head
        head.next = prevnode
