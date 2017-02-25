#Implementing Singly Linked List
class Node:
    def __init__(self):
        self.next = None #Setting Next pointer to null
        self.data = None #setting data value to null
class LinkedList:

    def __init__(self):
        self.head = None
        self.currnode = None

    def GetLength(self):
        count = 0
        currnode=self.head
        while currnode:
            currnode = currnode.next
            count += 1
        return count

    def AddNode(self, data):
        newnode=Node()
        newnode.data = data
        if self.head is None:
            self.head = newnode
            self.currnode = self.head
        else:
            self.currnode.next = newnode
            self.currnode = newnode

    def GetNodeAtPosition(self,index):
        if index > self.GetLength():
            print "Index is bigger than Linkedlist size"
            return False
        currnode=self.head
        for i in range(0,index):
            currnode = currnode.next
        return currnode

    def InsertNodeAtPosition(self,data,index):
        print "Not implemented"

    def InsertNodeAfterNode(self,prevnode,data):
        if prevnode == None or prevnode == False:
            print "Previous node can not be null , Insert Failed."
            return False
        newnode = Node()
        newnode.data = data
        temp = prevnode.next
        prevnode.next = newnode
        newnode.next = temp

    def AddNodeInFront(self,data):
        newnode = Node()
        newnode.data = data
        newnode.next = self.head
        self.head = newnode #Its Must to make first element as Head

    def RemoveDuplicates_withbuffer(self):
        currnode=self.head
        mylist=list()
        while currnode:
            if currnode.data not in mylist:
                mylist.append(currnode.data)
                prev = currnode
            else:
                prev.next = currnode.next
            currnode = currnode.next

    def RemoveDuplicates_withoutbuffer(self):
        currnode=self.head
        mylist=list()
        while currnode:
            nextnode = currnode.next
            prev = currnode
            while nextnode :
                if nextnode.data == currnode.data :
                    prev.next = nextnode.next
                else:
                    prev = nextnode
                nextnode = nextnode.next
            currnode = currnode.next

    def Reverse(self):
        currnode = self.head
        prevnode = None
        while currnode :
            nextnode = currnode.next
            currnode.next = prevnode
            prevnode = currnode
            currnode = nextnode
        self.head = prevnode

    def FindnthToLastElement(self,n):
        '''
        Will return n to last elements
        :param n:
        :return:
        '''

        curr = self.head
        for i in range(n):
            curr = curr.next
        self.head = curr


    def Print(self):
        self.currnode = self.head
        while self.currnode:
            print self.currnode.data,
            self.currnode = self.currnode.next

#Implementation of Singly Linked List
ll = LinkedList()
ll.AddNode(1)
ll.AddNode(2)
ll.AddNode(1)
ll.AddNode(1)
ll.AddNode(1)

ll.Print()

'''
ll.AddNode(4)
ll.AddNode(4)
ll.AddNode(5)
ll.AddNode(5)
ll.AddNode(5)
ll.InsertNodeAfterNode(ll.GetNodeAtPosition(1),5)
ll.AddNodeInFront(10)
ll.Print()
#ll.RemoveDuplicates_withbuffer()
#ll.RemoveDuplicates_withoutbuffer()
print "\n"
ll.Print()
ll.Reverse()
print "\n\n Linked List After reverse"
ll.Print()

print "\nFinding nth to last element\n"
ll.FindnthToLastElement(3)
ll.Print()

'''

