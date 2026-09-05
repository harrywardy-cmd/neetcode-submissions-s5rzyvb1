class Solution:
    def findLucky(self, arr: List[int]) -> int:

        my_dict = {}
        result = -1

        for i in arr:
            my_dict[i] = my_dict.get(i, 0) + 1

        for i in my_dict:
            if i == my_dict[i]:
                result = max(my_dict[i], result)

        print(my_dict)
        return result