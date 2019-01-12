from abc import ABC, abstractmethod

from binary_tree import TreeNode, BinaryTree


class Heap(ABC):

    @abstractmethod
    def heapify(lst):
        length = len(lst)
        if length == 1:
            node = TreeNode(lst[0])
        elif length == 2:
            node = TreeNode(lst[0])
            node.left = TreeNode(lst[1])
        else:
            node = TreeNode(lst[0])
            node.left = Heap.heapify(lst[1::2])
            node.right = Heap.heapify(lst[2::2])
        return node






class MinHeap():

    def __init__(self, value):
        if type(value) in {list, set, frozenset}:
            lst = sorted(value)
            self.heap = lst
        elif type(value) in {int, float}:
            self.heap = [value]
        else:
            raise ValueError("Unsupported datatype!!")


    def __repr__(self):
        root = Heap.heapify(self.heap)
        return str( BinaryTree(root) )

    
    def insert(self, value):
        # add the new value
        self.heap.append(value)
        # swap between parents when needed
        idx = len(self.heap)-1
        while(idx != 0):
            parent_idx = (idx-1)//2
            current = self.heap[idx]
            parent = self.heap[parent_idx]
            if parent > current:
                self.heap[parent_idx], self.heap[idx] = \
                                        self.heap[idx], self.heap[parent_idx]
                idx = parent_idx
            else:
                break







if __name__ == "__main__":
    heap = MinHeap([1,2,3,4])
    heap.insert(1)
    heap.insert(2)
    print(heap)