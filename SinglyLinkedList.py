class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
class LinkedList:

    def __init__(self):
        self.head = Node(None)
    def GetLength(self):
        count = 0
        if self.head.next == None:
            return count
        currnode=self.head.next
        while currnode:
            currnode = currnode.next
            count += 1
        return count

    def AddNode(self, data):
        newnode=Node(data)
        currnode = self.head.next
        if currnode is None:
            currnode = self.head
        #traversing through last element
        while currnode.next is not None:
            currnode = currnode.next
        currnode.next = newnode

    def GetNodeAtPosition(self,index):
        if index > self.GetLength():
            print "Index is bigger than Linkedlist size"
            return False
        currnode=self.head.next
        for i in range(0,index):
            currnode = currnode.next
        return currnode

    def InsertNodeAfterNode(self,prevnode,data):
        if prevnode == None or prevnode == False:
            print "Previous node can not be null , Insert Failed."
            return False
        newnode = Node(data)
        temp = prevnode.next
        prevnode.next = newnode
        newnode.next = temp

    def AddNodeInFront(self,data):
        newnode = Node(data)
        if self.head.next == None:
            self.head.next = newnode
        else:
            nextnode = self.head.next
            self.head.next = newnode
            newnode.next = nextnode

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
        currnode = self.head.next
        prevnode = None
        while currnode :
            nextnode = currnode.next
            currnode.next = prevnode
            prevnode = currnode
            currnode = nextnode
        self.head.next = prevnode

    def FindnthToLastElement(self,n):
        '''
        Will return n to last elements
        '''

        curr = self.head
        for i in range(n):
            curr = curr.next
        self.head = curr

    def DeleteNode(self,node):
        '''
        This fuction will delete node from linked list ,given access to that node only.
        :param node:
        :return:
        '''
        if node == None:
            print "Node can't be null\n"
            return
        print "Delete Node is :" +str(node.data)
        nextnode = node.next
        if nextnode == None :
            print "In this method of delete , Delete node can not be last one."
            return
        else:
            node.data = nextnode.data
            node.next = nextnode.next

    def AddLinkedListtoCurrent(self,otherlist):
        currnode_1 = self.head.next
        currnode_2 = otherlist.head.next
        reminder = 0
        while currnode_1 :
            sum = currnode_1.data + currnode_2.data + reminder

            if sum >= 10 :
                reminder = sum / 10
                sum = sum % 10
            currnode_1.data = sum
            currnode_1 = currnode_1.next
            currnode_2 = currnode_2.next

    def Print(self):
        self.currnode = self.head.next
        while self.currnode :
            print self.currnode.data,
            self.currnode = self.currnode.next
        print "\n"


