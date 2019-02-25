#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""BinTreeAssignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WioNx1yUBouBiJB65tuX4o3iL3mm2Ibs

## Binary Tree Class##

**Create a BinTree class** that uses the Node class below to create an ordered binary tree. 

The nodes (below) have a value instance variable that is comparable with the normal Python operators: "<", "<=" and "==", ">=" and ">".

The nodes also have pointers to their child nodes.
"""

class Node:
    def __init__(self, data):
        self.value = data  # An integer
        self.smaller = None
        self.larger = None
        
    def __str__(self):
        return str(self.value)

"""**Complete and test the methods below.**

> Indented block



**Note**: the _clear()_ method is tricky to code.  What you want to accomplish is to set every node's pointers to other nodes to None. If you have just 2 pointers to the left and right (larger and smaller) children of that node, then walk the tree carefully, and set those pointers in every node to None. This must be done from the bottom up. Once all of the pointers to a block of memory (in this case, a node) are removed, that block of memory becomes inaccessible, and should be collected by the garbage-collector later.
"""

import math
import sys


class BinTree:
    def __init__(self, A = None):
      # A is an optional argument containing a list of values to be inserted into the binary tree just after construction
      if (A == None):
        self.Tvalue = None   #self.Tvalue is a Node
      else:
        n = len(A)
        self.Tvalue = Node(A[0])
        q = 1
        while (q < n):
          self.insert(A[q])
          q+=1
        
    def insert(self, V):
      # inserts a new value
      if (self.Tvalue == None):
        self.Tvalue = Node(V)
      else:
        self._insert(V,self.Tvalue)
      
    def _insert(self,V,node):
      if (V > node.value): #if value is larger
        if (node.larger == None): #if node is empty
          node.larger = Node(V) #make it the node
        else:
          self._insert(V,node.larger) #keep searching
      elif (V < node.value): #if value is smaller
        if (node.smaller == None): #if node is empty
          node.smaller = Node(V) #make it the node
        else:
          self._insert(V,node.smaller) #keep searching
        
    def has(self, V):
      # returns True if V is in the list, else False
      if (self.Tvalue == None):
        return False
      else:
        return self._has(V,self.Tvalue) 
        
    def _has(self, V, node):
      if (V == node.value):
        return True #V does exist
      if (V > node.value):
        if (node.larger == None): #No larger node
          return False 
        else:
          return self._has(V,node.larger) #larger node exists, finding larger node
      elif(V < node.value):
        if (node.smaller == None): #No smaller node
          return False
        else:
          return self._has(V,node.smaller) #smaller node exists, finding smaller node


    def get_ordered_list(self):
        # returns a list of all values in ordered sequence
      if (self.Tvalue == None):
        return "nothing in list"
      List = []
      return self._get_ol(List,self.Tvalue)
     
    def _get_ol(self,List,node):
      if (node == None):
        return
      self._get_ol(List,node.smaller)
      List.append(node.value)
      #print(node.value)
      self._get_ol(List,node.larger)
      return List
        
        
    def clear(self):
      # clears the list of all nodes
      if (self.Tvalue == None):
        return 
      self._clear(self.Tvalue)


      #self.Tvalue.value = None
      #self.Tvalue = None
      
    def _clear(self, node):
      if (node != None):
        if (node.smaller != None or node.larger != None): #Arrived at the bottom
          self._clear(node.smaller) 
          self._clear(node.larger)
          node.value = None
          node = None
        elif (node.smaller == None and node.larger == None):
          node.value = None
          node = None

          
    '''search the tree for the value V and return the depth (level) of the tree where it was found (root = 1), 
      or, if not found, then the level of leaf where it gave up. 
      In other words, it counts the number of nodes examined in the search.'''
    def has_depth(self,V):
      if (self.Tvalue == None):
        return 1
      return self._has_depth(1,V,self.Tvalue)
    
    def _has_depth(self,root,V,node):
      if (V == node.value):
        return root #V does exist
      if (V > node.value):
        if (node.larger == None): #No larger node
          return root 
        else:
          return self._has_depth(root+1,V,node.larger) #larger node exists, finding larger node
      elif(V < node.value):
        if (node.smaller == None): #No smaller node
          return root
        else:
          return self._has_depth(root+1,V,node.smaller) #smaller node exists, finding smaller node
   
      
      
      
def Process(infilename,outfilename):
  f = open(infilename,'r')
  ctr = 0
  if '\r\n' in f.read():
    lines = f.read().split('\r\n')
  else:
    ctr = 1
    lines = f.read().split('\n')
  words = lines[0].split(',')
  ints = []
  avg = 0.0
  for i in words:
    ints.append(int(i))
    avg += int(i)
  avg /= len(words)
  print("avg value is " + str(avg))
  logval = math.log(len(words),2)
  print("log base 2 value is " + str(logval))
  
  A = BinTree(ints)
  #use lines[1] , which is argument for has_depth
  args = lines[1].split(',')
  retval = []
  for i in args:
    retval.append( str( A.has_depth( int(i) ) ) ) #add the str val of the int result from has_depth for each input
  
  g = open(outfilename,'w')
  s = ','.join(retval)
  if ctr == 1:
    g.write(s + '\n')
  else:
    g.write(s + '\r\n')
  f.close()
  g.close()
  

def main():
    Process(sys.argv[1],sys.argv[2])
    
          
          
'''           
T= BinTree([50])
T.insert(30) 
T.insert(20) 
T.insert(60) 
T.insert(40) 
T.insert(70)
T.insert(80)
print(T.has(50))
print(T.has(80))
print(T.has(90))
print(T.get_ordered_list())
print(T.has_depth(30))
print(T.has_depth(80))
print(T.has_depth(90))
print("clearing...")
T.clear()
print(T.get_ordered_list())
'''

'''
from google.colab import drive
drive.mount('/content/gdrive')

import os
print (sorted(os.listdir('../Colab Notebooks')))
'''
