# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        final_list = []
        final_list.append(pairs[:])

        for i in range(1, len(pairs)):
            j = i - 1
            current = pairs[i]

            while j >= 0 and pairs[j].key > current.key:
                pairs[j + 1] = pairs[j]
                j -= 1

            pairs[j + 1] = current
            final_list.append(pairs[:])

        return final_list