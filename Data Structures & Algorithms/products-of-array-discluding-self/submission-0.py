class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        i = 0

        while i < len(nums):
            j = 0
            value = 1
            while j < len(nums):
                if j != i:
                    value = value * nums[j]
                    
                j += 1

            output.append(value)
            value = 1
            i += 1

        return output
                
        