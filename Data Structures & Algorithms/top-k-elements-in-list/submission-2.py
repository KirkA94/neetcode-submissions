class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
       

        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1

        highest_first = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        first_two = list(highest_first)[:k]


        

        return first_two
      

        