from binary_search_tree import BinarySearchTree, NodeBST

class BSTwithTransversalRecursively(BinarySearchTree):

    def __init__(self):
        self.root = None
        self.nodes_BFS = []
        self.nodes_pre = []

    def BFT(self):
        self.root.level = 1
        queue = [self.root]
        current_level = self.root.level
    
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.level > current_level:
                current_level +=1
            self.nodes_BFS.append(current_node.value)
            
            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
        return self.nodes_BFS
    
    def preorder(self, node=None, level= 1):
        if not node and level == 1:
            node = self.root
        if node:
            self.nodes_pre.append(node.value)
            self.preorder(node.left, level+1)
            self.preorder(node.right, level+1)
        return self.nodes_pre

if __name__ == "__main__":
    bst = BSTwithTransversalRecursively()
    l = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]
    for i in l:
        bst.add_node(i)
    print("is node 8 leaf? : ", bst.is_leaf(8))
    print("what is level of node 8 : ", bst.get_node_level(8))
    print("is node 10 root? : ", bst.is_root(10))
    print("is node 1 root : ", bst.is_root(1))
    print("height of tree : ", bst.get_height())
    print("is this binary tree ? : ", bst.is_bst())
    print("is this balanced tree? :", bst.is_balanced())

    print("preorder : ", bst.preorder())
    print("bfs : ", bst.BFT())