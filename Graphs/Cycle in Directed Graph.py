# Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

# Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

# NOTE:

# The cycle must contain atleast two nodes.
# There are no self-loops in the graph.
# There are no multiple edges between two nodes.
# The graph may or may not be connected.
# Nodes are numbered from 1 to A.
# Your solution will run on multiple test cases. If you are using global variables make sure to clear them.


# Problem Constraints
# 2 <= A <= 105

# 1 <= M <= min(200000,A*(A-1))

# 1 <= B[i][0], B[i][1] <= A



# Input Format
# The first argument given is an integer A representing the number of nodes in the graph.

# The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].



# Output Format
# Return 1 if cycle is present else return 0.



# Example Input
# Input 1:

#  A = 5
#  B = [  [1, 2] 
#         [4, 1] 
#         [2, 4] 
#         [3, 4] 
#         [5, 2] 
#         [1, 3] ]
# Input 2:

#  A = 5
#  B = [  [1, 2]
#         [2, 3] 
#         [3, 4] 
#         [4, 5] ]


# Example Output
# Output 1:

#  1
# Output 2:

#  0


# Example Explanation
# Explanation 1:

#  The given graph contain cycle 1 -> 3 -> 4 -> 1 or the cycle 1 -> 2 -> 4 -> 1
# Explanation 2:

#  The given graph doesn't contain any cycle.

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, a,b):
        adj_list=[[] for _ in range(a+1)]
        for e in b:
            adj_list[e[0]].append(e[1])

        visited=[False]*(a+1)
        path=[False]*(a+1)

        for i in range(1,a+1):
            if not visited[i] and self.dfs(visited,path,i,adj_list):
                return 1
        return 0

    def dfs(self,visited,path,src,adj_list):
        visited[src]=True
        path[src]=True

        for nbr in adj_list[src]:
            if path[nbr]==True:
                return True
            if visited[nbr] and self.dfs(visited,path,nbr,adj_list):
                return True
        path[src]=False
        return False





