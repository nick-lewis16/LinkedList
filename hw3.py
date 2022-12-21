#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 00:00:00 2022

@author: Nick Lewis
"""


class Node:
    # 1
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self, pythonList = None):
        # 2
        self.first = None
        self.last = None
        self.len = 0
        
        if type(pythonList) is list and len(pythonList) > 0:
            self.first = Node(pythonList[0])
            self.len = 1
            #temp node used to traverse through list and connect between nodes
            temp = self.first
            for i in range(1, len(pythonList)):
                #Set temp.next to the next node, then update our temp node to temp.next
                iterator_node = Node(pythonList[i])
                temp.next = iterator_node
                temp = temp.next
                self.len += 1

            self.last = temp
            temp = None
            
    def append(self, data):
        this_node = Node(data)

        #Case 1: Empty linked list appending
        if self.first is None and self.last is None:
            self.first = this_node
            self.last = this_node
            self.len = 1
            return
        
        #Case 2: Non-empty list appending
        self.last.next = this_node
        self.last = this_node
        self.len += 1
    
    def prepend(self, data):
        this_node = Node(data)

        #Case 1: Empty linked list prepending
        if self.first is None and self.last is None:
            self.first = this_node
            self.last = this_node
            self.len = 1
            return
        
        #Case 2: Non-empty list prepending
        this_node.next = self.first
        self.first = this_node
        self.len += 1
        
    def __len__(self):
        return self.len
    
    
    def __eq__(self, other):
        if self.len != other.len:
            return False
        
        this_temp = self.first
        other_temp = other.first  
        
        for i in range(self.len):
            if this_temp.data != other_temp.data:
                return False
            this_temp = this_temp.next
            other_temp = other_temp.next  
            
        return True
    
    def __str__(self):
        this_temp = self.first
        L = "["
        for i in range(self.len):
            L += Node.__str__(this_temp) + " -> "
            this_temp = this_temp.next
        L += "]"
        return L

    def __repr__(self):
        this_temp = self.first
        L = "LinkedList(["
        for i in range(self.len):
            L += Node.__str__(this_temp) + ", "
            this_temp = this_temp.next
        L = L.rstrip(', ') 
        L += "])"
        return L        

    def insert(self, data, idx):
        if idx == 0:
            self.prepend(data)
            return
        if idx == self.len:
            self.append(data)
            return
        
        temp = self.first
        for i in range(idx-1):
            temp = temp.next
        
        insertion_node = Node(data)
        insertion_node.next = temp.next
        temp.next = insertion_node
        self.len += 1


LL = LinkedList(['8', [8], [8], '8'])
LL.append(1)
LL.append(2)
LL.prepend(-1)
LL.prepend(-2)
LL.insert(0,4)
print(len(LL), LL.first, LL.last)
print(LL)
print(repr(LL))
print(eval(repr(LL)) == LL)