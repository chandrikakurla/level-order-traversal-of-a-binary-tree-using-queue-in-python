#importing queue datastructure
from queue import Queue
que=Queue()
#class to create nodes of class
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
#function to print nodes of a tree in level order
def print_Levelorder(root):
    #if tree is empty
    if root is None:
        return
    #enqueue root of a tree into queue
    que.put(root)
    while(True):
        if que.empty():
            return
        temp=que.get()
        if temp.left is not None:
            #enqueue left node of temp into queue
            que.put(temp.left)
        if temp.right is not None:
            #enqueue right node of temp into queue
            que.put(temp.right)
        print(temp.data,end=" ")  
#main function      
if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    print("level order traversal of tree is:")
    print_Levelorder(root)

