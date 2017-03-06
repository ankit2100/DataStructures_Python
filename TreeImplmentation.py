__author__ = 'ankit.b.patel'
import Tree
import SinglyLinkedList
if __name__ == "__main__":
    #Tree operations Insert, Search , Delete ,Traversal
    t = Tree.Tree()
    root = t.Insert(None,10)
    t.Insert(root,20)
    t.Insert(root,5)
    t.Insert(root,1)
    t.Insert(root,15)
    t.Insert(root,25)
    t.Insert(root,12)
    t.Insert(root,18)
    if t.Search(root,12):
        print "Node found"
    else:
        print "Note not found"
    t.Delete(root,10)
    print "Traversing"
    t.TranverseInOrder(root)

    #Converting Tree into Linked List
    t = Tree.Tree()
    root = t.Insert(None,1)
    t.Insert(root,2)
    t.Insert(root,3)
    t.Insert(root,4)
    t.Insert(root,5)
    t.Insert(root,6)
    ll=SinglyLinkedList.LinkedList()
    t.ConvertTreeintoLinkedList(root,ll)
    print "Printing Linked 1ist"
    ll.Print()


    #Checking if Tree is Height Balanced or not
    t = Tree.Tree()
    root = t.Insert(None,10)
    t.Insert(root,5)
    t.Insert(root,3)
    t.Insert(root,1)
    t.Insert(root,15)
    t.Insert(root,20)
    t.Insert(root,25)

    print "Printing Height"
    print t.IsTreeHeightBalanced(root)

    #Converting sorted array into Binary tree
    t = Tree.Tree()
    root=t.ConvertIntoTreefromSortedArray([2,5,8,9,10,12,15],None)
    t.TranverseInOrder(root)
    print t.IsTreeHeightBalanced(root)


    #Finding nodes are cousin nodes
    print "Finding Cousin Nodes"
    t = Tree.Tree()
    root = t.Insert(None,10)
    t.Insert(root,5)
    t.Insert(root,2)
    t.Insert(root,7)
    t.Insert(root,15)
    t.Insert(root,12)
    t.Insert(root,17)
    print t.CheckTwoNodesareCousinNodes(root,5,17)