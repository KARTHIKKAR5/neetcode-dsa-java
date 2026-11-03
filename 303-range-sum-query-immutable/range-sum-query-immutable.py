class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = []
        sum = 0 
        for i in nums:
            sum+= i
            self.prefix.append(sum)

        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        if left > 0 & 3:
            return self.prefix[right] - self.prefix[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)