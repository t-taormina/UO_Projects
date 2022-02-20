"""
CIS 211 Lab 4
Author: Tyler Taormina
Credits:
Description:

"""

class Node():
    """Abstract base class"""
    def __init__(self, node_data: int):
        self.node_data = node_data

    def sum_node_data(self, left: "Node", right: "Node"):
        raise NotImplementedError("All classes must have sum_node_data method")

    def __str__(self):
        raise NotImplementedError("Not implemented for abstract class")

class Leaf(Node):
    def __init__(self, node_data: int):
        self.node_data = node_data

    def sum_node_data(self) -> int:
        return self.node_data

    def __str__(self) -> str:
        return f"{self.node_data}"

class Internal(Node):
    def __init__(self, node_data: int, left: Node, right: Node):
        self.node_data = node_data
        self.left = left
        self.right = right

    def sum_node_data(self) -> int:
        #when we initialize things, we don't need them in parameters
        left_value = self.left.sum_node_data()
        right_value = self.right.sum_node_data()
        return self.node_data + left_value + right_value

    def __str__(self) -> str:
        left_str = str(self.left)
        right_str = str(self.right)
        return f"<{self.node_data}, {left_str}, {right_str}>"



def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    print(root.sum_node_data())
    print(root)

if __name__ == '__main__':
    main()