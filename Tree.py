class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def Insert(self,node,data):
        if node == None :
            return Node(data)
        if node.data < data :
            node.right = self.Insert(node.right,data)
        elif node.data > data:
            node.left = self.Insert(node.left,data)
        return node

    def TranverseInOrder(self,node):
        if node == None:
            return node
        self.TranverseInOrder(node.left)
        print node.data
        self.TranverseInOrder(node.right)

    def TranversePostOrder(self,node):
        if node == None:
            return node
        self.TranversePostOrder(node.left)
        self.TranversePostOrder(node.right)
        print node.data

    def TranversePreOrder(self,node):
        if node == None:
            return node
        print node.data
        self.TranversePreOrder(node.left)
        self.TranversePreOrder(node.right)

    def Search(self,node,data):
        if node == None:
            return None
        if node.data == data:
            return node
        if node.data < data :
            return self.Search(node.right,data)
        else:
            return self.Search(node.left,data)
    def FindMinimum(self,node):
        if node.left == None and node.right == None:
            return node
        return self.FindMinimum(node.left)
        return self.FindMinimum(node.right)

    def Delete(self,node,data):
        if node == None:
            return Node
        if node.data < data:
            node.right = self.Delete(node.right,data)
        elif node.data > data:
            node.left = self.Delete(node.left,data)
        else:
            if node.left == None and node.right == None:
                return None
            if node.left == None:
                return node.right

            elif node.right == None:
                return node.left
            else:
                temp = self.FindMinimum(node.right)
                node.data = temp.data
                node.right = self.Delete(node.right,temp.data)
        return node
    def ConvertTreeintoLinkedList(self,node,list):
        if node == None:
            return None
        list.AddNode(node.data)
        self.ConvertTreeintoLinkedList(node.left,list)
        self.ConvertTreeintoLinkedList(node.right,list)
        return list

    def GetMaxHeightOfNode(self,node):
        if node == None :
            return 0
        return 1+ max(self.GetMaxHeightOfNode(node.left),self.GetMaxHeightOfNode(node.right))
    def IsTreeHeightBalanced(self,node):
        '''
        Its left subtree is height-balanced.
        Its right subtree is height-balanced.
        The difference between heights of left & right subtree is not greater than 1.
        :param node:
        :return:
        '''
        if node == None:
            return True
        return self.IsTreeHeightBalanced(node.left) and self.IsTreeHeightBalanced(node.right) and abs(self.GetMaxHeightOfNode(node.right)-self.GetMaxHeightOfNode(node.left)) <=1

    def ConvertIntoTreefromSortedArray(self,array,node=None):
        #print array
        if len(array) == 0:
            return None
        mid_pos = len(array)/2
        mid_ele = array[mid_pos]
        node = Node(mid_ele)
        node.left = self.ConvertIntoTreefromSortedArray(array[0:mid_pos],node.left)
        node.right = self.ConvertIntoTreefromSortedArray(array[mid_pos+1::],node.right)
        return node
    def GetParentofNode(self,node,data):
        if node == None :
            return None

        if node.left and node.left.data == data:
            return node
        if node.right and node.right.data == data:
            return node
        if data > node.data:
            return self.GetParentofNode(node.right,data)
        else:
            return self.GetParentofNode(node.left,data)

    def GetHeightofNode(self,node,data):
        if node == None:
            return None
        if node.data == data:
            return 0
        if data > node.data:
            return 1+self.GetHeightofNode(node.right,data)
        else:
            return 1+self.GetHeightofNode(node.left,data)
    def CheckTwoNodesareCousinNodes(self,root,data1,data2):
        if self.GetHeightofNode(root,data1) != self.GetHeightofNode(root,data2):
            return False
        if self.GetParentofNode(root,data1) == self.GetParentofNode(root,data2):
            return False
        return True
