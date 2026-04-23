class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:    
        res = []
        cursor = 0
        intervals.sort()

        while cursor<len(intervals):
            if cursor:                            
                start = res[-1][0]
                stop = res[-1][-1]

                if intervals[cursor][0] <= stop:
                    res[-1][-1] = max(intervals[cursor][-1], stop)                    
                else:
                    res.append(intervals[cursor])
            else:
                res.append(intervals[cursor])                    
            cursor+=1                
        return res
