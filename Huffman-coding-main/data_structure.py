class Node:
    def __init__(self, n, char):
        self.n = n
        self.char = char
        self.left = None
        self.right = None
    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False

class HuffmanTree:
    def __init__(self,list_of_leaves):
        self.root = None
        self.number_of_nodes = len(list_of_leaves)
        self.list_of_leaves = list_of_leaves
        self.binary_codes_dict = {}

    def create_tree(self):
        # choose two nodes with minimum n and remove them from list
        temp = self.list_of_leaves.copy()
        while len(temp)>1:
            node_1 = min(temp,key=lambda node:node.n)
            temp.remove(node_1)
            node_2 = min(temp,key=lambda node:node.n)
            temp.remove(node_2)
            # connect the nodes together and create sub-node(left to right less to larger), add sub-node to list
            sub_node = self.create_sub_node(node_1,node_2)
            temp.append(sub_node)
        self.root = temp[0]
        return self.root

    def create_sub_node(self,node_1,node_2):
        if node_2.n < node_1.n:
            l_node, r_node = node_2, node_1
        else:
            l_node, r_node = node_1, node_2
        sub_node = Node(n=l_node.n+r_node.n, char=l_node.char+r_node.char)
        self.number_of_nodes+=1
        sub_node.left = l_node
        sub_node.right = r_node
        return sub_node

    def create_binary_codes(self,node,code=''):
        if node.is_leaf():
            self.binary_codes_dict[node.char] = code
        else:
            self.create_binary_codes(node.left,code+'0')
            self.create_binary_codes(node.right,code+'1')
