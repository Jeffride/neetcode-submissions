import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # output ordering doesn't matter
        # input: nums (array), k (int)
        # return the top k most freq. elements in array
        # eg: nums = [1,2,2,3,3,3], k = 2 Output: [2,3]
        # k : 1 <= k <= number of distinct elements in nums.

        occurences = defaultdict(int)

        output = []
        for num in nums:
            occurences[num]+=1 

        while k > 0:
            largest_key = max(occurences, key=occurences.get)
            output += [largest_key]
            occurences.pop(largest_key) #remove key after use
            k -=1
            
        return output


