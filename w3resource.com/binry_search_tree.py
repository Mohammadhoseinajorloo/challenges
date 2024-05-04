'''Algorithm to search for a key in a given Binary Search Tree:
 - Let’s say we want to search for the number X, We start at the root. Then:

1.We compare the value to be searched with the value of the root. 
2.If it’s equal we are done with the search if it’s smaller we know that we need to go to the left subtree because in a binary search tree all the elements in the left subtree are smaller and all the elements in the right subtree are larger. 
Repeat the above step till no more traversal is possible
3.If at any iteration, key is found, return True. Else False.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binarytree:
    def __init__(self):
        self.root = None

    # insert
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print('Data in tree Already')

    # remove
    def remove(self, data):
        if self.root != None:
            self._remove(data, self.root)

    def _remove(self, data, cur_node):
        if cur_node == None:
            return cur_node
        if data < cur_node.data:
            cur_node.left = self._remove(data, cur_node.left)
        elif data > cur_node.data:
            cur_node.right = self._remove(data, cur_node.right)
        else:
            if cur_node.left is None and cur_node.right is Node:
                print('Remove leaf node')
                if cur_node == self.root:
                    self.root=None
                    del cur_node
                    return None
            if cur_node.left is None:
                print('Removing none with right child')
                if cur_node == self.root:
                    self.root = cur_node.right
                tempnode = cur_node.right
                del cur_node
                return tempnode
            if cur_node.right is None:
                print('Removing none with left child')
                if cur_node == self.root:
                    self.root = cur_node.left
                tempnode = cur_node.left
                del cur_node
                return tempnode 
            print('Removing none with 2 children')
            tempnode = self.getpred(cur_node.left)
            cur_node.data = tempnode.data 
            cur_node.left = self._remove(cur_node.data, cur_node.left)

    def getpred(self, cur_node):
        if cur_node.right != None:
            return self.getpred(cur_node.right)
        return cur_node

    def inorder(self):
        if self.root != None:
            self._inorder(self.root)

    def _inorder(self, cur_node):
        if cur_node != None:
            self._inorder(cur_node.left)
            print(cur_node.data)
            self._inorder(cur_node.right)

    def preorder(self):
        if self.root != None:
            self._preorder(self.root)

    def _preorde(self, cur_node):
        if cur_node != None:
            print(cur_node.data)
            self._preorder(cur_node.left)
            self._preorder(cur_node.right)
    
    def postorder(self):
        if self.root != None:
            self._postorder(self.root)

    def _postorder(self, cur_node):
        if cur_node != None:
            self._postorder(cur_node.left)
            self._postorder(cur_node.right)
            print(cur_node.data)

    def minval(self):
        if self.root != None:
            self._minval(self.root)

    def _minval(self, cur_node):
        if cur_node.left != None:
            return self._minval(cur_node.left)
        return cur_node.data

    def maxval(self):
        if self.root != None:
            self._maxval(self.root)

    def _maxval(self, cur_node):
        if cur_node.right != None:
            return self._maxval(cur_node.right)
        return cur_node.data

    def search(self, data):
        if self.root != None:
            return self._search(data, self.root)

    def _search(self, data, cur_node):
        if cur_node is None or cur_node.data == data:
            return cur_node.data
        if data < cur_node.data:
           return self._search(data, cur_node.left)
        else:
            return self._search(data, cur_node.right)

if __name__ == '__main__':
    tree = Binarytree()

    tree.insert(100)
    tree.insert(90)
    tree.insert(110)
    tree.insert(95)
    tree.insert(30)

    print(tree.search(90))
    print(tree.search(30))


    tree.inorder()


    print(tree.minval())
    print(tree.maxval())



