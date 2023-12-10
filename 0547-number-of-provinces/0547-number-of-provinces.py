class Solution:
    def DFS(self, visited, node, isConnected):
        visited[node] = 1
        adj = []
        for ind in range(0, len(isConnected)):
            if isConnected[node][ind] == 1:
                adj.append(ind)
        for x in adj:
            if x not in visited:
                self.DFS(visited,x ,isConnected)
            
        
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = {}
        count = 0
        for i in range(0,len(isConnected)):
            if i not in visited:
                count+=1
                self.DFS(visited, i , isConnected)
                
                    
        return count
                    
        