class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dict1 = {}
        
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1

        for char in t:
            if char not in dict1:
                return False

            if char in dict1:
                dict1[char] -= 1

            if dict1[char] < 0:
                return False

        return True
            

                
                


                


        
        