# You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

# Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
# Notice that you can apply the operation on the same pile more than once.

# Return the minimum possible total number of stones remaining after applying the k operations.

# floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).

# Example 1:

# Input: piles = [5,4,9], k = 2
# Output: 12
# Explanation: Steps of a possible scenario are:
# - Apply the operation on pile 2. The resulting piles are [5,4,5].
# - Apply the operation on pile 0. The resulting piles are [3,4,5].
# The total number of stones in [3,4,5] is 12.

# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/

import heapq
import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for i in range(k):
            top = piles[0]
            difference = math.floor(abs(heapq.heappop(piles)) / 2)
            result = abs(top) - difference
            heapq.heappush(piles, -result)

        return abs(sum(piles))

# You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

# You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

# Return the minimum cost of connecting all the given sticks into one stick in this way.

# Example 1:

# Input: sticks = [2,4,3]
# Output: 14
# Explanation: You start with sticks = [2,4,3].
# 1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
# 2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
# There is only one stick left, so you are done. The total cost is 5 + 9 = 14.

# https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/

import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            first_value = heapq.heappop(sticks)
            second_value = heapq.heappop(sticks)
            sum = first_value + second_value
            cost += sum
            heapq.heappush(sticks, sum)
    
        return cost

# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

# https://leetcode.com/problems/top-k-frequent-words/description/

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
          counter = Counter(words)
          heap = []

          for key,val in counter.items():
            heapq.heappush(heap,(-val, key))

          result = []

          while len(result) < k: result.append(heapq.heappop(heap)[1])

          return result

          

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Example 1:


# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# https://leetcode.com/problems/k-closest-points-to-origin/description/

from collections import Counter
import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []

        for point in points:
            heapq.heappush(heap, (math.sqrt(point[0]**2 + point[1]**2), point))

        while len(ans) < k:
            ans.append(heapq.heappop(heap)[1])
    
        return ans
