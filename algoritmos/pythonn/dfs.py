import sys
sys.stdin = open('file.in', 'r')
sys.stdout = open('file.out', 'w')

import os
#import sys
print(os.path.dirname(sys.executable))

print("----------------")
state = tuple([1,2,3,0,0,0])
for i, item in enumerate(state):
    if item == 0:
        print(i,item)
print("----------------")


print("----------------")
state = [1,2,3,0,0,0]
for i in range(6):
    print(state.count(i)," k")
print("----------------")

[n, m, k] = map(int, input().split(' '))
[a,b,c,d] = map(int, input().split(' '))
mat = [[0 for i in range(m)] for j in range(n)]

print(n)
print(m)
print(k)
print(a," ",b," ",c," ",d)
for i in mat:
    print(i)

aa = [1,2,3,4]
print(aa)
aa[2] = 10
print(aa)

kk= list(map(int, '1 2 3 4 5 6'.split(' ')))
print(kk)
# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')
