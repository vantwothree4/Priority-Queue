from graphviz import Digraph

class BSTNode:

    def __init__(self,pid,name):
        self.id = pid
        self.name = name
        self.left = None
        self.right = None
        self.parent = None

    def nodeInfo(self):
        return f'id: {self.id}\nname: {self.name}'

class BST:

    def __init__(self):
        self.root = None
        self.BSTSize = 0
        
    def sizeBST(self):
        return self.BSTSize
    
    def isEmpty(self):
        if self.sizeBST():
            return False
        return True
            
    def insertRequest(self,pid,name):
        if self.isEmpty():
            self.root = BSTNode(pid,name)
        else:
            p, q = None, self.root
            while q:
                p = q
                if q.id < pid:
                    q = q.right
                else:
                    q = q.left
            newNode = BSTNode(pid,name)
            newNode.parent = p
            if p.id < pid: 
                p.right = newNode
            else:
                p.left = newNode
        self.BSTSize += 1

    def searchRequest(self,pid):
        p = self.root
        while p:
            if p.id == pid:
                return p
            elif p.id < pid:
                p = p.right
            else:
                p = p.left
        return None

    def treeMinimum(self,root):
        while root.left:
            root = root.left
        return root
        
    
    def transplant(self,u,v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def deleteRequest(self,pid):
        node = self.searchRequest(pid)
        if not node:
            return
        if not node.left:
            self.transplant(node, node.right)
        elif not node.right:
            self.transplant(node, node.left)
        else:
            successor = self.treeMinimum(node.right)
            if successor.parent != node:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
        self.BSTSize -= 1
        return node


    def preorderRecursive(self,root):
        if not root:
            return
        print(f'{root.name} id:({root.id})')
        self.preorderRecursive(root.left)
        self.preorderRecursive(root.right)
    
    def printBST(self):
        self.preorderRecursive(self.root)

    def inorderRecursive(self,root):
        if not root:
            return
        self.inorderRecursive(root.left)
        print(f'{root.name} id:({root.id})')
        self.inorderRecursive(root.right)
        
    def showRequests(self):
        self.inorderRecursive(self.root)
        
        
    def visualizeBST(self):
        dot = Digraph(format='png')
        dot.attr(bgcolor='#7AB2D3') 
        def add_nodes_edges(node):
            if not node:
                return
            node_id = str(id(node))
            dot.node(node_id, node.nodeInfo(), shape='ellipse', style='filled', fillcolor='#DFF2EB')    
            if node.left:
                left_id = str(id(node.left))
                dot.edge(node_id, left_id)
                add_nodes_edges(node.left)
            elif node.right:
                invisibleNode = f'invisible child left {node_id}'
                dot.node(invisibleNode, '', width='0.01', height='0.01', style='invis')
                dot.edge(node_id, invisibleNode, style='invis')
            if node.right:
                right_id = str(id(node.right))
                dot.edge(node_id, right_id)
                add_nodes_edges(node.right)
            elif node.left:
                invisibleNode = f'invisible child right {node_id}'
                dot.node(invisibleNode, '', width='0.01', height='0.01', style='invis')
                dot.edge(node_id, invisibleNode, style='invis')
        add_nodes_edges(self.root)
        dot.render('BST', view=True)
