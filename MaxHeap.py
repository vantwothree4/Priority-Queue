
from graphviz import Digraph
from BST import BST

class HeapNode:

    def __init__(self, pid, priority):
        self.priority = priority
        self.id = pid
    
    def printNode(self):
        print(f'({self.priority}, id: {self.id})',end=' ')
    
    def nodeInfo(self):
        return f'priority: {self.priority} \n id: {self.id}'

class MaxHeap:

    def __init__(self):
        self.heap = ["Zero index"]
        self.heapSize = 0

    def sizeMaxHeap(self):
        return self.heapSize

    def isEmpty(self):
        if self.sizeMaxHeap():
            return False
        return True
        
        
    def maxheapify(self,index):
        left = 2 * index
        right = 2 * index + 1
        if left <= self.heapSize and (self.heap[left]).priority > (self.heap[index]).priority:
            largest = left
        else:
            largest = index
        if right <= self.heapSize and (self.heap[right]).priority > (self.heap[largest]).priority:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.maxheapify(largest)

    def findIndex(self,pid):
        for i in range(self.heapSize, 0, -1):
            if (self.heap[i]).id == pid:
                return i
        return None
    
    def increasePriority(self, pid, newPriority):
        index = self.findIndex(pid)
        if not index or newPriority < (self.heap[index]).priority:
            return False
        (self.heap[index]).priority = newPriority
        while index > 1 and (self.heap[index // 2]).priority < (self.heap[index]).priority:
                self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
                index = index // 2
        return True
            
    def insertHeap(self,pid,priority):
        newRequest = HeapNode(pid , -1)
        self.heap.append(newRequest)
        self.heapSize += 1
        self.increasePriority(pid,priority)
        
    def printHeap(self):
        levelNodes = 1
        i = 1
        while 1:
            for _ in range(levelNodes):
                if i > self.heapSize:
                    return
                self.heap[i].printNode()
                i += 1
            print()
            levelNodes *= 2
    
    def visualizeHeap(self):
        dot = Digraph(format='png')
        dot.attr(bgcolor='#7AB2D3') 
    
        for i in range(1, self.heapSize + 1):
            dot.node( str(i), label=self.heap[i].nodeInfo(), shape='ellipse', style='filled', fillcolor='#DFF2EB')
            if 2 * i <= self.heapSize:
                dot.edge(str(i), str(2 * i))
            if 2 * i + 1 <= self.heapSize:
                dot.edge(str(i), str(2 * i + 1))
        dot.render('heap', view=True)
        
    def deleteMaxHeap(self):
        if self.isEmpty():
            return None
        request = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heapSize -= 1
        self.heap.pop()
        self.maxheapify(1)
        return request
        
    def processHighestPriorityRequest(self,BSTtree: BST):
        request = self.deleteMaxHeap()
        if request:
            return BSTtree.deleteRequest(request.id)
            
    def deleteById(self, pid):
        index = self.findIndex(pid)
        if not index:
            return
        self.heap[index] = self.heap[-1]
        self.heapSize -= 1
        self.heap.pop()
        self.maxheapify(index)        
    
