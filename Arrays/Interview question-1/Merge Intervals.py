# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.



# Problem Constraints
# 0 <= |intervals| <= 105



# Input Format
# First argument is the vector of intervals

# second argument is the new interval to be merged



# Output Format
# Return the vector of intervals after merging



# Example Input
# Input 1:

# Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
# Input 2:

# Given intervals [1, 3], [6, 9] insert and merge [2, 6] .


# Example Output
# Output 1:

#  [ [1, 5], [6, 9] ]
# Output 2:

#  [ [1, 9] ]


# Example Explanation
# Explanation 1:

# (2,5) does not completely merge the given intervals
# Explanation 2:

# (2,6) completely merges the given intervals

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        res = []
        N = len(intervals)
        for i in range(N):
           
            if newInterval.start > intervals[i].end:
                res.append(intervals[i])

            elif intervals[i].start > newInterval.end:
                res.append(newInterval)
                k = i
                while k < N:
                    res.append(intervals[k])
                    k += 1
                return res

            else:
                newInterval.start = min(newInterval.start,intervals[i].start)
                newInterval.end = max(newInterval.end,intervals[i].end)
               

        res.append(newInterval)
        return(res)
    
obj=Solution()
print(obj.insert( [ [1, 3], [6, 9] ], [2, 5]))