class Solution:    

    def leadsToTerminalNodeViaBFS(self,graph,node,safe):
        if node in safe:
            return safe[node]
        
        safe[node] = False
        
        adjacentNodes = graph[node]

        for i in adjacentNodes:
            if not self.leadsToTerminalNodeViaBFS(graph,i,safe):
                return False

        safe[node] = True
        return True
            
        
        
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        eventualSafeNodes = []
        safe = {}
        for node in range(0,n):
            if self.leadsToTerminalNodeViaBFS(graph, node, safe):
                eventualSafeNodes.append(node)
        return eventualSafeNodes
            
            