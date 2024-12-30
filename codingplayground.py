from pythonds.basic import Stack
from pythonds.trees import BinaryTree
from pythonds.graphs import PriorityQueue, Graph, Vertex
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
    
    def rotateLeft(self, rotRoot):                  # The case of rotateRight is analogous
        newRoot = rotRoot.rightChild                # Temporary variable to store new root
        rotRoot.rightChild = newRoot.leftChild      # Child switches parent after rotation
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot      # Fix pointer of switched child after rotation
        newRoot.parent = rotRoot.parent             # Ensure consistency in case rotation is not at the root node
        if rotRoot.isRoot():                        # Case 1: Old root no parents
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():               # Case 2: Old root is left child
                rotRoot.parent.leftChild = newRoot  # Update pointer
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot                 # Update pointers
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(0, newRoot.balanceFactor) # Requires some derivation
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(0, rotRoot.balanceFactor)
    
    def rebalance(self, node):
        if node.balanceFactor < 0:   # Right heavy, need to do left rotation first
            if node.rightChild.balanceFactor > 0: # Check whether right child is left heavy
                self.rotateRight(node.rightChild) # Rotate left-heavy right child first
            self.rotateLeft(node)    # Proceed with left rotation
        elif node.balanceFactor > 0: # Left heavy, need to do right rotation first
            if node.leftChild.balanceFactor < 0:  # Proceed analogously
                self.rotateLeft(node.leftChild)
            self.rotateRight(node)


class Vertex:           # Dictionary of other connected vertices
    def __init__(self, key):
        self.id = key   # Initialise attributes
        self.connectedTo = {}
    
    def addNeighbour(self, nbr, weight = 0):  # Optional weight parameter
        self.connectedTo[nbr] = weight        # That defaults to 0

    def getConnections(self):   # Accessor
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    def __str__(self):  # Allows printing of Vertex class
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
class Graph:           # Master dictionary of vertices
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        return None
    
    def addEdge(self, f, t, weight = 0):
        if f not in self.vertList:  # Vertices must exist
            newVertex = self.addVertex(f)
        if t not in self.vertList:  # For an edge to be added
            newVertex = self.addVertex(t)
        self.vertList[f].addNeighbour(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()
    
    def __contains__(self, n):  # Allows graph membership testing
        return n in self.vertList

    def __iter__(self):         # Allows graph iteration
        return iter(self.vertList.values())

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r') # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

def bfs(g, start):
    start.setDistance(0)                        # Initialise starting vertex
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':       # White is undisocvered
                nbr.setColor('gray')            # Gray is currently being explored
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')           # Black is fully explored, no adjacent white vertices

def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row,col,bdSize)
            newPositions = genLegalMoves(row,col,bdSize)
            for e in newPositions:
               nid = posToNodeId(e[0],e[1],bdSize)
               ktGraph.addEdge(nodeId,nid)
    return ktGraph
    
def posToNodeId(row, column, board_size):
    return (row * board_size) + column # Node ID starts from 0 on the top left,
                                           # increasing along the row
        
def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves
    
def legalCoord(x,bdSize):
    if x >= 0 and x < bdSize:
        return True
    return False

def knightTour(n, path, u, limit): # Parameters are current depth, list of visited vertices, a candidate vertex, and the number of nodes in the path
    u.setColor('gray')                 # Gray vertices are visited
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor == 'white': # White vertices are visited
                done = knightTour(n+1, path, nbrList[i], limit)      # Recursive call
                i += 1
        if not done:                               # Prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True         # Base case, path with 64 vertices returns a successful tour
    return done

def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resList.append((c,v))
    resList.sort(key = lambda x: x[0])
    return [y[1] for y in resList]


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
        self.sccs = []
            
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)          # Vertex has no predecessor
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
                    
    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)
    
    def toposort(self): # New method for DFSGraph class
        self.dfs()      # Perform DFS to get times
        sorted_verts = sorted(self, key=lambda vert: vert.getFinish(), reverse = True)
        return [vert.getName() for vert in sorted_verts]

    def transpose(self): # No built-in transpose method
        gt = DFSGraph()
        for vertex in self: # Note that Graph has an adjacency list implementation
            gt.addVertex(vertex.getName())
        for vertex in self:
            for neighbour in vertex.getConnections():
                gt.addEdge(neighbour.getName(), vertex.getName()) # Reversed edges
        return gt

    def scc(self): # New method for DFSGraph class
        self.dfs()
        gt = self.transpose()
        self.time = 0 # Reset time before DFS on transpose

        sorted_verts = sorted(self, key=lambda vert: vert.getFinish(), reverse=True)

        for aVertex in gt: # Similar to dfsvisit method
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in sorted_verts: # Now in reverse order
            if aVertex.getColor() == 'white':
                component = [] # Storing each SCC
                self.sccdfsvisit(gt, aVertex, component)
                self.sccs.append(component) # Add a sccs attribute to DFSGraph before this
            
        return self.sccs
    
    def sccdfsvisit(self, gt, startVertex, component): # SCC variant of dfsvisit
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        component.append(startVertex.getName()) # Add to current SCC
        for nextVertex in startVertex.getConnections(): # Uses gt as intended
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.sccdfsvisit(gt, nextVertex, component)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)

def prim(G,start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
          newCost = currentVert.getWeight(nextVert)
          if nextVert in pq and newCost<nextVert.getDistance():
              nextVert.setPred(currentVert)
              nextVert.setDistance(newCost)
              pq.decreaseKey(nextVert,newCost)


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Each element is its own parent initially
        self.rank = [0] * size  # Rank is initially 0 for all elements

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:  # Only merge if they are in different sets
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(num_vertices, edges):
    edges.sort(key=lambda x: x[2])   # Sort edges by weight
    uf = UnionFind(num_vertices)
    mst = []
    total_cost = 0
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v): # No cycle
            uf.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight
    return mst, total_cost