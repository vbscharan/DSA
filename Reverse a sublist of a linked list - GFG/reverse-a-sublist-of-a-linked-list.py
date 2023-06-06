#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverseBetween(self, head, m, n):
        #code here
        def reverse(start,end):
            left=None
            k=start
            while start and start!=end:
                right=start.next
                start.next=left
                left=start
                start=right
            return left,k
        prevbeglist=None
        beglist=endlist=head
        #get to starting of mth node
        while m!=1 and beglist:
            prevbeglist=beglist
            beglist=beglist.next
            m-=1
        #get to starting node of n
        while n!=1 and endlist:
            endlist=endlist.next
            n-=1
        #print(beglist.data)
        #print(endlist.data)
        
        nextendlist=endlist.next
        #get the head of reversed sub list
        reversedhead,reversedtail=reverse(beglist,nextendlist)
        
        #print(reversedhead.next.data)
        if prevbeglist:
            prevbeglist.next=reversedhead
        else:
            head=reversedhead
        if nextendlist:
            reversedtail.next=nextendlist
        
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self, head):
        if head is None:
            print(' ')
            return
        curr_node = head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print()
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        inp = list(map(int,input().split())) 
        N=inp[0]
        m=inp[1]
        n=inp[2]
        
        a = LinkedList() # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
            
       
        ob=Solution()
        newhead=ob.reverseBetween(a.head, m, n)
        a.printList(newhead)
# } Driver Code Ends