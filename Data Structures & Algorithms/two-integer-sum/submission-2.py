class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #constraints i!=j
        # every input has one i,j that satisfy target
        # return answer with smaller index first

        indices = {}  # val -> index

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in indices and indices[diff] != i:
                return [indices[diff],i]
            
            indices[nums[i]] = i #store after check to avoid overwrite
        return []


             

