class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        firstPoint = points[0]
        for secondPoint in points:
            count += max(abs(firstPoint[0] - secondPoint[0]) , abs(firstPoint[1] - secondPoint[1]))
            firstPoint=secondPoint
        return count