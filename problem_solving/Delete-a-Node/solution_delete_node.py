import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>PROBLEM<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<            

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    
  
    count = 0
    current = head 
    
    while count <= position:
        prev_node = current
        current = prev_node.next
        
        if position == 0:
            head = head.next
            
        elif count == position-1:
            prev_node.next = current.next
    
        count +=1
        
    return head
        