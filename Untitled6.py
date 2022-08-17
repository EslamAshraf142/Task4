#!/usr/bin/env python
# coding: utf-8

# In[1]:


#How to create destructor in python

class Student:
     # constructor
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('Object initialized')

    def show(self):
        print('Hello, my name is', self.name)

    # destructor
    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')

# create object
s1 = Student('Emma')
s1.show()

# delete object
del s1


# In[11]:


# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

dict = {'ravi': '10', 'rajnish': '9','sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)


# In[ ]:


#Compare between Adjacency Matrix/List:
#Adjacency List: An Adjacency list is an array consisting of the address of all the linked lists. The first node of the linked list represents the vertex and the remaining lists connected to this node represents the vertices to which this node is connected. This representation can also be used to represent a weighted graph. The linked list can slightly be changed to even store the weight of the edge.
#Adjacency Matrix: Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph. Let the 2D array be adj[][], a slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j. Adjacency matrix for undirected graph is always symmetric. Adjacency Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w.


# In[ ]:


#Breadth First Search (BFS) algorithm traverses a graph in a breadthward motion and uses a queue to remember to get the next vertex to start a search when a dead end occurs in any iteration.

#Depth First Search (DFS) algorithm traverses a graph in a depthward motion and uses a stack to remember to get the next vertex to start a search when a dead end occurs in any iteration.


# In[ ]:





# In[ ]:





# In[ ]:




