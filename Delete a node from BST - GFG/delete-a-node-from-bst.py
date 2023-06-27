#User function Template for python3


#Function to delete a node from BST.
def deleteNode(root, X):
    # code here.
    def count(root):
        if root is None:
            return 0
        return 1+count(root.left)+count(root.right)
    def delete(root,X,curr):
        if root is None:
            return 
        if X<root.data:
            if root.left:
                root.left=delete(root.left,X,curr)
        elif X>root.data:
            if root.right:
                root.right=delete(root.right,X,curr)
        else:
            if root.left is None:
                temp=root.right
                if X==curr:
                    root.data=temp.data
                    root.left=temp.left
                    root.right=temp.right
                    temp=None
                    return
                root=None
                return temp
            if root.right is None:
                temp=root.left
                if X==curr:
                    root.data=temp.data
                    root.left=temp.left
                    root.right=temp.right
                    temp=None
                    return
                root=None
                return temp
            node=root.right
            while node.left:
                node=node.left
            root.data=node.data
            root.right=delete(root.right,node.data,curr)
        return root
    if count(root)==1 and root.data==X:
        return None
    return delete(root,X,root.data)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
# A utility function to do inorder traversal of BST 
def inorder(root): 
    if root is not None: 
        inorder(root.left) 
        print (root.data, end=' '),
        inorder(root.right) 
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        x=int(input())
        root=buildTree(s)
        root = deleteNode(root,x)
        inorder(root)
        print()
        
# } Driver Code Ends