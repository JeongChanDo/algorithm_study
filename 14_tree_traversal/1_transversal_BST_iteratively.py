from collections import deque
from binary_search_tree import BinarySearchTree, NodeBST

class BSTwithTransversalIterative(BinarySearchTree):

    def preorder(self):
        current = self.root
        nodes, stack= [], []
        while stack or current:
            if current:
                nodes.append(current.value)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return nodes
    
    def BFT(self):
        current = self.root
        nodes =[]
        queue = deque()
        queue.append(current)
        while queue:
            current = queue.popleft()
            nodes.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return nodes
    
if __name__ == "__main__":
    bst = BSTwithTransversalIterative()
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