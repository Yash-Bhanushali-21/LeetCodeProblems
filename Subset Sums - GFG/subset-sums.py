#User function Template for python3
class Solution:
    def solve(self,index,arr,currentSolution, solution):
        solution.append(sum(currentSolution[:]))
        
        for i in range(index, len(arr)):
            currentSolution.append(arr[i])
            self.solve(i + 1, arr, currentSolution, solution)
            currentSolution.pop()
        
	def subsetSums(self, arr, N):
	    currentSolution,solution = [],[]
	    self.solve(0,arr,currentSolution,solution)
	    return solution
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends