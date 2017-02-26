__author__ = 'ankit.b.patel'
import SinglyLinkedList
import DoublyLinkedList

if __name__ == "__main__":
    #-----------------Implementation of Singly Linked List------------------#
    ll = SinglyLinkedList.LinkedList()
    print "Before Adding Nodes :"
    ll.Print()
    ll.AddNode(1)
    ll.AddNode(2)
    ll.AddNode(1)
    ll.AddNode(1)
    ll.AddNode(1)
    ll.AddNode(3)
    ll.AddNode(4)
    ll.AddNode(5)
    ll.AddNode(1)
    ll.AddNode(5)
    print "After Adding Nodes :"
    ll.Print()

    ll.InsertNodeAfterNode(ll.GetNodeAtPosition(1),5)
    print "After Inserting node (data=5) at position 2"
    ll.Print()


    ll.AddNodeInFront(10)
    print "After Inserting node at Front"
    ll.Print()

    ll.RemoveDuplicates_withbuffer()
    print "After Removing Duplicates : "
    ll.Print()

    ll.Reverse()
    print "After Reversing List : "
    ll.Print()

    ll.FindnthToLastElement(0)
    print "Finding nth(n=4) to last element"
    ll.Print()

    ll.DeleteNode(ll.GetNodeAtPosition(1))
    print "Deleting node"
    ll.Print()

    ########----------------Adding two Singly linked lists -------------------#######
    #
    ll = SinglyLinkedList.LinkedList()
    ll.AddNode(3)
    ll.AddNode(1)
    ll.AddNode(5)
    l2 = SinglyLinkedList.LinkedList()
    l2.AddNode(5)
    l2.AddNode(9)
    l2.AddNode(2)

    ll.AddLinkedListtoCurrent(l2)
    print "After Adding Another List"
    ll.Print()


    #-----------------Implementation of Doubly Linked List------------------#
    dl = DoublyLinkedList.Linkedlist()
    print "\nBefore Adding Nodes : "
    dl.Print()
    dl.AddNode(1)
    dl.AddNode(2)
    dl.AddNode(3)
    dl.AddNode(4)
    dl.AddNode(5)
    dl.AddNode(6)
    print "\nAfter Adding Nodes : "
    dl.Print()

    dl.Reverse()
    print "\nAfter Reverse : "
    dl.Print()