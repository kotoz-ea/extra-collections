class TreeNode():
    def __init__(self, value):
        # assert value != None, "You can't use None as a value!!"
        self.data = value
        self.left = None
        self.right = None


    def __repr__(self):
        return str(self.data)


    def is_leaf(self):
        return self.left == self.right == None




class BinaryTree():
    def __init__(self, value):
        self.root = TreeNode(value)

    ############################## HEIGHT ##############################
    def __get_height(self, start_node):
        height = 0
        if start_node != None:
            left_height, right_height = 0, 0
            if start_node.left:
                left_height = 1 + self.__get_height(start_node.left)
            if start_node.right:
                right_height = 1 + self.__get_height(start_node.right)
            height += max(left_height, right_height)
            # print(start_node.data, left_height, right_height)
        return height


    def get_height(self):
        return self.__get_height(self.root)


    ############################## NODES ##############################
    def __get_nodes_per_level(self, start_node, level, level_nodes):
        if start_node != None:
            if level == len(level_nodes):
                level_nodes.append([])
            level_nodes[level].append(start_node.data)
            if start_node.left:
                self.__get_nodes_per_level(start_node.left,
                                           level+1,
                                           level_nodes)
            if start_node.right:
                self.__get_nodes_per_level(start_node.right,
                                           level+1,
                                           level_nodes)
        return level_nodes


    def get_nodes(self):
        return self.__get_nodes_per_level(self.root, 0, [])


    ############################## HEIGHT ##############################
    def __count_nodes(self, start_node):
        total_nodes = 0
        if start_node != None:
            total_nodes += 1
            if start_node.left:
                total_nodes += self.__count_nodes(start_node.left)
            if start_node.right:
                total_nodes += self.__count_nodes(start_node.right)
        return total_nodes


    def __len__(self):
        return self.__count_nodes(self.root)


    ######################### Pre-Order TRAVERSE #########################
    def __preorder_traverse(self, start_node):
        nodes = []
        if start_node != None:
            nodes.append(start_node.data)
            if start_node.left:
                nodes.extend(self.__preorder_traverse(start_node.left))
            if start_node.right:
                nodes.extend(self.__preorder_traverse(start_node.right))
        return nodes


    def preorder_traverse(self):
        return self.__preorder_traverse(self.root)


    ######################### Post-Order TRAVERSE #########################
    def __postorder_traverse(self, start_node):
        nodes = []
        if start_node != None:
            if start_node.left:
                nodes.extend(self.__postorder_traverse(start_node.left))
            if start_node.right:
                nodes.extend(self.__postorder_traverse(start_node.right))
            nodes.append(start_node.data)
        return nodes


    def postorder_traverse(self):
        return self.__postorder_traverse(self.root)


    ######################### In-Order TRAVERSE #########################
    def __inorder_traverse(self, start_node):
        nodes = []
        if start_node != None:
            if start_node.left:
                nodes.extend(self.__inorder_traverse(start_node.left))
            nodes.append(start_node.data)
            if start_node.right:
                nodes.extend(self.__inorder_traverse(start_node.right))
        return nodes


    def inorder_traverse(self):
        return self.__inorder_traverse(self.root)






if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.right.right = TreeNode(7)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    tree.root.left.left.right = TreeNode(10)
    #################################
    print("Tree Nodes:", len(tree))
    print("Tree Height:", tree.get_height())
    print("Nodes per level:", tree.get_nodes())
    print("PreOrder Traverse:")
    print(tree.preorder_traverse())
    print("\npostOrder Traverse:")
    print(tree.postorder_traverse())
    print("\ninOrder Traverse:")
    print(tree.inorder_traverse())
    # print(tree)
    # print(tree.root, tree.root.left.right, tree.root.left.left)