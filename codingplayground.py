from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator

def bubbleSort(lst):
    no_of_pass = len(lst)
    for _ in range(len(lst)-1):
        no_of_pass -= 1
        exchanges = False
        for i in range(no_of_pass):
            if lst[i] > lst[i+1]:
                lst[i+1], lst[i] = lst[i], lst[i+1]
                exchanges = True
        if exchanges == False:
            break
    print(lst)
    return lst

def selectionSort(lst):
    for i in range(len(lst)):
        index_of_max = 0
        for j in range(len(lst)-i):
            if lst[j] > lst[index_of_max]:
                index_of_max = j
        lst[index_of_max], lst[len(lst)-1-i] = lst[len(lst)-1-i], lst[index_of_max]
    print(lst)
    return lst

def insertionSort(lst):
    sortedList = [lst[0]]
    for i in range(1,len(lst)):
        if lst[i] > sortedList[-1]:
            sortedList.append(lst[i])
        elif lst[i] < sortedList[0]:
            sortedList.insert(0, lst[i])
        else:
            for j in range(len(sortedList)-1):
                if sortedList[j] <= lst[i] and lst[i] <= sortedList[j+1]:
                    sortedList.insert(j+1, lst[i])
                    break
    #print(sortedList)
    return sortedList

def shellSort(lst):
    increment = 3
    list_of_lists = []
    merged_list = []
    for i in range(increment):
        sublist = lst[i::increment]
        list_of_lists.append(insertionSort(sublist))
    for i in range(increment):
        for sublistitem in list_of_lists:
            try:
                merged_list.append(sublistitem[i])
            except:
                continue
    return insertionSort(merged_list)

def reversebubbleSort(lst):
  for i in range(len(lst) - 1):
    for j in range(i, len(lst)):
      if lst[i] > lst[j]:
        lst[i], lst[j] = lst[j], lst[i]
        print(lst)
  return lst

def mergeSort(lst):
    def merge(left, right):
        result = []
        i = 0
        j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    if len(lst) <= 1:
        return lst
    else:
        number = len(lst)//2
        left = mergeSort(lst[:number])
        right = mergeSort(lst[number:])
        return merge(left, right)

def quickSort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot_value = lst[0]
        i = 1
        j = len(lst)-1

        while i <= j:
            while lst[i] <= pivot_value and i <= j:
                i += 1
                if i > len(lst)-1:
                    break
            while lst[j] >= pivot_value and i <= j:
                j -= 1
                if j < 0:
                    break
            if i < j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
        
        lst[0], lst[j] = lst[j], lst[0]
        
        left = quickSort(lst[:j])
        right = quickSort(lst[j+1:])
        return left + [lst[j]] + right
    
def BinaryTree(r):
    return [r, [], []]

def insertLeft(atree, newnode):
    t = atree.pop(1)
    atree.insert(1, [newnode, t, []])
    return atree

def insertRight(atree, newnode):
    t = atree.pop(2)
    atree.insert(2, [newnode, [], t])
    return atree

def getRootVal(atree):
    return atree[0]

def setRootVal(atree, newval):
    atree[0] = newval

def getLeftChild(atree):
    return atree[1]

def getRightChild(atree):
    return atree[2]

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRootVal(self):
        return self.key
    
    def setRootVal(self, newval):
        self.key = newval

    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild

def buildParseTree(astring):
    lst = astring.split()
    astack = Stack()
    aTree = BinaryTree('')
    astack.push(aTree)
    currentTree = aTree

    for char in lst:
        if char == '(':
            currentTree.insertLeft('')
            astack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif char in ['+', '-', '*', '/']:
            currentTree.setRootVal(char)
            currentTree.insertRight('')
            astack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif char == ')':
            currentTree = astack.pop()
        else:
            currentTree.setRootVal(int(char))
            currentTree = astack.pop()
    return aTree

def evaluate(parseTree):
    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()
    
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightCHild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self, lst):
        i = len(lst) // 2
        self.currentSize = len(lst)
        self.heapList = [0] + lst[:]
        while i > 0:
            self.percDown(i)
            i -= 1
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent = currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent = currentNode)
    def __setitem__(self, key, val):
        self.put(key, val)
    
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)
    def __getitem__(self, key):
        return self.get(key)
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        return False
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')
    def __delitem__(self, key):
        self.delete(key)
    def remove(self, currentNode):
        parent = currentNode.parent
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                parent.leftChild = None
            else:
                parent.rightChild = None
        elif not currentNode.hasBothChildren():
            if currentNode.hasLeftChild():
                child = currentNode.leftChild
                if currentNode.isLeftChild():
                    child.parent = parent
                    parent.leftChild = child
                elif currentNode.isRightChild():
                    child.parent = parent
                    parent.rightChild = child
                else:
                    currentNode.replaceNodeData(child.key, child.payload, child.leftChild, child.rightChild)
            else:
                child = currentNode.RightChild
                if currentNode.isLeftChild():
                    child.parent = parent
                    parent.leftChild = child
                elif currentNode.isRightChild():
                    child.parent = parent
                    parent.rightChild = child
                else:
                    currentNode.replaceNodeData(child.key, child.payload, child.leftChild, child.rightChild)
        else:
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            

class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    
    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)
    
    def hasAnyChildren(self):
        return not self.isLeaf()
    
    def hasBothChildren(self):
        return self.leftChild and self.rightChild
    
    def replaceNodeData(self, key, val, left, right):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild()
        return current
    
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.leftChild.parent = self.parent
                    self.parent.leftChild = self.leftChild
                else:
                    self.leftChild.parent = self.parent
                    self.parent.rightChild = self.leftChild
            else:
                if self.isLeftChild():
                    self.rightChild.parent = self.parent
                    self.parent.leftChild = self.rightChild
                else:
                    self.rightChild.parent = self.parent
                    self.parent.rightChild = self.rightChild
    
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

class AVLTree(BinarySearchTree):
    def __init__(self, key, val, left = None, right = None, parent = None):
        super.__init__(key, val, left = None, right = None, parent = None)

    def _put(self,key,val,currentNode):   # Override the _put method
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)   # New addition of updateBalance method
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)
    
    def updateBalance(self, node):   # Implements the recursive updating
        if node.balanceFactor > 1 or node.balanceFactor < -1: # Modify TreeNode to include a balanceFactor attribute, and thus modify BinarySearchTree
            self.rebalance(node)     # Rebalancing a node moves it to a more balanced position
            return                   # Terminate the method early
        if node.parent != None:      # Check for base case 1
            if node.isLeftChild():
                node.parent.balanceFactor += 1 # Update parent balance factor
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0: # Check for base case 2
                self.updateBalance(node.parent)

'''
First check is rebalancing is needed. If needed, then performed, and done. Else, continue balancing parents.
Efficient rebalancing is key to making the AVL perform well.

Perform one or more rotations on the tree
--Diagram of Rotation--
Left Rotation:
- Promote right child to the root
- Move old root to the left child
- The left child (if any) getting replaced is the right child of the replacement
Reversed for the Right Rotation.
Need to ensure BST properties are preserved, and update all parent pointers.
'''