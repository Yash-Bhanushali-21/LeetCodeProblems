class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        _counter = 0
        _solutionStepsArray = []
        _startIndexOfUnwantedCharacters = -1
        
        for i in range(1,n + 1):
            if _counter > len(target) - 1:
                break
            elif i == target[_counter]:
                if _startIndexOfUnwantedCharacters > -1:
                    _solutionStepsArray += [ "Pop"] * (i - _startIndexOfUnwantedCharacters)
                    _startIndexOfUnwantedCharacters = -1
                _counter+=1
             
            elif i != target[_counter] and _startIndexOfUnwantedCharacters == -1:
                _startIndexOfUnwantedCharacters = i  
                
            _solutionStepsArray.append("Push")
             
        return _solutionStepsArray

            
            
                
        