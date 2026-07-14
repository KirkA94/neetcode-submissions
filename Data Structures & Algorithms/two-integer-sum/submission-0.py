class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict1 = {}
        position = 0

        for num in nums:
            need = target - num

            if need  not in dict1:
                dict1[num] = position
                position += 1
            else:
                return [dict1[need], position]
               

     

        
            



