class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        

        for t in range(len(nums)):
            for u in range(t + 1, len(nums)):
                if nums[t] + nums[u] == target:
                    return [t, u]
        
        

                
