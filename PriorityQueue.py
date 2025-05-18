from BST import BST
from MaxHeap import MaxHeap

class PriorityQueue:
    def __init__(self):
        self.BST = BST()
        self.heap = MaxHeap()
        
    def newRequest(self, pid, name, priority):
        self.BST.insertRequest(pid, name)
        self.heap.insertHeap(pid, priority)
        
    def process(self):
        return self.heap.processHighestPriorityRequest(self.BST)
        
    def increasePriority(self, pid, newPriority):
        return self.heap.increasePriority(pid, newPriority)

    def searchRequestByID(self,pid):
        request = self.BST.searchRequest(pid)
        return request
    
    def deleteRequestByID(self,pid):
        request = self.BST.deleteRequest(pid)
        self.heap.deleteById(pid)
        return request
        
    def showRequests(self):
        self.BST.showRequests()
        
    def visualizeTrees(self, mode='all'):
        if mode == 'BST':
            self.BST.visualizeBST()
        elif mode == 'heap':
            self.heap.visualizeHeap()
        else:
            self.BST.visualizeBST()
            self.heap.visualizeHeap()